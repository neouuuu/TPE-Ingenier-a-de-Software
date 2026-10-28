# Vista de componentes y conectores — ADD-1

```mermaid
flowchart LR
  CLIENT[Web / móvil] -->|HTTPS request-response| API[API de aplicación]
  API --> DOMAIN[Servicios de dominio]
  DOMAIN <--> DB[(Base operativa)]
  DOMAIN -->|evento interno| BUS[[Canal de eventos]]
  WORKER[Workers asíncronos] <--> BUS
  WORKER --> PORT[Puertos y adaptadores]
  PORT <--> MAIL[API correo]
  PORT <--> TRAVEL[APIs turísticas]
  PORT <--> AGENCY[API agencia si existe]
  PORT <--> MAPS[API mapas]
  PORT --> SOCIAL[API social]
  BUS --> ETL[Proyección analítica]
  ETL --> ADB[(Almacén analítico)]
  API --> REC[Recomendador]
  REC --> ADB
```

HTTPS request-response sirve al usuario; eventos internos desacoplan procesamiento, reintentos y notificaciones. No se presupone que todos los proveedores externos emitan eventos. La entrega, idempotencia y DLQ se detallan en ADD-3.
