# Plan ADD — Trotamundos

## Secuencia de diseño

| Etapa | Objetivo | Salida |
|---|---|---|
| [ADD-1](01-Iteracion-1/Iteracion-1.md) | Arquitectura de alto nivel del sistema completo | Clientes, backend, dominio, integraciones y eventos internos |
| [ADD-2](02-Iteracion-2/Iteracion-2.md) | Componentes de funcionalidad central | Viajes/reservas, ingesta, adaptadores, identidad y notificaciones |
| [ADD-3](03-Iteracion-3/Iteracion-3.md) | Disponibilidad, escala, seguridad e interoperabilidad | Resiliencia, idempotencia, permisos, monitoreo |
| [ADD-4](04-Iteracion-4/Iteracion-4.md) | Rendimiento, analítica, recomendación y experiencia | Proyecciones de lectura, almacén analítico, contrato del recomendador |
| [Etapa previa al prototipo](05-Integraciones-pendientes.md) | Validar APIs, cuotas y permisos reales | Contratos implementables y limitaciones documentadas |

La etapa 5 complementa, pero no reemplaza, las cuatro iteraciones ADD. El README del repositorio no forma parte de este cambio.

## Reglas

Cada iteración identifica objetivo, entradas, drivers, elemento a refinar, alternativas, decisiones, estructura, vistas, ADR, evaluación y siguientes pasos. Las vistas representan diseño propuesto; no demuestran por sí mismas disponibilidad o escala. Se distinguen metas del enunciado de supuestos de dimensionamiento.

## Drivers principales

RF-01/RF-05 y RN-01–RN-05 (viajes/reservas); RF-07/RF-08/RF-17/RF-18 (correo autorizado); RF-11–RF-15 (integraciones turísticas y agencia); RF-16 (analítica); RF-19 (notificaciones); RF-20–RF-22 (recomendaciones); RF-23/RF-24 (compartición); QA-A1 (5 min/mes de indisponibilidad); QA-P1/P2/P3 (frescura 5 min, web 800 ms, FCP móvil <1,4 s); QA-S1/S2 (15 M de cuentas, 2 M activos semanales); seguridad, interoperabilidad, evolución y multirregión.

La integración directa con la agencia se diseña detrás de un adaptador, pero queda condicionada a que exista una API oficial compatible. Para correo y proveedores turísticos se prefieren notificaciones/webhooks cuando estén disponibles; se admite consulta periódica cuando sea necesaria.
