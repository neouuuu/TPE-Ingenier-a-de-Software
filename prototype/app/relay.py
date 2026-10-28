import json, time
from datetime import datetime, timezone
import pika
from sqlalchemy import select
from app.config import RABBITMQ_URL, RABBITMQ_QUEUE
from app.db import SessionLocal, init_db
from app.models import OutboxEvent

def publish_pending():
    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.confirm_delivery()
    try:
        with SessionLocal() as db:
            events = db.scalars(select(OutboxEvent).where(OutboxEvent.published_at.is_(None)).order_by(OutboxEvent.created_at).limit(50)).all()
            for event in events:
                body = json.dumps({"id": event.id, "event_type": event.event_type, "aggregate_id": event.aggregate_id, "payload": event.payload}, separators=(",", ":")).encode()
                try:
                    confirmed = channel.basic_publish(exchange="", routing_key=RABBITMQ_QUEUE, body=body,
                        properties=pika.BasicProperties(delivery_mode=2, content_type="application/json", message_id=event.id))
                    if confirmed:
                        event.published_at = datetime.now(timezone.utc)
                    event.attempts += 1
                except Exception:
                    event.attempts += 1
            db.commit()
    finally:
        connection.close()

def main():
    init_db()
    while True:
        try:
            publish_pending()
        except Exception as exc:
            print(f"Outbox relay error: {exc}", flush=True)
        time.sleep(1)
if __name__ == "__main__":
    main()
