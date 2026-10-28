import json, time
from uuid import uuid4
import httpx
from fastapi import FastAPI, HTTPException
from app.config import PROVIDER_SHARED_SECRET
from app.schemas import SimulationRequest
from app.security import signature_for

app = FastAPI(title="Simulador independiente de proveedor hotelero")
API_URL = "http://api:8000/webhooks/hotel-provider"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/simulate")
async def simulate(request: SimulationRequest):
    data = request.model_dump()
    operation = data.pop("operation")
    if operation == "cancel":
        data["status"] = "cancelled"
        event_type = "reservation.cancelled"
    elif operation == "update":
        event_type = "reservation.updated"
    else:
        event_type = "reservation.created"
    body = json.dumps({"event_type": event_type, "reservation": data}, separators=(",", ":")).encode()
    timestamp = str(int(time.time()))
    headers = {
        "Content-Type": "application/json",
        "X-Provider-Timestamp": timestamp,
        "X-Provider-Signature": signature_for(PROVIDER_SHARED_SECRET, timestamp, body),
        "X-Provider-Event-Id": str(uuid4()),
    }
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.post(API_URL, content=body, headers=headers)
    except httpx.HTTPError as exc:
        raise HTTPException(502, f"No se pudo contactar la API: {exc}") from exc
    if response.status_code >= 400:
        raise HTTPException(response.status_code, response.text)
    return {"provider_response": response.json(), "event_type": event_type}
