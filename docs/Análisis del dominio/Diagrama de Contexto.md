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

    E -->|"Notifica nuevos correos o eventos relevantes"| T
    T -->|"Solicita acceso autorizado a correos"| E

    T -->|"Envía enlace seguro al itinerario"| D
    D -->|"Solicita acceso al itinerario"| T

    T -->|"Consulta reservas y disponibilidad"| P
    P -->|"Información de reservas, actualizaciones y cancelaciones"| T

    T -->|"Consulta ubicaciones, rutas y estimaciones"| M
    M -->|"Información geográfica y estimaciones de distancia y duración"| T

    T -->|"Solicita publicar el itinerario elegido"| R

    T -->|"Datos de viajes, reservas, preferencias e interacciones para análisis y mejora"| A

    T -.->|"Facilita datos de contacto de la agencia al usuario"| U
    U -.->|"Se comunica externamente para solicitar asistencia"| AG
```

## Notas sobre el alcance

- El acceso al correo requiere autorización del usuario.
- Los enlaces compartidos deben restringir el acceso a los destinatarios designados. La autorización, caducidad y revocación quedan pendientes de diseño.
- Las consultas a proveedores turísticos no implican que Trotamundos realice reservas automáticamente.
- El equipo de análisis accede a los datos necesarios para sus tareas autorizadas. Se priorizan datos agregados o desidentificados cuando sean suficientes.
- La agencia no tiene integración técnica directa con Trotamundos: el usuario se comunica con ella por fuera del sistema.
- Las capacidades concretas de los proveedores externos quedan pendientes de selección y validación.