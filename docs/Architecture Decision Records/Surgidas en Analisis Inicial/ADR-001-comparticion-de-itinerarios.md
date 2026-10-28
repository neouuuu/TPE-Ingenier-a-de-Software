# ADR-001: Compartir itinerarios por correo y redes sociales

- **Estado:** Aceptado
- **Fecha:** 2026-10-28
- **Categoría:** Seguridad e interoperabilidad

## Contexto y problema
Trotamundos debe permitir compartir itinerarios con personas designadas y contempla interoperabilidad con redes sociales. Los destinatarios por correo pueden no tener una cuenta de Trotamundos. Compartir no debe habilitar edición colaborativa.

## Drivers
RF-23/RF-24; QA-SE2 (acceso limitado a destinatarios); QA-I3 (publicación social); requisitos de privacidad e interoperabilidad.

## Alternativas consideradas
1. Compartición solo por correo.
2. Publicación solo en redes sociales.
3. Ambas modalidades: enlace privado por correo y publicación social explícita.

## Decisión
Ofrecer ambas modalidades:
- **Correo:** enviar un enlace seguro de solo lectura al itinerario; el destinatario no necesita cuenta.
- **Redes sociales:** permitir al usuario elegir la red y solicitar la publicación del itinerario seleccionado, sujeta a capacidades y permisos de esa plataforma.

No se ofrece edición colaborativa. El mecanismo de verificación del destinatario, la caducidad y revocación del enlace se concretarán antes del prototipo.

## Consecuencias
**Beneficios:** destinatarios sin cuenta pueden consultar el itinerario y se cubren dos formas de compartir.

**Costos/riesgos:** el enlace puede reenviarse; se requieren expiración, revocación, minimización de datos y autorización clara. La publicación depende de APIs, permisos y visibilidad de la plataforma.

## Trazabilidad
RF-23/RF-24; QA-SE2/QA-I3; ADD-3; ADR-013.
