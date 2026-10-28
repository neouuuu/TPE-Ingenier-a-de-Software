# ADD-2 — Componentes de funcionalidad central

- **Estado:** propuesta de diseño
- **Objetivo:** asignar responsabilidades y contratos a los componentes que soportan los casos de uso centrales.

## Entradas y drivers

ADD-1; RF-01–RF-15, RF-17–RF-19; RN-01–RN-05; QA-P1, QA-I1/I2, QA-SE1, QA-E1; CRN-02/03/04/05/06/09.

## Elementos a refinar y justificación

- **Servicio de viajes/reservas y asignación:** aplica RN-01–RN-05 y soporta las lecturas frecuentes.
- **Orquestador de ingesta:** procesa correos no confiables y trabajos lentos sin bloquear la API.
- **Adaptadores de correo, turismo y agencia:** aíslan contratos externos cambiantes.
- **Identidad/compartición:** controla autorización de correo y enlaces sin cuenta.
- **Notificaciones:** avisa después de confirmar el cambio operativo.

## Diseño

| Componente | Responsabilidad |
|---|---|
| API de viajes | Consultar viajes, reservas asignadas y reservas sin asignar; DTOs versionados. |
| Servicio de reservas | Alta/edición/baja y validación de asociación única. |
| Servicio de viajes | Crear, consultar y archivar viajes. |
| Servicio de asignación | Asociar/desasociar reserva con validación transaccional. |
| Orquestador de correo | Obtener mensajes autorizados, filtrar y publicar candidatos. |
| Extractor/normalizador | Convertir mensajes a una reserva candidata; no asigna viaje por conjetura. |
| Adaptador de correo | Permisos OAuth mínimos, renovación y revocación. |
| Adaptador turístico | Traducir detalles, cambios y cancelaciones al contrato interno. |
| Adaptador de agencia | Ejecutar RF-15 solo si existe API compatible y autorizada. |
| Servicio de compartición | Enlaces de solo lectura y publicación social separada. |
| Notificaciones | Comunicar cambios relevantes tras persistirlos. |

Se usa un modelo canónico de reserva con procedencia y marcas temporales. La precedencia entre edición manual y actualización externa queda abierta; no se impone “gana el último evento” como regla universal.

## Vistas y ADR

- [Vista C&C central](Vistas/Vista-CyC-Central.md)
- [Vista de módulos central](Vistas/Vista-Modulos-Central.md)
- [ADR-010: modelo canónico y reconciliación](ADRs/ADR-010-modelo-canonico-reconciliacion.md)
- [ADR-011: ingesta idempotente](ADRs/ADR-011-ingesta-idempotente.md)

## Evaluación

Los flujos centrales tienen responsables y límites definidos. Riesgos abiertos: deduplicación, conflictos entre fuentes, extracción multilingüe, webhooks disponibles, autorización/caducidad de enlaces, API de agencia y canal de notificación. ADD-3 aborda resiliencia y controles de seguridad.
