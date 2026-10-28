import hashlib, hmac, time
def signature_for(secret: str, timestamp: str, raw_body: bytes) -> str:
    signed = timestamp.encode("utf-8") + b"." + raw_body
    return "sha256=" + hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
def verify_signature(secret: str, timestamp: str, raw_body: bytes, signature: str, max_skew: int) -> bool:
    try:
        sent_at = int(timestamp)
    except (TypeError, ValueError):
        return False
    if abs(int(time.time()) - sent_at) > max_skew:
        return False
    return hmac.compare_digest(signature_for(secret, timestamp, raw_body), signature)
