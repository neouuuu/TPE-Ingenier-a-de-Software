# ADR-015: Aislar el recomendador detrás de un contrato estable

- **Estado:** Aceptado para el diseño
- **Fecha:** 2026-10-28
- **Iteración:** ADD-4

## Contexto

El módulo avanzado recomienda alojamiento, transporte y rutas, y utiliza interacciones para mejorar resultados. El algoritmo puede evolucionar y no debe acoplarse al dominio transaccional.

## Drivers

RF-20/RF-21/RF-22; QA-P5, QA-E3, QA-SE3; CRN-10.

## Alternativas

- Incorporar algoritmo en servicios de dominio.
- Definir puerto de recomendación y contrato versionado.
- Depender de un proveedor opaco sin controlar datos/interfaz.

## Decisión

Definir una interfaz estable que reciba contexto mínimo autorizado y preferencias y devuelva sugerencias tipadas. Registrar aceptación/ajuste para evaluación posterior, sin reentrenamiento inmediato obligatorio. Si falla o excede el presupuesto temporal, la consulta del itinerario sigue funcionando.

## Consecuencias

Permite sustituir el algoritmo, pero requiere versionado, evaluación y control de acceso. Calidad y latencia deben medirse con el prototipo.

## Trazabilidad

ADD-4; ADR-005/006; RF-20–RF-22.
