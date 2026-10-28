# ADR-003: Uso de datos de viaje para analítica y mejora del servicio

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Categoría:** Datos y privacidad

## Contexto y problema
Trotamundos necesita analizar tendencias, destinos y cancelaciones. El recomendador también usa historial, preferencias e interacciones. La necesidad analítica no justifica acceso irrestricto a datos personales.

## Drivers
RF-16/RF-20–RF-22; QA-P4 (aislamiento de consultas), QA-SE3 (acceso autorizado); CRN-07/08.

## Alternativas consideradas
1. Utilizar exclusivamente datos agregados/desidentificados.
2. Permitir datos individuales para tareas autorizadas y priorizar agregación/desidentificación cuando sea suficiente.
3. Permitir acceso irrestricto a todos los datos individuales.

## Decisión
Procesar datos de viajes, reservas, preferencias e interacciones para analítica del producto y mejora del servicio. El equipo analítico accede a datos individuales solo cuando sean necesarios para tareas autorizadas. Cuando los datos agregados o desidentificados alcancen, se priorizan. La monetización del producto no implica vender datos personales.

## Consecuencias
**Beneficios:** habilita análisis útiles y evaluación de recomendaciones.

**Costos/riesgos:** se requieren controles de acceso, auditoría, minimización, retención y reglas de consentimiento. La política final debe validarse según regiones y normativa aplicable.

## Trazabilidad
RF-16/RF-20–RF-22; QA-P4/QA-SE3; ADD-4; ADR-014.
