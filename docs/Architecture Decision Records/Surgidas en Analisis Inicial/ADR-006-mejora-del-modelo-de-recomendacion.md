# ADR-006: Registrar interacciones para evaluar y mejorar recomendaciones

- **Estado:** Propuesto
- **Fecha:** 2026-10-28
- **Categoría:** Evolución del recomendador

## Contexto y problema
El módulo de recomendación debe permitir que el usuario acepte sugerencias o ajuste parámetros. Estas interacciones pueden indicar utilidad, pero no justifican reentrenar automáticamente el modelo después de cada acción.

## Drivers
RF-22; QA-E3; QA-SE3; CRN-10; ADR-005.

## Alternativas consideradas
1. No registrar interacciones.
2. Registrar interacciones relevantes para evaluación y mejora periódica.
3. Actualizar/reentrenar el modelo después de cada interacción.

## Decisión propuesta
Registrar eventos relevantes —por ejemplo, aceptación o ajuste de parámetros— con minimización de datos y controles de acceso. Utilizarlos para evaluar y mejorar recomendaciones mediante una estrategia que se definirá en el diseño. Esto **no** implica reentrenamiento inmediato después de cada interacción.

## Consecuencias
**Beneficios:** habilita evaluación continua y conserva flexibilidad sobre el método de mejora.

**Costos/riesgos:** deben definirse eventos, retención, consentimiento, controles de acceso, evaluación y prevención de señales engañosas. El estado permanece *Propuesto* hasta que el equipo confirme la política de datos y el ciclo de mejora.

## Trazabilidad
RF-20–RF-22; ADR-003/005; ADD-4; ADR-015.
