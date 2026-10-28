# ADD-1 — Arquitectura de alto nivel

- **Estado:** propuesta de diseño
- **Objetivo:** establecer la partición de alto nivel para web, móvil, dominio, integraciones y procesos asíncronos.

## 1. Entradas

RF-01/RF-05, RF-07/RF-08, RF-11–RF-16, RF-17/RF-18, RF-20–RF-24; QA-A1, QA-P1/P2, QA-S1/S2, seguridad, interoperabilidad y evolución; CON-06/07/09–12; ADR-001–ADR-007.

## 2. Drivers seleccionados

- RF-01/RF-05 y RN-01–RN-05: dominio central de viajes y reservas.
- RF-07/RF-08 y RF-11–RF-14: ingesta de fuentes externas heterogéneas, frescura y trabajo asíncrono.
- RF-16: consultas analíticas pesadas sin degradar la operación.
- QA-A1 y QA-S1/S2: disponibilidad y escala objetivo.
- QA-P1/P2: actualizaciones en 5 min y respuesta web de 800 ms.
- QA-SE1/SE2/SE3: correo autorizado, enlaces compartidos y analítica protegida.
- QA-E1 e QA-I1/I2: nuevos transportes y proveedores sin acoplar el dominio.

## 3. Elemento a refinar

El sistema completo: todavía no hay límites estables entre solicitudes interactivas, procesamiento externo y analítica.

## 4. Conceptos y alternativas

Se elige cliente-servidor con web RIA y móvil sobre backend compartido; módulos lógicos por capacidad; Ports and Adapters en integraciones; eventos internos para tareas asíncronas. Las solicitudes del usuario siguen siendo request-response.

Un monolito modular reduce costo inicial y es viable para el prototipo. Microservicios independientes permiten aislamiento, pero agregan costo de operación y consistencia distribuida. Por eso se fijan límites lógicos que permitan despliegue separado si la evidencia lo justifica, sin exigir un microservicio por módulo desde el día uno.

## 5. Estructura resultante

- Cliente web RIA y cliente móvil.
- API de aplicación: autenticación, autorización, validación y contratos versionados.
- Dominio: usuarios, viajes, reservas y reglas de asignación.
- Workers de ingesta, conciliación, notificaciones y tareas programadas.
- Puertos/adaptadores para correo, proveedores turísticos, agencia, mapas y redes sociales.
- Persistencia operativa y canal de eventos interno.
- Proyección/almacén analítico separado.
- Módulo de recomendación detrás de una interfaz estable.

La integración directa con la agencia preferida se modela como adaptador opcional, condicionado a validar una API compatible en la etapa 5.

## 6. Vistas y ADR

- [Vista de módulos](Vistas/Vista-Modulos.md)
- [Vista C&C](Vistas/Vista-CyC.md)
- [Vista de asignación](Vistas/Vista-Asignacion.md)
- [ADR-008](ADRs/ADR-008-arquitectura-modular-y-eventos.md), [ADR-009](ADRs/ADR-009-puertos-adaptadores-e-integraciones.md)

## 7. Evaluación

Se fijan límites y responsabilidades de alto nivel. Los objetivos de escala, disponibilidad y latencia siguen sin demostrarse. Riesgos abiertos: costo operativo, duplicados y reintentos, reconciliación entre fuentes, cuotas de terceros, residencia regional y capacidades reales de APIs. ADD-2 detallará los componentes centrales.
