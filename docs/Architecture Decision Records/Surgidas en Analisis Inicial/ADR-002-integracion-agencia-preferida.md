# ADR-002: Integración técnica con la agencia de viajes preferida

- **Estado:** Aceptado como objetivo de diseño; API pendiente de validación
- **Fecha:** 2026-10-28

## Contexto y problema
Trotamundos debe ayudar a resolver problemas de viaje a través de la agencia preferida del usuario. RF-15 pide integración técnica cuando exista una integración compatible. Todavía no se identificó la agencia concreta ni se verificó que exponga una API oficial con las operaciones necesarias.

## Drivers
RF-15; QA-I1 (interoperabilidad); QA-SE1 (acceso autorizado); CRN-05 (condiciones de terceros); CON-10 (APIs estándar).

## Alternativas consideradas
1. Integración técnica directa mediante adaptador, si existe una API compatible.
2. Derivación indirecta a un canal externo.
3. Excluir la agencia del flujo.

## Decisión
Diseñar una **integración técnica directa** detrás de un puerto/adaptador, con contrato interno desacoplado del proveedor. La implementación queda pendiente de la etapa 5, donde se verifican API oficial, autenticación, permisos, operaciones, cuotas y condiciones de uso.

Si no existe una API viable, no se simulará una integración: se documentará el bloqueo y se revisará con el equipo/cátedra la alternativa de alcance. La derivación indirecta solo puede adoptarse mediante una decisión explícita posterior.

## Consecuencias
- La arquitectura contempla RF-15 sin acoplar el dominio a una agencia específica.
- La viabilidad depende de capacidades y permisos de terceros.
- Hasta validar la API, RF-15 no puede considerarse implementado ni completamente resuelto.

## Trazabilidad
RF-15; ADD-1/ADD-2; ADR-009; [etapa 5 de integraciones](../../../ADD/05-Integraciones-pendientes.md).
