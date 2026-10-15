# Trotamundos: descripción del sistema y requerimientos

## 1. Descripción del sistema

Trotamundos es una plataforma web y móvil que centraliza las reservas de viaje de cada usuario en un único lugar, incluyendo hoteles, automóviles, vuelos, trenes y autobuses.

El sistema debe recopilar información proveniente de servicios externos, permitir la gestión manual de reservas y organizar los viajes durante todo su ciclo de vida.

## 2. Requerimientos funcionales

### A. Usuarios

- Consultar sus viajes y reservas.
- Gestionar manualmente las reservas, permitiendo agregarlas, actualizarlas o eliminarlas.
- Configurar filtros y listas de remitentes de confianza para el procesamiento de correos electrónicos.
- Compartir itinerarios con personas autorizadas.

### B. Reservas

- Examinar correos electrónicos relacionados con viajes.
- Extraer información de los correos y agregar las reservas correspondientes al itinerario.
- Consultar las APIs de proveedores externos.
- Reflejar las actualizaciones y cancelaciones de las reservas.

### C. Viajes

- Agrupar las reservas por viaje.
- Mantener actualizada la información del itinerario.
- Archivar los viajes completados o retirarlos de la vista principal.

### D. Sistema de recomendación

- Analizar el historial de viajes y las preferencias de los usuarios.
- Sugerir alternativas de alojamiento, transporte o rutas.
- Permitir que los usuarios acepten las sugerencias o ajusten los parámetros de recomendación.
- Utilizar las interacciones de los usuarios para refinar las recomendaciones futuras.

### E. Integraciones y servicios complementarios

- Integrarse con proveedores de servicios de viaje y de correo electrónico.
- Facilitar el contacto con la agencia de viajes preferida por el usuario.
- Permitir compartir itinerarios mediante redes sociales.
- Recopilar datos para analizar tendencias, destinos y cancelaciones.

## 3. Atributos de calidad y medidas explícitas

| Atributo | Medida o condición |
|---|---|
| Rendimiento web | Tiempo de respuesta de 800 ms. |
| Rendimiento móvil | First Contentful Paint (FCP) inferior a 1,4 segundos. |
| Frescura de los datos | Mostrar las actualizaciones dentro de los 5 minutos posteriores a su generación por la fuente externa. |
| Disponibilidad | Máximo de 5 minutos de inactividad no planificada por mes. |
| Escalabilidad | Soportar 15 millones de cuentas y 2 millones de usuarios activos semanales, contemplando picos de tráfico. |
| Interoperabilidad | Integración mediante APIs con proveedores de viajes, proveedores de correo electrónico y redes sociales. |
| Seguridad y privacidad | Garantizar el acceso seguro a los correos electrónicos y controlar quién puede visualizar los itinerarios compartidos. |
| Evolucionabilidad | Facilitar la incorporación futura de nuevos medios de transporte, manteniendo la trazabilidad mediante ADR y contratos. |
| Usabilidad e internacionalización | Ofrecer una interfaz enriquecida, capacidades móviles nativas —como GPS— y preparación para operar en múltiples regiones. |

## 4. Cuestiones pendientes de definición

- Determinar qué proveedor de correo electrónico o de reservas se utilizará en el prototipo.
- Identificar qué APIs reales estarán disponibles para la implementación del prototipo.
