# ADD-3 — Disponibilidad, escala, seguridad e interoperabilidad

- **Estado:** propuesta de diseño
- **Objetivo:** refinar integraciones y operación para tolerar fallas, picos, cambios externos y proteger datos sensibles.

## Drivers

QA-A1 (máximo 5 min/mes de indisponibilidad), QA-P1 (actualizaciones en 5 min), QA-S1/S2/S3 (15 M cuentas, 2 M activos semanales y picos), QA-SE1/SE2/SE3, QA-I1/I2; RF-07/RF-11–RF-19/RF-23/RF-24; CON-14/15; CRN-05/06/07/08/12/13.

## Elementos a refinar

Workers, broker, adaptadores externos, persistencia operativa, identidad/compartición y observabilidad: concentran fallas de terceros, credenciales y riesgo de incumplir frescura/disponibilidad.

## Decisiones y tácticas

- Timeouts, reintentos limitados con backoff+jitter, circuit breaker y límites de concurrencia en llamadas externas.
- Idempotencia en consumidores; outbox transaccional o mecanismo equivalente para evitar perder eventos tras confirmar cambios; colas durables, DLQ y reproceso controlado.
- Backpressure y escalado guiado por latencia y retraso de colas.
- OAuth con scopes mínimos, cifrado en tránsito/reposo, secretos fuera del código, rotación y revocación.
- Enlaces compartidos de solo lectura, impredecibles, revocables y con expiración. No incluir datos sensibles en URL/logs. Verificación exacta de destinatario pendiente de cerrar antes del prototipo.
- Acceso por rol/atributos y auditoría para analítica; desidentificar cuando alcance.
- Health checks, métricas, trazas, alertas, backups probados y procedimientos de recuperación.

## Vistas y ADR

- [Vista de resiliencia y seguridad](Vistas/Vista-Resiliencia-Seguridad.md)
- [Flujo de actualización](Vistas/Flujo-Actualizacion.md)
- [ADR-012: resiliencia](ADRs/ADR-012-resiliencia-integraciones.md)
- [ADR-013: seguridad y compartición](ADRs/ADR-013-seguridad-comparticion.md)

## Evaluación

La frescura depende de que la fuente externa publique/exponga el cambio a tiempo. Redundancia no garantiza por sí sola 99,988 % de disponibilidad; hacen falta pruebas de carga, fallas y recuperación. Riesgos abiertos: cuotas reales, RTO/RPO, residencia de datos, costo, y verificación de destinatarios.
