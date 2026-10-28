# ADR-013: Proteger el correo y los itinerarios compartidos

- **Estado:** Aceptado para el diseño; detalles de autorización pendientes
- **Fecha:** 2026-10-28
- **Iteración:** ADD-3

## Contexto

Trotamundos accede a correos privados bajo autorización y permite compartir itinerarios con destinatarios sin cuenta. También puede publicar contenido en redes sociales a petición del usuario.

## Drivers

RF-17/RF-18/RF-23/RF-24; QA-SE1/SE2/SE3; CON-14/15; CRN-06/07/08.

## Alternativas

- Enlaces permanentes y acceso amplio.
- Exigir cuenta a todo destinatario.
- Mínimo privilegio, revocación de tokens y enlaces de solo lectura con expiración.

## Decisión

Aplicar scopes mínimos al correo y almacenar tokens en un gestor de secretos. La autorización puede revocarse. Los enlaces compartidos serán impredecibles, solo lectura, revocables y con vencimiento. Se debe especificar cómo se verifica el destinatario designado antes del prototipo. Publicar en redes es una acción explícita separada, sujeta a permisos y visibilidad de la plataforma.

## Consecuencias

Permite compartir sin cuenta ni edición colaborativa. Los enlaces bearer pueden reenviarse, por lo que la caducidad/revocación y la minimización de datos son esenciales. La normativa y retención de datos requieren definición por región.

## Trazabilidad

ADD-3; ADR-001; RF-17/RF-18/RF-23/RF-24.
