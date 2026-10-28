# Etapa 5 — Validación de integraciones antes del prototipo

- **Estado:** pendiente de evidencia externa.
- **Propósito:** convertir los puertos en contratos implementables sin inventar capacidades de terceros.
- **Nota:** esta etapa no reemplaza las cuatro iteraciones ADD.

| Integración | Preferencia | Validaciones obligatorias |
|---|---|---|
| Correo | Notificaciones/webhooks si existen; consulta periódica como fallback | OAuth/scopes, permisos, webhook/renovación, cuotas, verificación de aplicación, revocación, sandbox y términos. |
| Proveedores turísticos | Eventos si se ofrecen; consulta según cuotas si no | APIs de acceso a reservas, autenticación, identificadores, cambios/cancelaciones, límites y consistencia. |
| Agencia preferida (RF-15) | Integración técnica directa detrás de adaptador | API oficial, autenticación, consentimiento, operaciones permitidas, acuerdos y disponibilidad. Si no existe API viable, documentar bloqueo y consultar cambio de alcance; no simular integración. |
| Mapas/rutas | API externa detrás de puerto | Cobertura, rutas, costo, límites, atribución, privacidad y fallback. |
| Redes sociales | Publicación explícita en una red seleccionada | API vigente, permisos, revisión de aplicación, formatos, privacidad y visibilidad real. |
| Notificaciones al usuario | Canal desacoplado | Push/correo, opt-in, preferencias, entrega y reintentos. |

## Entregables

1. Matriz de proveedores, capacidades verificadas, costos y límites.
2. Contrato interno estable y mapeo de errores para cada puerto.
3. OpenAPI para APIs HTTP propias y esquemas versionados para eventos.
4. Pruebas de contrato y adaptadores contra sandbox/fixtures.
5. Limitaciones, riesgos y cambios de alcance documentados.
6. ADR para decisiones de proveedor que cambien materialmente la arquitectura.

## Criterio de salida

No comenzar integración real hasta comprobar que la API permite la operación requerida bajo sus términos y permisos. Si no existe API compatible para la agencia, RF-15 queda como bloqueo/limitación explícita a resolver, no como integración implementada.
