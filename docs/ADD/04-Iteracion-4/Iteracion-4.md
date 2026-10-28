# ADD-4 — Rendimiento, analítica, recomendación y experiencia

- **Estado:** propuesta de diseño
- **Objetivo:** proteger las lecturas interactivas, aislar consultas pesadas y permitir evolucionar el recomendador.

## Drivers

QA-P2 (web 800 ms), QA-P3 (FCP móvil <1,4 s), RF-16/QA-P4 (analítica pesada aislada), RF-20–RF-22/QA-P5/QA-E3 (recomendaciones con feedback), QA-U1/U2/U3 (móvil, internacionalización, multirregión), QA-SE3; CRN-07/08/10/11/14/15/16.

## Elementos a refinar

API de consulta y proyecciones; almacén analítico; servicio de recomendación; clientes web/móvil; adaptador de mapas. Estos elementos concentran los objetivos de latencia, las cargas distintas y la experiencia contextual.

## Conceptos de diseño

- CQRS selectivo: separar modelos de escritura/lectura donde la carga lo justifique, no necesariamente todo el sistema.
- Proyecciones de lectura y caché con invalidación explícita; datos sensibles aislados por usuario.
- Pipeline y almacén analítico separados de la base transaccional.
- Puerto de recomendación versionado, con entradas autorizadas y sugerencias tipadas. Feedback registrado para evaluación posterior, no reentrenamiento inmediato obligatorio.
- Fallback: si recomendador o mapas fallan, la consulta principal del itinerario continúa.
- Recursos web optimizados/carga diferida; textos y formatos externalizados; copia local mínima del itinerario activo solo si se define almacenamiento seguro.
- Preparar separación regional, pero decidir topología según residencia legal, costo y operación.

## Vistas y ADR

- [Vista de lectura y analítica](Vistas/Vista-Lecturas-Analitica.md)
- [Vista del recomendador](Vistas/Vista-Recomendador.md)
- [ADR-014: aislamiento de analítica](ADRs/ADR-014-aislamiento-analitica.md)
- [ADR-015: contrato del recomendador](ADRs/ADR-015-interfaz-recomendador.md)

## Evaluación

Se separan las consultas analíticas y se mantiene estable la interfaz del recomendador. No se fija motor analítico, algoritmo ni framework sin validar presupuesto y competencias. Riesgos: consistencia eventual, caché, evaluación del modelo, modo sin conexión, residencia regional, mapas y rendimiento real.
