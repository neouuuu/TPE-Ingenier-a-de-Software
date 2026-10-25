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

    E -->|"Entrega o notifica correos nuevos<br/>(mecanismo por definir)"| T
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

- El acceso al correo requiere autorización del usuario, que puede revocar en cualquier momento (RF-17, RF-18; CU-17).
- La forma de obtener los correos nuevos (consulta periódica de Trotamundos o notificación del proveedor) queda **pendiente de diseño**: los requisitos RF-07 y RF-13 no fijan el mecanismo. Se decidirá durante el ADD.
- Trotamundos notifica al usuario los cambios relevantes en sus reservas (RF-19; CU-18). Los canales concretos quedan pendientes de diseño.
- Los enlaces compartidos deben restringir el acceso a los destinatarios designados. La autorización, caducidad y revocación quedan pendientes de diseño.
- Las consultas a proveedores turísticos no implican que Trotamundos realice reservas automáticamente.
- El equipo de análisis accede a los datos necesarios para sus tareas autorizadas. Se priorizan datos agregados o desidentificados cuando sean suficientes. Es el actor del caso de uso CU-12.
- La agencia no tiene integración técnica directa con Trotamundos: el usuario se comunica con ella por fuera del sistema.
- Las capacidades concretas de los proveedores externos quedan pendientes de selección y validación.