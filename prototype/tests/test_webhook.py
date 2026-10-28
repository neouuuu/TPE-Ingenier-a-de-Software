import time
from fastapi.testclient import TestClient
from app.main import app

def test_health_endpoint():
    with TestClient(app) as client:
        assert client.get('/health').json() == {'status': 'ok'}

def test_invalid_signature_is_rejected():
    with TestClient(app) as client:
        response = client.post('/webhooks/hotel-provider', content=b'{}', headers={
            'X-Provider-Timestamp': str(int(time.time())),
            'X-Provider-Signature': 'sha256=invalid',
            'X-Provider-Event-Id': 'evt-test',
        })
        assert response.status_code == 401
