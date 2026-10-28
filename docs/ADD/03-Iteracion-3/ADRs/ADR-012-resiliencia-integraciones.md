# ADR-012: Aislar fallas de integraciones externas

- **Estado:** Aceptado para el diseño
- **Fecha:** 2026-10-28
- **Iteración:** ADD-3

## Contexto

Disponibilidad y frescura dependen de proveedores externos con latencia, cuotas y fallas fuera del control de Trotamundos. Reintentos ilimitados pueden propagar fallas.

## Drivers

QA-A1, QA-P1, QA-S1/S2, QA-I1/I2; RF-07/RF-11–RF-15; CRN-05/12/13.

## Alternativas

- Llamadas directas sin aislamiento.
- Reintentos inmediatos ilimitados.
- Timeouts, reintentos limitados, backoff+jitter, circuit breaker, límites de concurrencia y colas durables.

## Decisión

Adoptar la tercera alternativa. Mensajes que agoten reintentos pasan a DLQ con alertas y reproceso controlado. Aplicar backpressure y escalar con métricas de cola/latencia. La configuración se ajusta a cuotas reales.

## Consecuencias

Limita la propagación de fallas, pero agrega complejidad operativa. La frescura de cinco minutos no puede garantizarse si la fuente no expone el cambio a tiempo.

## Trazabilidad

ADD-3; vistas de resiliencia y actualización; QA-A1/QA-P1.
