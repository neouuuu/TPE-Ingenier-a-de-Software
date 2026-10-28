# ADR-010: Modelo canónico y reconciliación de reservas

- **Estado:** Aceptado para el diseño; precedencia de conflictos pendiente
- **Fecha:** 2026-10-28
- **Iteración:** ADD-2

## Contexto

Una reserva puede llegar por correo, API de proveedor o carga manual. Sin un modelo común y procedencia, pueden aparecer duplicados o sobrescribirse ediciones del usuario.

## Drivers

RF-02/RF-03/RF-08/RF-12/RF-13/RF-14; RN-01–RN-05; QA-P1, QA-I2, QA-E1; CRN-02/04/05.

## Alternativas

- Modelos separados por fuente.
- Modelo canónico con procedencia y reconciliación.
- Sobrescritura universal por la actualización recibida más recientemente.

## Decisión

Normalizar las fuentes a un modelo canónico de reserva. Conservar identificadores externos cuando existan, fuente, fecha de observación y estado de sincronización. Validar cambios antes de persistirlos; no asumir que el último evento tiene prioridad en todos los campos.

## Consecuencias

Facilita consultas y deduplicación; requiere definir identidad de reserva y precedencia por campo. La regla de conflictos debe definirse antes de producción y explicitarse en el prototipo.

## Trazabilidad

ADD-2; ADR-007; RF-02/RF-03/RF-08/RF-12–RF-14.
