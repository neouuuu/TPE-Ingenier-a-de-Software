# ADR-011: Procesamiento idempotente de mensajes y cambios

- **Estado:** Aceptado como táctica
- **Fecha:** 2026-10-28
- **Iteración:** ADD-2

## Contexto

Notificaciones, reintentos y consultas pueden entregar el mismo correo o cambio varias veces. Procesar repetidos sin control puede duplicar reservas y notificaciones.

## Drivers

RF-07/RF-08/RF-13/RF-14/RF-19; QA-P1, QA-A1, QA-I1/I2; CRN-02/03/05.

## Alternativas

- Confiar en entrega exactly-once extremo a extremo.
- Resolver duplicados manualmente.
- Usar claves de idempotencia y consumidores idempotentes.

## Decisión

Consumidores idempotentes, priorizando identificadores externos estables. Si no existen, definir una huella con límites documentados. Los eventos pueden entregarse al menos una vez; no se presume exactly-once extremo a extremo.

## Consecuencias

Los reintentos son más seguros, pero la deduplicación depende de identificadores y datos disponibles. Deben evitarse falsos positivos que fusionen reservas distintas.

## Trazabilidad

ADD-2; CRN-02; vistas C&C central y resiliencia.
