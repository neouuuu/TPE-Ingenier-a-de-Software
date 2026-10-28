import json, time
from datetime import datetime, timezone
import pika
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from app.config import RABBITMQ_URL, RABBITMQ_QUEUE, RABBITMQ_DLQ
from app.db import SessionLocal, init_db
from app.models import InboxEvent, ReservationRead

def connect():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_DLQ, durable=True)
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True, arguments={
        "x-dead-letter-exchange": "",
        "x-dead-letter-routing-key": RABBITMQ_DLQ,
    })
    channel.basic_qos(prefetch_count=1)
    return connection, channel

def handle_message(body: bytes) -> bool:
    message = json.loads(body)
    event_id = message["id"]
    reservation = message["payload"]["reservation"]
    with SessionLocal() as db:
        try:
            with db.begin():
                if db.get(InboxEvent, event_id):
                    return True
                db.add(InboxEvent(id=event_id))
                db.execute(pg_insert(ReservationRead).values(
                    reservation_id=reservation["reservation_id"], data=reservation, updated_at=datetime.now(timezone.utc)
                ).on_conflict_do_update(index_elements=[ReservationRead.reservation_id], set_={
                    "data": reservation, "updated_at": datetime.now(timezone.utc)
                }))
            return True
        except Exception:
            return False

def main():
    init_db()
    while True:
        try:
            connection, channel = connect()
            def callback(ch, method, properties, body):
                ok = handle_message(body)
                if ok:
                    ch.basic_ack(method.delivery_tag)
                else:
                    # Reintentos limitados; el broker enruta a DLQ tras el límite.
                    headers = properties.headers or {}
                    count = int(headers.get("x-retry-count", 0))
                    if count >= 3:
                        ch.basic_publish(exchange="", routing_key=RABBITMQ_DLQ, body=body,
                            properties=pika.BasicProperties(delivery_mode=2, content_type="application/json"))
                        ch.basic_ack(method.delivery_tag)
                    else:
                        ch.basic_publish(exchange="", routing_key=RABBITMQ_QUEUE, body=body,
                            properties=pika.BasicProperties(delivery_mode=2, content_type="application/json",
                                headers={"x-retry-count": count + 1}))
                        ch.basic_ack(method.delivery_tag)
                        time.sleep(min(2 ** count, 8))
            channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
            print("Consumer listo", flush=True)
            channel.start_consuming()
        except Exception as exc:
            print(f"Consumer reiniciando tras error: {exc}", flush=True)
            time.sleep(2)
if __name__ == "__main__":
    main()
