# ADR-005: Seleccionar el sistema de recomendación como módulo avanzado

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Categoría:** Alcance funcional

## Contexto y problema
La consigna exige incorporar al menos un módulo avanzado. La opción A analiza historial y preferencias para sugerir alternativas de alojamiento, transporte y rutas; contempla interacción humana para aceptar o ajustar recomendaciones.

## Drivers
RF-20/RF-21/RF-22; QA-P5/QA-E3; CRN-10; privacidad de datos personales.

## Alternativas consideradas
1. **Opción A:** sistema de recomendación personalizado.
2. **Opción B:** asistente conversacional/chatbot.

## Decisión
Seleccionar la **Opción A: sistema de recomendación**. Utilizará historial y preferencias autorizadas para producir sugerencias. El usuario puede aceptarlas o ajustar parámetros; las interacciones sirven como señal para evaluar y mejorar resultados.

## Consecuencias
**Beneficios:** personalización y una funcionalidad avanzada diferenciada.

**Costos/riesgos:** hay que definir acceso a datos, interfaz, evaluación de calidad, privacidad y comportamiento para usuarios sin historial. El algoritmo concreto se selecciona en el diseño del módulo/prototipo.

## Trazabilidad
RF-20–RF-22; ADD-4; ADR-006/015.
