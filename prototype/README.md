# Trotamundos prototype

Run with Docker Compose:

```bash
cp .env.example .env
docker compose up --build
```

API: http://localhost:8000/docs
Provider simulator: http://localhost:8001/docs
RabbitMQ management: http://localhost:15672

Use `POST /simulate` in the simulator Swagger UI to create, update, or cancel a hotel reservation. Then query `GET /reservations/{reservation_id}` in the API. The read projection is asynchronous, so retry after a short wait if it returns 404.

Run tests locally with `pip install -e '.[test]'` and `pytest`.

This is a prototype, not production-ready. The real provider integration, out-of-order event policy, and broader failure-injection tests remain open.