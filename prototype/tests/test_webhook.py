import time
from fastapi.testclient import TestClient
from app.main import app

# No se inicia el lifespan de la app: estas pruebas no necesitan PostgreSQL.
client = TestClient(app)

def test_health_endpoint():
    assert client.get("/health").json() == {"status": "ok"}

def test_invalid_signature_is_rejected():
    response = client.post("/webhooks/hotel-provider", content=b"{}", headers={
        "X-Provider-Timestamp": str(int(time.time())),
        "X-Provider-Signature": "sha256=invalid",
        "X-Provider-Event-Id": "evt-test",
    })
    assert response.status_code == 401
