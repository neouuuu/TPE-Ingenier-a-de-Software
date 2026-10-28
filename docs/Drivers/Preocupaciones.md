# Preocupaciones (concerns) — Trotamundos

Una **preocupación** es un tema relevante para los interesados que influye en el diseño aunque todavía no esté expresado como requisito medible. El estado diferencia decisiones adoptadas de cuestiones aún abiertas.

| ID | Preocupación | Origen | Drivers relacionados | Estado |
|---|---|---|---|---|
| CRN-01 | Definir estructura general sin arquitectura heredada. | Análisis inicial | Todos | Supuesto: sistema nuevo. |
| CRN-02 | Extracción heterogénea y deduplicación de reservas que llegan por varias fuentes. | CU-07, RF-08 | RF-07/08, QA-P1, QA-I2 | Abierta; definir identidad de reserva y manejo de datos insuficientes. |
| CRN-03 | Mecanismo de ingesta de correo: notificación/webhook o consulta periódica. | RF-07/RF-13 | QA-P1, QA-S3, QA-I1 | Preferir notificaciones cuando el proveedor las soporte; consulta periódica como alternativa según cuotas/capacidades. |
| CRN-04 | Fuente de verdad y conflictos entre correo, API y edición manual. | RF-02/03/08/13 | RF-01, QA-P1 | Abierta; no asumir que el último dato recibido siempre gana. |
| CRN-05 | Cuotas, permisos, disponibilidad y acceso a APIs reales de correo, turismo y agencia. | Resumen del sistema, RF-11–RF-15 | QA-I1/I2, QA-SE1, CON-T3 | Etapa 5; la integración directa con la agencia depende de una API oficial compatible. |
| CRN-06 | Verificación, caducidad y revocación de enlaces para destinatarios sin cuenta. | ADR-001, RF-23 | QA-SE2 | Abierta; solo lectura decidido. |
| CRN-07 | Permisos analíticos, consentimiento, retención y desidentificación. | ADR-003 | RF-16, QA-SE3 | Parcial; política final pendiente. |
| CRN-08 | Normativa aplicable y residencia de datos por región. | Requisito multirregión | QA-U3, QA-A1, QA-SE2 | Abierta. |
| CRN-09 | Cuándo se completa/archiva un viaje y qué significa eliminar una reserva. | CU-04/CU-06/RF-06 | RF-06 | Abierta. |
| CRN-10 | Datos, feedback, evaluación y ciclo de mejora del recomendador. | ADR-005/006 | RF-20–RF-22, QA-E3 | Abierta; no asumir reentrenamiento por interacción. |
| CRN-11 | Proveedor de mapas, costo, límites y comportamiento ante fallas. | ADR-004 | QA-U1 | Abierta; etapa 5. |
| CRN-12 | Costo de infraestructura al crecer la carga. | Enunciado | QA-S1/S2 | Abierta; dimensionamiento real pendiente. |
| CRN-13 | Observabilidad, recuperación y operación con presupuesto de indisponibilidad estricto. | Enunciado | QA-A1 | Abierta; definir SLI/SLO, alertas, backup y ensayos. |
| CRN-14 | Conectividad limitada durante el viaje. | Experiencia móvil | QA-U1 | Supuesto: soporte offline para itinerario activo; validar alcance. |
| CRN-15 | Corte vertical del prototipo. | Enunciado | CON-06/07 | Abierta. |
| CRN-16 | Tiempo y competencias del equipo para operar tecnologías elegidas. | Cronograma | Todos | Abierta; seleccionar tecnología después de comparar complejidad y costo. |

## Estimaciones de carga: uso correcto

Las estimaciones de sesiones, porcentajes de tráfico pico, solicitudes por sesión, multiplicadores de eventos y buzones conectados que aparezcan en escenarios o análisis son **supuestos del equipo**, no requisitos del enunciado. Deben etiquetarse como tales y utilizarse para diseñar pruebas de carga, no como cifras garantizadas.

La meta explícita de disponibilidad es un máximo de 5 minutos de indisponibilidad no planificada por mes (≈99,988 % en un mes de 30 días). Este cálculo no demuestra que la arquitectura alcance el objetivo; se requieren pruebas de fallos y recuperación.
