# Vista de módulos — ADD-1

Las cajas son módulos lógicos, no necesariamente servicios desplegables independientes.

```mermaid
flowchart TB
  WEB[Cliente web RIA] --> API[API de aplicación]
  MOB[Cliente móvil] --> API
  API --> IAM[Identidad y autorización]
  API --> DOM[Dominio: viajes y reservas]
  API --> SHARE[Compartición y notificaciones]
  API --> REC[Recomendaciones]
  JOBS[Procesamiento asíncrono] --> DOM
  JOBS --> PORTS[Puertos de integración]
  PORTS --> ADAPTERS[Adaptadores externos]
  ADAPTERS --> EMAIL[Correo]
  ADAPTERS --> TRAVEL[Proveedores turísticos]
  ADAPTERS --> AGENCY[Agencia preferida]
  ADAPTERS --> MAPS[Mapas y rutas]
  ADAPTERS --> SOCIAL[Red social]
  DOM --> OPDB[(Persistencia operativa)]
  JOBS --> EVENTS[(Eventos internos)]
  EVENTS --> ANALYTICS[Proyección analítica]
  ANALYTICS --> ADB[(Almacén analítico)]
  ADB --> TEAM[Equipo de análisis]
  REC --> ADB
```

El dominio no depende de SDKs externos. Analítica y recomendación acceden solo a los datos autorizados que necesitan. El despliegue físico se decidirá con evidencia de costo, escala y operación.
