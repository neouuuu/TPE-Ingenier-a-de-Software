# ADR-016: Stack y técnicas concretas para el prototipo de viabilidad

- **Estado:** aceptado para el prototipo; no constituye una decisión definitiva de producción.
- **Fecha:** 2026-10-28
- **Iteración:** ADD-5

## Contexto

Las iteraciones ADD-1 a ADD-4 definen la arquitectura lógica de Trotamundos. ADD-5 refina el sistema completo hasta un nivel implementable, seleccionando tecnologías para un prototipo integrado y explicitando los subsistemas cuya tecnología concreta queda abierta. Hace falta comprobar las decisiones principales mediante un flujo ejecutable. Se necesita un prototipo local que reciba actualizaciones externas, las procese asíncronamente y las refleje en una consulta, con fallos reproducibles.

## Drivers

RF-11–RF-15; RF-01/RF-05; QA-P1; QA-SE1/QA-SE2; QA-A1; CRN-05/06/07/08/12/13.

## Alternativas consideradas

- Construir toda la aplicación y sus clientes antes de validar los flujos internos.
- Usar una cola simulada y almacenamiento en memoria para reducir trabajo.
- Implementar un flujo integrado acotado con tecnologías concretas y servicios reproducibles localmente.

## Alcance del sistema y del prototipo

La iteración refina el sistema completo, pero el prototipo ejecutable se limita a un flujo vertical de reservas para probar la arquitectura de eventos. Las decisiones siguientes son concretas para ese prototipo; no fuerzan tecnologías no elegidas para clientes web/móvil, proveedor de identidad, analítica o recomendación.

- Los clientes web/móvil continúan separados del backend y consumen contratos HTTP; el framework de frontend queda sin seleccionar.
- La identidad de usuarios continúa siendo una responsabilidad separada. HMAC autentica webhooks de proveedor y no reemplaza la autenticación/autorización de usuarios.
- Los módulos de dominio definidos en ADD-1/ADD-2 se conservan como límites lógicos; no se exige desplegar cada uno como microservicio.
- Las integraciones de correo, agencia, mapas, redes sociales y notificaciones continúan detrás de adaptadores y sujetas a validación externa. El prototipo usa únicamente el simulador de hoteles.
- Analítica y recomendación conservan su separación lógica de ADD-4; sus motores concretos quedan fuera de este prototipo.

## Decisión

Para el prototipo se adopta:

- Python + FastAPI para endpoints de webhook y consulta.
- PostgreSQL como único motor, con tablas separadas para el modelo de escritura, recibos de webhooks externos, Outbox, Inbox y proyección de lectura.
- RabbitMQ para eventos internos, con colas durables y confirmación de publicación.
- Transactional Outbox para registrar el cambio de dominio y el evento interno en una sola transacción.
- Inbox transaccional e ID único por evento para evitar repetir los efectos sobre la proyección.
- HMAC-SHA256 con secreto compartido para autenticar los webhooks; la firma cubre marca temporal y cuerpo original.
- Reintentos limitados con espera progresiva y Dead Letter Queue para fallos persistentes.
- Simulador independiente de proveedor de hoteles para generar altas, modificaciones, cancelaciones, duplicados y fallos.
- Docker Compose para ejecutar y aislar los procesos localmente.
- Pytest para pruebas automatizadas, complementado con exploración manual por HTTP.

## Consecuencias positivas

- El flujo principal se puede ejecutar de extremo a extremo sin credenciales comerciales.
- Se pueden provocar fallos en el relay y el consumidor sin depender de un proveedor externo.
- Las transacciones y restricciones de unicidad permiten probar los límites entre persistencia y mensajería.
- El entorno puede reproducirse y documentarse como parte del trabajo práctico.

## Costos y limitaciones

- Outbox, Inbox, DLQ y consistencia eventual agregan complejidad que debe explicarse y probarse.
- RabbitMQ y PostgreSQL necesitan configuración y mantenimiento incluso en el entorno local.
- La firma HMAC requiere proteger y gestionar el secreto; no reemplaza la autorización de negocio ni la deduplicación.
- El prototipo no prueba la integración real con Booking.com ni con otros proveedores.
- No demuestra los objetivos de escala, disponibilidad mensual, multirregión ni rendimiento de producción.
- El stack puede cambiar si la evidencia de las pruebas o las restricciones del despliegue lo justifican.

## Trazabilidad

ADD-1 a ADD-4; ADD-5; vistas C&C del sistema y del prototipo; RF-01/RF-05/RF-11–RF-15; QA-P1, QA-SE1/SE2 y QA-A1.
