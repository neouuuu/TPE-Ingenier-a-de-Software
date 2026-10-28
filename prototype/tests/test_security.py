import time
from app.security import signature_for, verify_signature

def test_signature_valid_for_exact_body():
    body = b'{"event":"reservation.created"}'
    ts = str(int(time.time()))
    sig = signature_for("secret", ts, body)
    assert verify_signature("secret", ts, body, sig, 300)

def test_signature_rejects_modified_body():
    ts = str(int(time.time()))
    sig = signature_for("secret", ts, b'{"a":1}')
    assert not verify_signature("secret", ts, b'{"a":2}', sig, 300)

def test_signature_rejects_expired_timestamp():
    ts = str(int(time.time()) - 1000)
    sig = signature_for("secret", ts, b"body")
    assert not verify_signature("secret", ts, b"body", sig, 300)
