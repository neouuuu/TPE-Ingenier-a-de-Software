import json
from datetime import datetime, timezone
from uuid import uuid4
from fastapi import FastAPI, Header, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.config import PROVIDER_SHARED_SECRET, WEBHOOK_MAX_SKEW_SECONDS
from app.db import SessionLocal, init_db
from app.models import OutboxEvent, ProviderEvent, Reservation, ReservationRead
from app.schemas import ProviderWebhook
from app.security import verify_signature

app = FastAPI(title="Trotamundos Prototype API", version="0.1.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/webhooks/hotel-provider", status_code=202)
async def provider_webhook(
    request: Request,
    x_provider_timestamp: str = Header(default=""),
    x_provider_signature: str = Header(default=""),
    x_provider_event_id: str = Header(default=""),
):
    raw = await request.body()
    if not x_provider_event_id:
        raise HTTPException(400, "Falta X-Provider-Event-Id")
    if not verify_signature(PROVIDER_SHARED_SECRET, x_provider_timestamp, raw, x_provider_signature, WEBHOOK_MAX_SKEW_SECONDS):
        raise HTTPException(401, "Firma inválida o timestamp vencido")
    try:
        event = ProviderWebhook.model_validate_json(raw)
    except Exception as exc:
        raise HTTPException(422, "Payload de webhook inválido") from exc

    reservation_data = event.reservation.model_dump()
    now = datetime.now(timezone.utc)
    internal_event_id = str(uuid4())
    payload = {"event_id": internal_event_id, "event_type": event.event_type, "reservation": reservation_data}
    with SessionLocal() as db:
        try:
            with db.begin():
                db.add(ProviderEvent(provider_event_id=x_provider_event_id))
                reservation = db.get(Reservation, reservation_data["reservation_id"])
                if event.event_type == "reservation.created" and reservation is not None:
                    raise HTTPException(409, "La reserva ya existe")
                if event.event_type != "reservation.created" and reservation is None:
                    raise HTTPException(404, "La reserva no existe; enviar primero reservation.created")
                if reservation is None:
                    reservation = Reservation(id=reservation_data["reservation_id"], provider="simulated-hotel", **{
                        k: v for k, v in reservation_data.items() if k != "reservation_id"
                    })
                    db.add(reservation)
                else:
                    reservation.guest_name = reservation_data["guest_name"]
                    reservation.hotel_name = reservation_data["hotel_name"]
                    reservation.check_in = reservation_data["check_in"]
                    reservation.check_out = reservation_data["check_out"]
                    reservation.status = "cancelled" if event.event_type == "reservation.cancelled" else reservation_data["status"]
                    reservation.version += 1
                    reservation.updated_at = now
                db.add(OutboxEvent(id=internal_event_id, event_type=event.event_type, aggregate_id=reservation_data["reservation_id"], payload=payload))
        except IntegrityError:
            # Delivery duplicada: el evento de proveedor ya fue registrado.
            db.rollback()
            if db.scalar(select(ProviderEvent).where(ProviderEvent.provider_event_id == x_provider_event_id)):
                return {"accepted": True, "duplicate": True}
            raise HTTPException(409, "Conflicto de integridad")
    return {"accepted": True, "duplicate": False, "event_id": internal_event_id}

@app.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: str):
    with SessionLocal() as db:
        row = db.get(ReservationRead, reservation_id)
        if row is None:
            raise HTTPException(404, "Reserva todavía no disponible en la proyección de lectura")
        return row.data
