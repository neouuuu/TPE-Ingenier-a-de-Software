# Diagrama de contexto — Trotamundos

```mermaid
flowchart TB
    U["Usuario"]
    T["TROTAMUNDOS<br/>Planificación, organización y compartición de viajes"]
    E["Proveedor de correo"]
    D["Destinatario del itinerario"]
    P["Proveedores turísticos<br/>(aerolíneas, hoteles, transporte, etc.)"]
    M["Servicio de mapas"]
    R["Red social seleccionada"]
    A["Equipo de análisis de datos"]
    AG["Agencia de viajes preferida"]

    U -->|"Gestiona viajes, reservas y preferencias"| T
    T -->|"Itinerarios, recomendaciones y notificaciones"| U
    E -->|"Notificaciones/webhooks si están disponibles"| T
    T -->|"Solicita acceso autorizado a correos"| E
    T -->|"Envía enlace seguro de solo lectura"| D
    D -->|"Solicita visualizar itinerario"| T
    T -->|"Consulta reservas y disponibilidad"| P
    P -->|"Detalles, actualizaciones y cancelaciones"| T
    T -->|"Consulta ubicaciones, rutas y estimaciones"| M
    M -->|"Mapas y datos de rutas"| T
    T -->|"Solicita publicar itinerario elegido"| R
    T -->|"Datos autorizados para análisis"| A
    T <-->|"Integración técnica por API, si está disponible"| AG
```

## Notas sobre el alcance
- El usuario autoriza y puede revocar el acceso al correo (RF-17/RF-18).
- Se prefieren notificaciones/webhooks de correo y proveedores turísticos cuando existan; la consulta periódica queda como alternativa según la API y sus cuotas.
- Los enlaces compartidos son de solo lectura; el destinatario puede no tener cuenta. Caducidad, revocación y verificación del destinatario deben definirse antes del prototipo.
- Las consultas a proveedores no implican que Trotamundos efectúe reservas automáticamente.
- El equipo de análisis solo accede a los datos necesarios para tareas autorizadas; se priorizan datos agregados/desidentificados cuando sean suficientes.
- RF-15 se diseña como integración técnica directa con la agencia preferida. La existencia y capacidad de la API quedan pendientes de validación en la etapa 5; no se asume que exista.
- Las APIs y proveedores concretos siguen pendientes de selección y validación.
