# Requerimientos funcionales

## A. Gestión de viajes y reservas

- **RF-01:** El sistema debe permitir al usuario consultar las reservas organizadas por viaje y visualizar los detalles de cada reserva.
- **RF-02:** El sistema debe permitir al usuario registrar manualmente una reserva y asociarla opcionalmente a un viaje existente.
- **RF-03:** El sistema debe permitir al usuario actualizar manualmente los datos de una reserva existente y, cuando corresponda, modificar su asociación con un viaje.
- **RF-04:** El sistema debe permitir al usuario eliminar manualmente una reserva existente.
- **RF-05:** El sistema debe permitir al usuario organizar las reservas y los elementos del itinerario dentro de un viaje, asignando una reserva a un único viaje como máximo. Las reservas pueden permanecer sin asignar y asociarse posteriormente a un viaje existente o a uno nuevo.
- **RF-06:** El sistema debe archivar o retirar de la vista principal los elementos correspondientes a viajes completados, conservando la información archivada para su consulta cuando corresponda.

## B. Procesamiento de correo electrónico

- **RF-07:** El sistema debe buscar y procesar correos electrónicos para identificar aquellos relacionados con viajes y que puedan contener información sobre reservas.
- **RF-08:** El sistema debe identificar y registrar automáticamente las reservas reconocidas en los correos electrónicos procesados, sin requerir que estén previamente asociadas a un viaje. Las reservas que no puedan asociarse de forma válida deben permanecer sin asignar hasta que el usuario las organice.
- **RF-09:** El sistema debe permitir al usuario configurar filtros para determinar qué correos electrónicos relacionados con viajes deben procesarse.
- **RF-10:** El sistema debe permitir al usuario gestionar listas de remitentes seguros (*whitelists*) utilizadas durante el procesamiento de correos electrónicos relacionados con viajes.

## C. Integración con proveedores turísticos

- **RF-11:** El sistema debe integrarse con sistemas de viajes y proveedores externos mediante APIs estándar, de acuerdo con las interfaces que estos ofrezcan.
- **RF-12:** El sistema debe obtener detalles de las reservas desde los proveedores externos compatibles.
- **RF-13:** El sistema debe obtener actualizaciones sobre las reservas desde los proveedores externos compatibles y reflejar los cambios en la información almacenada.
- **RF-14:** El sistema debe obtener información sobre cancelaciones de reservas desde los proveedores externos compatibles y actualizar el estado de las reservas correspondientes.

## D. Resolución de problemas de viaje

- **RF-15:** El sistema debe integrarse con la agencia de viajes preferida por el usuario, cuando exista una integración compatible, para facilitar la resolución de problemas relacionados con sus viajes.

## E. Analítica de datos

- **RF-16:** El sistema debe recopilar y permitir analizar datos de viajes, incluyendo tendencias, destinos y cancelaciones, para generar información analítica sobre los viajes registrados.

## F. Sistema de recomendación

- **RF-20:** El sistema debe analizar el historial de viajes del usuario y sus preferencias para generar recomendaciones personalizadas.
- **RF-21:** El sistema debe generar sugerencias de alternativas de viaje, incluyendo opciones de alojamiento, transporte y rutas, considerando la información disponible y las preferencias del usuario.
- **RF-22:** El sistema debe permitir al usuario aceptar las sugerencias de viaje o modificar los parámetros de recomendación para orientar los resultados, y debe utilizar las interacciones del usuario con las sugerencias para refinar progresivamente el modelo de recomendación.

## G. Compartición de itinerarios

- **RF-27:** El sistema debe permitir al usuario compartir un itinerario con destinatarios específicos mediante un enlace seguro enviado por correo electrónico.
- **RF-28:** El sistema debe permitir al usuario publicar un itinerario en una red social seleccionada por él, mediante una integración compatible.

