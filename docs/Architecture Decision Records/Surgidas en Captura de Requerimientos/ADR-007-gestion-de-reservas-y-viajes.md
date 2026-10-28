# ADR-007: Separar el registro de reservas de su asignación a viajes

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Categoría:** Dominio y reglas funcionales

## Contexto y problema
Una reserva puede registrarse manualmente o importarse desde correo antes de que exista el viaje correspondiente o antes de que pueda determinarse a qué viaje pertenece. Exigir una asignación inmediata o automática puede impedir el registro o crear asociaciones incorrectas.

## Drivers
RF-01/RF-02/RF-03/RF-05/RF-08; RN-01–RN-05; calidad y trazabilidad del modelo de dominio.

## Alternativas consideradas
1. Exigir asignación a un viaje al registrar.
2. Asignar automáticamente todas las reservas importadas.
3. Permitir reservas sin asignar y asociación opcional a un único viaje.
4. Permitir que una reserva pertenezca a varios viajes.

## Decisión
1. Una reserva se asocia a **cero o un viaje** como máximo.
2. Un viaje puede contener múltiples reservas.
3. El registro manual permite asociar un viaje opcionalmente.
4. La importación puede crear una reserva sin asignar; no se asigna automáticamente salvo que la información disponible justifique la asociación.
5. Las reservas sin asignar se pueden consultar y organizar posteriormente.
6. Registrar y organizar son responsabilidades separadas, aunque la interfaz permita hacerlas en un mismo paso.

## Consecuencias
**Beneficios:** admite importación temprana, evita asociaciones ambiguas y permite organizar progresivamente.

**Costos/riesgos:** se necesita una vista de reservas sin asignar, validación transaccional de asociación única y reglas de deduplicación. La información insuficiente no debe generar una asociación inventada.

## Trazabilidad
RF-01/RF-02/RF-03/RF-05/RF-08; RN-01–RN-05; ADD-2; ADR-010/011.
