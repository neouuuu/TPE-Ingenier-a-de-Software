import os
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://trotamundos:trotamundos@localhost:5432/trotamundos")
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/%2F")
PROVIDER_SHARED_SECRET = os.getenv("PROVIDER_SHARED_SECRET", "local-dev-secret-change-me")
WEBHOOK_MAX_SKEW_SECONDS = int(os.getenv("WEBHOOK_MAX_SKEW_SECONDS", "300"))
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "reservation.events")
RABBITMQ_DLQ = os.getenv("RABBITMQ_DLQ", "reservation.events.dlq")
