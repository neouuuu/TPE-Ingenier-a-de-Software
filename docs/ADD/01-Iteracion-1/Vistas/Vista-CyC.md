# Vista de componentes y conectores — ADD-1

La vista describe los principales componentes en tiempo de ejecución y los conectores entre ellos. Las flechas etiquetadas distinguen interacción síncrona, eventos internos y llamadas a terceros.

```mermaid
flowchart TB
  subgraph Clients["Clientes"]
    WEB["Cliente web RIA"]
    MOB["Cliente móvil"]
  end

  subgraph Sync["Camino síncrono de interacción"]
    EDGE["Entrada HTTPS / rate limiting"]
    API["API de aplicación"]
    IAM["Identidad y autorización"]
    APP["Servicios de aplicación"]
    DOMAIN["Dominio: viajes y reservas"]
    OPDB[("Base operativa")]
    READ["Servicio de consulta"]
    WEB -->|"HTTPS · request/response"| EDGE
    MOB -->|"HTTPS · request/response"| EDGE
    EDGE --> API
    API --> IAM
    IAM -->|"identidad y permisos"| APP
    APP --> DOMAIN
    DOMAIN -->|"transacción"| OPDB
    APP --> READ
    READ -->|"lectura"| OPDB
  end

  subgraph Async["Camino asíncrono interno"]
    OUTBOX[("Outbox transaccional")]
    RELAY["Publicador de eventos"]
    BUS[["Broker / canal de eventos"]]
    WORKERS["Workers: ingesta, sincronización y notificaciones"]
    DLQ[("DLQ / mensajes fallidos")]
    DOMAIN -->|"mismo commit lógico"| OUTBOX
    OUTBOX --> RELAY
    RELAY -->|"publicación reintentable"| BUS
    BUS -->|"entrega al menos una vez"| WORKERS
    WORKERS -->|"resultado validado"| DOMAIN
    WORKERS -->|"fallos no recuperables"| DLQ
  end

  subgraph Integrations["Puertos y adaptadores externos"]
    PORTS["Puertos de integración"]
    EMAIL["Adaptador de correo"]
    TRAVEL["Adaptadores turísticos"]
    AGENCY["Adaptador de agencia (si hay API)"]
    MAPS["Adaptador de mapas"]
    SOCIAL["Adaptador social"]
    MAILAPI["API de correo"]
    TRAVELAPI["APIs turísticas"]
    AGENCYAPI["API de agencia"]
    MAPAPI["API de mapas"]
    SOCIALAPI["API social"]
    WORKERS --> PORTS
    APP --> PORTS
    PORTS --> EMAIL
    PORTS --> TRAVEL
    PORTS --> AGENCY
    PORTS --> MAPS
    PORTS --> SOCIAL
    EMAIL <-->|"API / webhook si existe"| MAILAPI
    TRAVEL <-->|"API / webhook si existe"| TRAVELAPI
    AGENCY <-->|"API oficial pendiente"| AGENCYAPI
    MAPS <-->|"consulta de rutas"| MAPAPI
    SOCIAL -->|"publicación explícita"| SOCIALAPI
  end

  subgraph ReadModels["Proyecciones y capacidades derivadas"]
    PROJ[("Proyección de lectura")]
    PIPE["Consumidor / pipeline analítico"]
    DW[("Almacén analítico")]
    REC["Servicio de recomendación"]
    BUS -->|"eventos de dominio"| PROJ
    BUS --> PIPE
    PIPE --> DW
    READ -.->|"contexto autorizado"| REC
    REC -->|"sugerencias"| APP
  end

  OBS["Logs, métricas, trazas y alertas"]
  API -.-> OBS
  WORKERS -.-> OBS
  RELAY -.-> OBS
  DLQ -.-> OBS
```

## Semántica de conectores y límites

- **HTTPS request/response:** consultas y comandos interactivos; errores de autorización/validación vuelven por el mismo canal.
- **Transacción + outbox:** el cambio de dominio y el evento pendiente se registran juntos; un publicador independiente reintenta su entrega.
- **Broker:** entrega al menos una vez; consumidores idempotentes evitan efectos duplicados. Los mensajes irrecuperables pasan a DLQ con alerta y reproceso controlado.
- **Integraciones externas:** el adaptador normaliza protocolo, errores, cuotas y credenciales. Webhooks solo se usan si la API los soporta; en caso contrario, un planificador consulta respetando cuotas.
- **Límites de confianza:** tokens y secretos quedan en almacenamiento protegido; los logs no incluyen credenciales ni contenido sensible de correos.
- **Despliegue:** los componentes son límites lógicos. No se impone un microservicio por componente; la topología física queda pendiente de pruebas de carga, costos y capacidad operativa.

La vista define mecanismos propuestos, pero no demuestra los objetivos de latencia, escala ni disponibilidad.
