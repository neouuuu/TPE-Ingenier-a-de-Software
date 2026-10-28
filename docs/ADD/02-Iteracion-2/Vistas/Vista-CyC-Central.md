# Vista C&C — funcionalidad central (ADD-2)

La vista refina los componentes del flujo de reservas y muestra las rutas principales para registro manual, importación desde correo, sincronización turística y compartición.

```mermaid
flowchart TB
  CLIENT["Web / móvil"] -->|"HTTPS"| API["API de aplicación"]
  API --> AUTH["Autenticación / autorización"]
  AUTH --> TRIPAPI["Servicio de viajes"]
  AUTH --> RESAPI["Servicio de reservas"]
  AUTH --> SHARE["Servicio de compartición"]

  TRIPAPI --> TRIPDOM["Dominio de viajes"]
  RESAPI --> RESDOM["Dominio de reservas"]
  RESAPI --> ASSIGN["Servicio de asignación"]
  TRIPDOM --> REPO[("Repositorio operativo")]
  RESDOM -->|"validación de reglas"| ASSIGN
  ASSIGN -->|"transacción: reserva + asociación"| REPO

  subgraph EmailIngestion["Ingesta de correo"]
    TIMER["Webhook del proveedor si existe / planificador fallback"]
    MAILADAPTER["Adaptador correo OAuth"]
    FILTER["Filtros + remitentes confiables"]
    PARSER["Extractor de reserva"]
    NORMALIZER["Normalizador a modelo canónico"]
    DEDUP["Deduplicación idempotente"]
    TIMER --> MAILADAPTER
    MAILADAPTER -->|"mensajes autorizados"| FILTER
    FILTER --> PARSER
    PARSER --> NORMALIZER
    NORMALIZER --> DEDUP
    DEDUP -->|"candidato validado"| RESAPI
  end

  subgraph ProviderSync["Sincronización turística"]
    SYNC["Planificador / receptor de notificaciones"]
    TRAVELPORT["Puerto turístico"]
    TRAVELADAPTER["Adaptador turístico"]
    PROVIDER["API turística"]
    RECON["Validación + reconciliación"]
    SYNC --> TRAVELPORT
    TRAVELPORT --> TRAVELADAPTER
    TRAVELADAPTER <-->|"API estándar"| PROVIDER
    TRAVELADAPTER --> RECON
    RECON -->|"cambio validado"| RESAPI
  end

  AGENCYPORT["Puerto agencia preferida"] --> AGENCYADAPTER["Adaptador de agencia"]
  AGENCYADAPTER <-->|"API oficial, si existe"| AGENCYAPI["API de agencia"]
  RESAPI --> AGENCYPORT

  RESDOM -->|"cambio confirmado"| OUTBOX[("Outbox transaccional")]
  OUTBOX --> RELAY["Publicador"]
  RELAY --> BUS[["Broker de eventos internos"]]
  BUS --> NOTIFY["Consumidor de notificaciones"]
  NOTIFY --> NOTIFYPORT["Puerto de notificación"]
  NOTIFYPORT --> CHANNEL["Canal habilitado para el usuario"]

  SHARE --> LINK["Emisor de enlace de solo lectura"]
  LINK --> MAILOUT["Adaptador de envío de correo"]
  SHARE --> SOCIALADAPTER["Adaptador social"]
  SOCIALADAPTER -->|"publicación confirmada por usuario"| SOCIALAPI["API social"]

  DLQ[("DLQ / errores de procesamiento")]
  MAILADAPTER -.->|"error no recuperable"| DLQ
  PARSER -.->|"mensaje no interpretable"| DLQ
  RECON -.->|"respuesta inválida"| DLQ
```

## Contratos y semántica

- Las acciones interactivas se responden por HTTPS; la ingesta y las notificaciones no bloquean la petición del usuario.
- La importación produce una **reserva candidata**. Solo después de validación y deduplicación se registra; no se inventa la asociación a un viaje.
- Las actualizaciones externas se reconcilian con el modelo canónico. La precedencia entre edición manual y datos externos sigue abierta y no se resuelve con “último evento gana”.
- Las escrituras publican eventos mediante outbox para evitar confirmar un cambio sin dejar registro de su evento pendiente.
- Los adaptadores de correo, turismo y agencia ocultan detalles del proveedor. La integración directa de agencia depende de una API compatible y autorizada.
- DLQ, alertas y reproceso deben tener responsables y límites de retención; los fallos no deben borrar la última información válida.
