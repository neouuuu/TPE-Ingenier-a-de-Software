# Vista C&C de lectura, analítica y recomendaciones — ADD-4

```mermaid
flowchart TB
  subgraph Interactive["Camino interactivo"]
    CLIENT["Web / móvil"] -->|"HTTPS request/response"| API["API de aplicación"]
    API --> AUTH["Autorización por usuario/rol"]
    AUTH --> QUERY["Servicio de consulta"]
    QUERY --> CACHE[("Caché opcional, clave por usuario")]
    QUERY --> READ[("Proyección de lectura")]
    READ --> QUERY
    QUERY -->|"DTO versionado"| API
  end

  subgraph WriteAndEvents["Actualización de datos"]
    DOMAIN["Servicios de dominio"] --> TX[("Base operativa + outbox transaccional")]
    TX --> OUTBOX[("Outbox")]
    OUTBOX --> RELAY["Relay"]
    RELAY --> BUS[["Broker de eventos"]]
    BUS --> PROJCON["Consumidor idempotente de proyecciones"]
    PROJCON --> READ
    BUS --> ETL["Pipeline de analítica"]
    ETL --> DW[("Almacén analítico separado")]
  end

  subgraph Analytics["Acceso analítico controlado"]
    TEAM["Equipo de análisis"] --> ANALYTICSAPI["API / entorno de consultas autorizado"]
    ANALYTICSAPI --> POLICY["Autorización, auditoría y límites de consulta"]
    POLICY --> DW
    POLICY --> AUDIT["Registro de auditoría"]
  end

  subgraph Recommendation["Servicio de recomendación desacoplado"]
    RECAPI["API de recomendaciones"] --> REC["Motor de recomendación"]
    REC --> FEATURES["Selector de características autorizadas"]
    FEATURES --> READ
    REC --> MODEL[("Modelo / versión activa")]
    REC --> RESULTS["Sugerencias tipadas"]
    RESULTS --> RECAPI
    RECAPI -->|"respuesta o fallback"| API
    CLIENT -->|"aceptar / ajustar"| RECAPI
    RECAPI --> FEEDBACK["Registro mínimo de feedback"]
    FEEDBACK --> FEEDBACKBUS[["Evento de feedback"]]
    FEEDBACKBUS --> EVAL["Evaluación por lotes"]
    EVAL --> REGISTRY["Registro de modelos"]
    REGISTRY --> MODEL
  end

  MONITOR["Métricas de latencia, retraso de proyección y errores"]
  QUERY -.-> MONITOR
  PROJCON -.-> MONITOR
  ETL -.-> MONITOR
  REC -.-> MONITOR
```

## Contratos y límites

- La base operativa sigue siendo la fuente de verdad; las proyecciones pueden estar temporalmente atrasadas. El retraso debe medirse y el sistema debe mostrar datos conocidos sin fingir frescura.
- El camino interactivo no ejecuta consultas analíticas pesadas. Las consultas del equipo pasan por autorización, límites y auditoría.
- La caché es opcional y se invalida/actualiza de forma explícita; nunca se comparte una entrada entre usuarios por una clave insuficiente.
- El recomendador usa un contrato versionado y el conjunto mínimo de datos autorizado. Si falla o excede su presupuesto, se conserva el acceso al itinerario.
- Aceptar una sugerencia no altera automáticamente una reserva: la modificación requiere una acción explícita del usuario.
- La evaluación del modelo es asíncrona y versionada; no se implica reentrenamiento inmediato por cada interacción.
