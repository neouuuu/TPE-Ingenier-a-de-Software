# ADR-004: Integración con servicio externo de mapas y rutas

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Categoría:** Integración externa

## Contexto y problema
Trotamundos debe ofrecer experiencia móvil contextual y puede sugerir rutas. El GPS del dispositivo obtiene ubicación; no reemplaza mapas, geocodificación ni cálculo de rutas.

## Drivers
Experiencia móvil/GPS; RF-21; QA-U1; disponibilidad de servicios externos; CRN-11.

## Alternativas consideradas
1. Desarrollar mapas y cálculo de rutas propios.
2. Integrar un servicio externo especializado.
3. Usar solo GPS, sin mapas ni cálculo de rutas.

## Decisión
Integrar un servicio externo de mapas/rutas detrás de un puerto y adaptador. El proveedor se seleccionará durante la etapa 5 tras comparar cobertura, funciones, costo, límites, atribución, privacidad y términos.

## Consecuencias
**Beneficios:** se aprovechan capacidades geográficas especializadas y se reduce desarrollo propio.

**Costos/riesgos:** dependencia de latencia, disponibilidad, cuotas y condiciones del proveedor. Se debe definir fallback y proteger datos de ubicación. La consulta del itinerario no debe fallar si mapas no está disponible.

## Trazabilidad
RF-21; QA-U1; ADD-4; etapa 5 de integraciones.
