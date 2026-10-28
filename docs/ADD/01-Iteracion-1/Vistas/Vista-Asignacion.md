# Vista de asignación inicial — ADD-1

```mermaid
flowchart TB
  subgraph Devices[Dispositivos]
    WEB[Navegador]
    MOBILE[Aplicación móvil]
  end
  subgraph Platform[Plataforma lógica]
    EDGE[Entrada HTTPS / balanceador]
    API[API]
    WORKERS[Workers]
    BROKER[Broker / eventos]
    DB[(Base operativa)]
    DW[(Almacén analítico)]
    OBS[Logs, métricas, trazas y alertas]
  end
  subgraph External[Sistemas externos]
    MAIL[Correo]
    TRAVEL[Proveedores turísticos]
    AGENCY[Agencia preferida]
    MAPS[Mapas]
    SOCIAL[Red social]
  end
  WEB --> EDGE
  MOBILE --> EDGE
  EDGE --> API
  API --> DB
  API --> BROKER
  BROKER --> WORKERS
  WORKERS --> DB
  WORKERS --> MAIL
  WORKERS --> TRAVEL
  WORKERS --> AGENCY
  API --> MAPS
  API --> SOCIAL
  DB --> DW
  API --> OBS
  WORKERS --> OBS
```

No se fija proveedor cloud, número de regiones, topología, motor de base de datos ni broker. La vista no demuestra el objetivo de disponibilidad: hacen falta pruebas de carga, fallo y recuperación.
