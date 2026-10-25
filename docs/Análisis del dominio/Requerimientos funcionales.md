# Requerimientos funcionales

## A. Gestión de viajes y reservas

- **RF-01:** El sistema debe permitir al usuario consultar las reservas organizadas por viaje y visualizar los detalles de cada reserva.
- **RF-02:** El sistema debe permitir al usuario registrar manualmente una reserva y asociarla opcionalmente a un viaje existente.
- **RF-03:** El sistema debe permitir al usuario actualizar manualmente los datos de una reserva existente y, cuando corresponda, modificar su asociación con un viaje.
- **RF-04:** El sistema debe permitir al usuario eliminar manualmente una reserva existente.
- **RF-05:** El sistema debe permitir al usuario organizar las reservas y los elementos del itinerario dentro de un viaje, asignando una reserva a un único viaje como máximo. Las reservas pueden permanecer sin asignar y asociarse posteriormente a un viaje existente o a uno nuevo.
- **RF-06:** El sistema debe archivar o retirar de la vista principal los elementos correspondientes a viajes completados, conservando la información archivada para su consulta cuando corresponda.

## B. Procesamiento de correo electrónico

- **RF-07:** El sistema debe obtener los correos electrónicos de las cuentas que el usuario haya autorizado mediante notificaciones del proveedor de correo y procesarlos para identificar aquellos relacionados con viajes y que puedan contener información sobre reservas.
- **RF-08:** El sistema debe identificar y registrar automáticamente las reservas reconocidas en los correos electrónicos procesados, sin requerir que estén previamente asociadas a un viaje. Las reservas que no puedan asociarse de forma válida deben permanecer sin asignar hasta que el usuario las organice.
- **RF-09:** El sistema debe permitir al usuario configurar filtros para determinar qué correos electrónicos relacionados con viajes deben procesarse.
- **RF-10:** El sistema debe permitir al usuario gestionar listas de remitentes seguros (*whitelists*) utilizadas durante el procesamiento de correos electrónicos relacionados con viajes.

## C. Integración con proveedores turísticos

- **RF-11:** El sistema debe integrarse con sistemas de viajes y proveedores externos mediante APIs estándar, de acuerdo con las interfaces que estos ofrezcan.
- **RF-12:** El sistema debe obtener detalles de las reservas desde los proveedores externos compatibles.
- **RF-13:** El sistema debe obtener actualizaciones sobre las reservas desde los proveedores externos compatibles mediante las notificaciones que el proveedor ofrezca y reflejar los cambios en la información almacenada.
- **RF-14:** El sistema debe obtener información sobre cancelaciones de reservas desde los proveedores externos compatibles y actualizar el estado de las reservas correspondientes.

## D. Resolución de problemas de viaje

- **RF-15:** El sistema debe integrarse con la agencia de viajes preferida por el usuario, cuando exista una integración compatible, para facilitar la resolución de problemas relacionados con sus viajes.

## E. Analítica de datos

- **RF-16:** El sistema debe recopilar datos de viajes, incluyendo tendencias, destinos y cancelaciones, y permitir al equipo de análisis de datos ejecutar consultas analíticas sobre ellos, incluidas consultas pesadas, para generar información sobre los viajes registrados.

## F. Acceso al correo y notificaciones

- **RF-17:** El sistema debe permitir al usuario autorizar el acceso a su cuenta de correo electrónico para que el sistema pueda procesar sus correos. Sin autorización expresa del usuario, el sistema no debe acceder a su correo.
- **RF-18:** El sistema debe permitir al usuario consultar las cuentas de correo que ha conectado y revocar el acceso en cualquier momento. Una vez revocado el acceso, el sistema no debe volver a acceder a los correos de esa cuenta.
- **RF-19:** El sistema debe notificar al usuario los cambios relevantes en sus reservas (por ejemplo, actualizaciones y cancelaciones) una vez reflejados en el itinerario. Los canales de notificación y los cambios que se consideran relevantes se definirán en el diseño.

## G. Sistema de recomendación

- **RF-20:** El sistema debe analizar el historial de viajes del usuario y sus preferencias para generar recomendaciones personalizadas.
- **RF-21:** El sistema debe generar sugerencias de alternativas de viaje, incluyendo opciones de alojamiento, transporte y rutas, considerando la información disponible y las preferencias del usuario.
- **RF-22:** El sistema debe permitir al usuario aceptar las sugerencias de viaje o modificar los parámetros de recomendación para orientar los resultados, y debe utilizar las interacciones del usuario con las sugerencias para refinar progresivamente el modelo de recomendación.

## H. Compartición de itinerarios

- **RF-23:** El sistema debe permitir al usuario compartir un itinerario con destinatarios específicos mediante un enlace seguro enviado por correo electrónico.
- **RF-24:** El sistema debe permitir al usuario publicar un itinerario en una red social seleccionada por él, mediante una integración compatible.

---

## Historial de cambios en la numeración

| Antes | Ahora | Motivo |
|---|---|---|
| (sin número) | **RF-17**, **RF-18** | Nuevos: autorizar y revocar el acceso al correo. Aparecían en el diagrama de contexto, pero no tenían requisito |
| (sin número) | **RF-19** | Nuevo: notificaciones al usuario. Aparecían en el diagrama de contexto, pero no tenían requisito |
| RF-27 | **RF-23** | Se eliminaron los huecos de numeración |
| RF-28 | **RF-24** | Se eliminaron los huecos de numeración |
| RF-07, RF-13, RF-16 | Mismo número, texto ajustado | RF-07 y RF-13 ya no fijan el mecanismo de obtención (consulta o notificación). RF-16 aclara que el actor es el equipo de análisis |

Los números RF-01 a RF-06, RF-08 a RF-12, RF-14, RF-15 y RF-20 a RF-22 no cambian.
