# Vista de resiliencia y seguridad — ADD-3

```mermaid
flowchart TB
  subgraph TrustBoundary["Límite de confianza: API propia"]
    CLIENT["Web / móvil"] --> EDGE["Entrada HTTPS + rate limit"]
    EDGE --> IAM["Autenticación / autorización"]
    IAM --> API["API y servicios de aplicación"]
    API --> DOMAIN["Dominio / validación de negocio"]
    DOMAIN --> TX[("Transacción operativa + outbox")]
    TX --> DB[("Base operativa")]
    TX --> OUTBOX[("Outbox persistente")]
    IAM --> TOKENS[("Almacén cifrado de credenciales/tokens")]
    IAM --> AUDIT["Auditoría de acceso"]
  end

  subgraph ExternalBoundary["Integraciones externas aisladas"]
    PROVIDER["API correo / turismo / agencia"]
    ADAPTER["Adaptador con validación de contrato"]
    LIMIT["Rate limiter + timeout"]
    CB{"Circuit breaker"}
    RETRY["Reintentos limitados con backoff + jitter"]
    WORKER["Worker idempotente"]
    RECON["Reconciliación"]
    PROVIDER <-->|"HTTPS / webhook opcional"| ADAPTER
    ADAPTER --> LIMIT
    LIMIT --> CB
    CB -->|"cerrado: permitido"| RETRY
    RETRY --> WORKER
    WORKER --> RECON
    RECON --> DOMAIN
    TOKENS -.->|"credenciales necesarias"| ADAPTER
    CB -->|"abierto / timeout"| FAIL["Registrar fallo y mantener último dato válido"]
  end

  subgraph ReliableEvents["Entrega fiable de eventos"]
    RELAY["Relay de outbox"]
    BROKER[["Broker durable"]]
    CONSUMER["Consumidores idempotentes"]
    DLQ[("DLQ")]
    ALERT["Alerta + reproceso autorizado"]
    OUTBOX --> RELAY
    RELAY -->|"publicar y reintentar"| BROKER
    BROKER -->|"at-least-once"| CONSUMER
    CONSUMER -->|"fallo agotados reintentos"| DLQ
    DLQ --> ALERT
  end

  subgraph SecurityControls["Controles transversales"]
    SECRETS["Gestor de secretos + rotación"]
    OBS["Métricas, trazas y logs redactados"]
    POLICY["Política de mínimo privilegio / scopes"]
  end
  SECRETS -.-> TOKENS
  POLICY -.-> IAM
  API -.-> OBS
  WORKER -.-> OBS
  RELAY -.-> OBS
  ALERT -.-> OBS
  AUDIT -.-> OBS
```

## Invariantes y decisiones operativas

- Tokens de correo nunca van en código, URLs ni logs; se cifran, se restringen por scope y se eliminan/revocan al desconectar la cuenta.
- Cada proveedor tiene límites de concurrencia y políticas de timeout/reintento propias; un circuito abierto no bloquea integraciones no relacionadas.
- Se conserva el último dato válido cuando una fuente falla; se marca el estado de sincronización y se alerta sobre antigüedad.
- Outbox evita perder el evento entre la confirmación de datos y su publicación. El broker puede entregar repetidos; consumidores idempotentes los toleran.
- DLQ no es un agujero negro: requiere alerta, retención, acceso limitado, causa visible y reproceso controlado.
- Los enlaces compartidos son de solo lectura, impredecibles, revocables y con expiración. La verificación del destinatario debe cerrarse antes del prototipo.
- La vista no prueba el SLO: deben medirse disponibilidad, latencia, backlog, errores de proveedores, recuperación y comportamiento bajo carga.
