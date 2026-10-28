# ADR-008: Arquitectura modular con procesamiento asíncrono dirigido por eventos

- **Estado:** Aceptado como diseño lógico
- **Fecha:** 2026-10-28
- **Iteración:** ADD-1

## Contexto

Trotamundos combina clientes web/móvil, consultas de reservas, procesamiento de correo y cambios externos, notificaciones y analítica. Los proveedores pueden fallar o responder lentamente y el prototipo tiene un alcance acotado.

## Drivers

RF-01/RF-05, RF-07/RF-08, RF-11–RF-16, RF-19; QA-A1, QA-P1/P2, QA-S1/S2, QA-I1/I2, QA-E1; CON-06/07/09–12; CRN-01/04/05/12/13/15/16.

## Alternativas

1. Monolito sin límites explícitos ni trabajo asíncrono.
2. Microservicios separados para todas las capacidades desde el inicio.
3. Módulos lógicos, APIs síncronas para interacción y eventos internos para tareas asíncronas, dejando el despliegue físico sujeto a evidencia.

## Decisión

Adoptar la alternativa 3. Las solicitudes interactivas usan request-response. Ingesta, conciliación, notificaciones y proyecciones se procesan de forma asíncrona. No se exige desplegar cada módulo como microservicio: se decidirá según aislamiento, costo y capacidad operativa.

## Consecuencias

**Beneficios:** aísla tareas lentas, permite escalar workers por separado y facilita separar cargas analíticas.

**Costos/riesgos:** consistencia eventual, duplicados, reintentos, observabilidad y operación de mensajería. Se requiere idempotencia. La estructura no demuestra por sí sola escala ni disponibilidad.

## Trazabilidad

ADD-1; vistas de módulos, C&C y asignación; ADD-2; ADR-010/011.
