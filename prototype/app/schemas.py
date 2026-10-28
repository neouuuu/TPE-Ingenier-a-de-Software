from typing import Literal
from pydantic import BaseModel, Field
class ReservationPayload(BaseModel):
    reservation_id: str = Field(min_length=1, max_length=100)
    guest_name: str = Field(min_length=1, max_length=200)
    hotel_name: str = Field(min_length=1, max_length=200)
    check_in: str
    check_out: str
    status: Literal["confirmed", "cancelled"] = "confirmed"
class ProviderWebhook(BaseModel):
    event_type: Literal["reservation.created", "reservation.updated", "reservation.cancelled"]
    reservation: ReservationPayload
class SimulationRequest(ReservationPayload):
    operation: Literal["create", "update", "cancel"] = "create"
