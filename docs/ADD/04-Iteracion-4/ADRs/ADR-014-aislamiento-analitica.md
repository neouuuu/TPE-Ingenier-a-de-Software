# ADR-014: Separar cargas analíticas de transacciones operativas

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Iteración:** ADD-4

## Contexto

El equipo de análisis necesita consultas pesadas sobre tendencias, destinos y cancelaciones. Ejecutarlas sobre la misma base operativa puede degradar el uso interactivo.

## Drivers

RF-16; QA-P2, QA-S1/S2, QA-SE3; CRN-07/08/12/13.

## Alternativas

- Consultar la base operativa directamente.
- Limitar consultas en esa base.
- Alimentar un almacén/proyección analítica por pipeline.

## Decisión

Separar el procesamiento analítico del transaccional. Alimentar una proyección/almacén mediante eventos o pipeline controlado; priorizar datos agregados o desidentificados cuando alcancen y restringir el acceso individual.

## Consecuencias

Protege el camino operativo, pero introduce consistencia eventual y costos de almacenamiento/gobernanza. Tecnología concreta pendiente de validación.

## Trazabilidad

ADD-4; ADR-003; RF-16; vista de lectura y analítica.
