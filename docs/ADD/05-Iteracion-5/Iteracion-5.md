# ADD-5 — Refinamiento de implementación y validación integrada del sistema

- **Estado:** propuesta de diseño para el prototipo.
- **Objetivo:** refinar el sistema completo hasta un nivel implementable, concretando tecnologías y técnicas para comprobar el flujo principal de Trotamundos de extremo a extremo.
- **Alcance:** prototipo local ejecutado con Docker Compose. Esta iteración no reemplaza ADD-1 a ADD-4 ni implica que el stack seleccionado sea automáticamente el de producción.

## Propósito y criterio de diseño

Esta iteración refina la arquitectura de Trotamundos como sistema completo y, para validarla sin implementar todas las funcionalidades, define un prototipo vertical representativo. El prototipo debe aportar evidencia de que las decisiones arquitectónicas centrales pueden colaborar en un flujo realista: un proveedor turístico informa una reserva de hotel nueva, modificada o cancelada; Trotamundos valida y procesa la notificación; el cambio se propaga de forma asíncrona; y una consulta devuelve el estado actualizado.

No se busca implementar todas las funcionalidades del producto ni demostrar capacidad de producción. Se prioriza un flujo integrado y pruebas de comportamiento ante duplicados y fallos.

## Drivers

- **RF-11–RF-15:** integración con proveedores turísticos y agencia, detrás de adaptadores.
- **RF-01/RF-05 y reglas de negocio de reservas:** persistencia y consulta de reservas asociadas a viajes.
- **QA-P1:** propagación de cambios de fuentes externas; en el prototipo se valida el flujo, sin convertir la prueba en un estudio de métricas de rendimiento.
- **QA-SE1/QA-SE2:** autenticidad de la notificación y protección de los datos.
- **QA-A1:** recuperación ante fallos como comportamiento a comprobar; el prototipo local no demuestra por sí solo la disponibilidad mensual objetivo.
- **CRN-05/06/07/08/12/13:** integraciones desacopladas, eventos durables, idempotencia, resiliencia y seguridad.
- Decisiones de implementación acordadas durante el diseño del prototipo.

## Elementos a refinar

1. Endpoint HTTP que recibe webhooks externos.
2. Adaptador y contrato del proveedor simulado de hoteles.
3. Modelo de escritura de reservas y persistencia de eventos entrantes.
4. Transactional Outbox y proceso publicador.
5. RabbitMQ y sus colas de eventos.
6. Consumidor con Inbox transaccional y proyección de lectura CQRS.
7. API de consulta del itinerario.
8. Política de reintentos, DLQ y reprocesamiento controlado.
9. Configuración local reproducible y pruebas automatizadas.

## Mapa de refinamiento del sistema completo

ADD-5 no redefine los límites funcionales de ADD-1 a ADD-4: los concreta hasta el nivel de implementación cuando ya existe una decisión y deja explícito qué permanece sin seleccionar.

| Subsistema del sistema objetivo | Concreción en ADD-5 | Límite del prototipo |
|---|---|---|
| Clientes web y móvil | Consumen APIs mediante contratos HTTP; se mantiene la separación cliente/backend. | No se selecciona framework frontend porque no es necesario para validar el flujo de eventos. La consulta puede probarse por HTTP. |
| API y dominio | Python + FastAPI para el prototipo, con módulos internos para reservas y consultas. | Los módulos lógicos no se convierten automáticamente en microservicios independientes. |
| Identidad de usuarios | Se conserva como responsabilidad arquitectónica separada, según ADD-1/ADD-3. | No se elige proveedor de identidad ni se pretende validar todo el inicio de sesión. HMAC autentica al emisor del webhook, no a los usuarios finales. |
| Reservas y persistencia | PostgreSQL, modelo de escritura y proyección de lectura en tablas separadas. | Un solo motor en el prototipo; la topología productiva queda abierta. |
| Comunicación interna | RabbitMQ, Transactional Outbox, Inbox, reintentos limitados y DLQ. | Se implementa el flujo de actualización de reserva de hotel como corte vertical de validación. |
| Integraciones externas | Puertos/adaptadores desacoplados y contratos propios versionados. | Se usa un simulador independiente de proveedor de hoteles. Correo, agencia, mapas, redes sociales y canales de notificación siguen sujetos a la etapa previa de validación de APIs. |
| Analítica y recomendaciones | Se mantienen como subsistemas lógicos desacoplados definidos en ADD-4. | No se seleccionan motor analítico, algoritmo ni framework de recomendación en este prototipo; no son necesarios para validar el flujo central. |
| Despliegue y validación | Docker Compose local, Pytest y exploración HTTP manual. | No se considera una topología de producción ni una prueba de escala o multirregión. |

## Decisiones de implementación para el prototipo

