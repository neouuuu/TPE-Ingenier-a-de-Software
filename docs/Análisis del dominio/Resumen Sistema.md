# Trotamundos: descripción del sistema y requerimientos

## 1. Descripción

Trotamundos es una plataforma web y móvil que centraliza las reservas de viaje de cada usuario (hoteles, automóviles, vuelos, trenes y autobuses), permite registrar reservas manualmente, las organiza en viajes y refleja actualizaciones de fuentes externas.

## 2. Capacidades funcionales

- **Viajes y reservas:** consultar, registrar, actualizar, eliminar y asignar reservas; una reserva pertenece a cero o un viaje y puede quedar sin asignar.
- **Correo:** acceder solo con autorización expresa; aplicar filtros y remitentes confiables; detectar correos de viaje y extraer reservas.
- **Proveedores turísticos:** consultar detalles, actualizaciones y cancelaciones mediante APIs compatibles.
- **Agencia preferida:** RF-15 requiere diseñar integración técnica directa mediante API cuando exista una interfaz oficial compatible. API y viabilidad pendientes de la etapa 5; no se asume que exista.
- **Notificaciones:** informar al usuario cambios relevantes después de reflejarlos en el itinerario.
- **Compartición:** enlace seguro por correo a destinatarios específicos, que pueden no tener cuenta; solo lectura. También se contempla publicar en una red social elegida.
- **Analítica:** permitir al equipo autorizado analizar tendencias, destinos y cancelaciones, incluyendo consultas pesadas.
- **Recomendaciones:** usar historial y preferencias para sugerir alojamiento, transporte y rutas; permitir aceptar o ajustar sugerencias y usar las interacciones para evaluar mejoras.
- **Mapas:** integrar un servicio externo para ubicaciones y rutas; el proveedor está pendiente.

## 3. Atributos de calidad y metas del enunciado

| Atributo | Meta/condición |
|---|---|
| Rendimiento web | Respuesta objetivo de 800 ms. |
| Rendimiento móvil | First Contentful Paint (FCP) menor a 1,4 s. |
| Frescura | Mostrar cambios dentro de los 5 minutos posteriores a su generación por la fuente externa, cuando esta los exponga oportunamente. |
| Disponibilidad | Máximo de 5 minutos de indisponibilidad no planificada por mes. |
| Escala | 15 millones de cuentas y 2 millones de usuarios activos semanales; contemplar picos. |
| Interoperabilidad | APIs estándar de correo, proveedores turísticos, agencia si está disponible y redes sociales. |
| Seguridad/privacidad | Acceso autorizado y revocable al correo; control de acceso a itinerarios y datos analíticos. |
| Evolución | Incorporar transportes/proveedores nuevos con contratos y trazabilidad mediante ADR. |
| UX/globalización | Interfaz enriquecida, capacidades móviles como GPS e infraestructura preparada para múltiples regiones. |

## 4. Pendientes relevantes para el diseño

- Seleccionar APIs concretas para correo, proveedores turísticos, agencia, mapas y redes sociales.
- Validar cuotas, permisos, verificación de aplicación, costos y términos de uso.
- Definir política de deduplicación y precedencia cuando una edición manual compite con un cambio externo.
- Definir caducidad/revocación y verificación del destinatario de enlaces compartidos.
- Definir canales de notificación, residencia regional de datos y alcance vertical del prototipo.

## 5. Decisiones de diseño que no deben confundirse con requisitos

Se prefieren webhooks/notificaciones externas cuando el proveedor los ofrece; la consulta periódica es alternativa cuando no existe un mecanismo adecuado. El procesamiento por eventos dentro de Trotamundos no implica que todos los proveedores externos sean capaces de publicar eventos. La arquitectura lógica no obliga a desplegar cada módulo como microservicio.
