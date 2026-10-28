# Vista de resiliencia y seguridad — ADD-3

```mermaid
flowchart LR
  PROVIDER[Proveedor externo] --> ADAPTER[Adaptador: timeout/circuit breaker]
  ADAPTER --> WORKER[Worker idempotente]
  WORKER --> VALIDATE[Validación y reconciliación]
  VALIDATE --> TX[Transacción de estado + outbox]
  TX --> DB[(Base operativa)]
  TX --> OUTBOX[(Outbox)]
  OUTBOX --> RELAY[Publicador]
  RELAY --> BUS[[Broker durable]]
  BUS --> CONSUMER[Consumidor idempotente]
  CONSUMER --> PROJ[Proyección / notificación]
  CONSUMER --> DLQ[(DLQ + alerta y reproceso)]
  IAM[Identidad y scopes mínimos] --> API[API/compartición]
  API --> AUDIT[Auditoría sin datos sensibles]
  SECRETS[Gestor de secretos] --> ADAPTER
  SECRETS --> IAM
```

## Invariantes

- Tokens de correo nunca van en código ni logs.
- Entrega al menos una vez implica consumidores idempotentes.
- La falla de un proveedor no debe bloquear todas las integraciones.
- DLQ requiere retención, alertas y proceso de reproceso.
- El diagrama no prueba el SLO: debe verificarse mediante ensayos.