| Área | Decisión | Motivo |
|---|---|---|
| Lenguaje/API | Python + FastAPI | Permite implementar endpoints HTTP y separar procesos de aplicación con bajo costo inicial. |
| Persistencia | PostgreSQL | Transacciones y restricciones únicas para reservas, recibos de webhooks, Outbox, Inbox y proyección de lectura. |
| Mensajería | RabbitMQ | Permite probar colas durables, confirmación de publicación, consumidores, reintentos y DLQ. |
| CQRS | Modelo de escritura y proyección de lectura en tablas separadas dentro del mismo PostgreSQL | Valida la propagación asíncrona sin agregar un segundo motor de base de datos. |
| Publicación fiable | Transactional Outbox | El cambio del modelo de escritura y el evento interno se registran en una misma transacción. |
| Duplicados internos | ID de evento y Inbox transaccional | La inserción del ID procesado y la actualización de la proyección se confirman juntas. |
| Duplicados externos | ID estable del evento del proveedor con restricción única | Un reintento del webhook no debe repetir los efectos de negocio ni crear eventos internos duplicados. |
| Seguridad del webhook | HMAC-SHA256 con secreto compartido | Verifica autenticidad e integridad del cuerpo antes de procesarlo. La implementación firmará marca temporal + cuerpo original y aplicará una ventana temporal. |
| Fallos de consumidor | Reintentos limitados con espera progresiva y DLQ | Evita ciclos de reintentos ilimitados y permite inspección/reproceso explícito. |
| Entorno | Docker Compose local | Hace reproducibles los servicios y permite detener y reiniciar procesos de manera controlada. |
| Pruebas | Pytest para automatización y solicitudes HTTP manuales para exploración | Permite verificar comportamientos y depurar el flujo durante el desarrollo. |
| Proveedor | Simulador independiente de proveedor de hoteles | Controla altas, modificaciones, cancelaciones, duplicados, firmas inválidas y errores sin depender de credenciales comerciales. |

Estas decisiones concretan el **prototipo**, no una obligación de desplegar cada módulo como microservicio en producción. El API, el relay del Outbox y el consumidor pueden compartir código fuente, pero se ejecutarán como procesos diferenciados en Compose cuando sea necesario provocar fallos de manera independiente.

## Flujo integrado que se implementará

1. El simulador envía un webhook de alta, modificación o cancelación de una reserva de hotel.
2. FastAPI valida el contrato, la marca temporal y la firma HMAC sobre el cuerpo original.
3. En una transacción PostgreSQL, Trotamundos registra el ID externo con unicidad, aplica el cambio al modelo de escritura y agrega el evento interno al Outbox.
4. El relay publica el evento en RabbitMQ y lo marca publicado después de recibir confirmación del broker. Si se cae entre la publicación y el marcado, puede volver a publicarlo; el consumidor debe tolerar esa entrega repetida.
5. El consumidor registra el ID del evento en Inbox y actualiza la proyección de lectura en una sola transacción.
6. El consumidor confirma el mensaje a RabbitMQ después del commit. Los fallos transitorios siguen la política de reintentos; los persistentes llegan a la DLQ.
7. La API de consulta devuelve el estado de la reserva desde la proyección de lectura, que puede actualizarse después de la confirmación inicial del webhook.

## Contratos mínimos

- Cada webhook contiene un ID de evento estable, tipo de evento, ID de reserva, fecha de emisión y datos de la reserva.
- Tipos mínimos: `reservation.created`, `reservation.updated` y `reservation.cancelled`.
- Los eventos internos tienen `event_id`, tipo, versión de esquema, ID de reserva, fecha de ocurrencia y datos necesarios para actualizar la proyección.
- El contrato HTTP propio se documentará con OpenAPI; el esquema de eventos se versionará.
- La autenticación HMAC y la deduplicación son controles separados: una firma válida no implica que el evento sea nuevo ni que el proveedor esté autorizado para cualquier reserva.
- No se registran secretos ni cuerpos completos con datos sensibles en logs.

## Vistas y ADR

- [Vista C&C del prototipo integrado](Vistas/Vista-CyC-Prototipo.md)
- [ADR-016: Stack y técnicas del prototipo](ADRs/ADR-016-stack-y-tecnicas-prototipo.md)

## Plan de pruebas de comportamiento

- Webhook válido: alta, modificación y cancelación se reflejan finalmente en la consulta.
- Firma inválida o marca temporal fuera de ventana: rechazo sin cambios de negocio.
- Webhook externo repetido: no duplica el efecto ni publica una segunda operación lógica.
- Evento interno repetido: Inbox impide aplicar dos veces el mismo evento a la proyección.
- API detenida o indisponible: el simulador observa el fallo de entrega y puede reintentar.
- Consumidor detenido: los mensajes permanecen en RabbitMQ y se procesan al recuperarlo.
- Error persistente del consumidor: el mensaje llega a DLQ y puede inspeccionarse y reprocesarse de forma controlada.
- Fallo del relay tras publicar pero antes de marcar el Outbox: se permite una republicación y se verifica la deduplicación del consumidor.

No se incorpora como requisito de esta iteración un tablero de métricas o un informe de rendimiento: el foco acordado es validar el comportamiento arquitectónico del flujo y sus mecanismos de recuperación.

## Límites y asuntos abiertos

- El prototipo usa un proveedor simulado; no demuestra que Booking.com u otro proveedor real permita las mismas operaciones o webhooks.
- La estrategia para eventos distintos de una misma reserva que lleguen fuera de orden sigue siendo una decisión pendiente. No se debe asumir una regla de “último evento recibido gana” sin definir versión o precedencia de fuentes.
- Se validará el rechazo de firmas inválidas, pero la gestión completa de rotación de secretos, múltiples proveedores y distribución de secretos queda fuera del alcance inicial.
- La DLQ necesita una política operativa de inspección y reproceso; no se debe reenviar en bucle automáticamente.
- CQRS introduce consistencia eventual: el webhook puede confirmarse antes de que la proyección muestre el cambio.
- No se afirma que el prototipo demuestre los objetivos de escala, disponibilidad mensual o despliegue multirregión de producción.

## Criterio de salida

La iteración se considera implementada cuando el flujo de alta/modificación/cancelación se ejecuta de extremo a extremo en Compose y las pruebas verifican autenticación, deduplicación, Outbox, propagación a la proyección y recuperación de mensajes fallidos. Los resultados deben registrar qué se comprobó, qué no se comprobó y qué decisiones deben revisarse antes de producción.
