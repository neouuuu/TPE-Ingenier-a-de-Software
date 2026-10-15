# ADR-001: Compartición de itinerarios por correo y redes sociales

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto
Trotamundos debe permitir compartir itinerarios y contemplar la interoperabilidad con proveedores de correo y redes sociales. Por correo, solo las personas designadas deben poder visualizar el itinerario. Se decidió que los destinatarios no necesitan una cuenta de Trotamundos y que compartir no habilita edición colaborativa.

## Decisión
Se ofrecen dos modalidades:
1. **Correo electrónico:** Trotamundos envía un enlace seguro al itinerario.
2. **Redes sociales:** el usuario elige una sola red por publicación y Trotamundos solicita publicar el itinerario seleccionado.

Los destinatarios por correo pueden consultar el itinerario sin registrarse y no pueden editarlo colaborativamente. El acceso debe restringirse a las personas designadas; el mecanismo concreto de autorización se definirá durante el diseño.

## Alternativas consideradas
- Compartir solo por redes sociales.
- Compartir solo por correo electrónico.
- Ofrecer ambas modalidades.

Se elige ofrecer ambas para cubrir los modos de compartición contemplados en el alcance.

## Consecuencias
### Positivas
- Los destinatarios pueden consultar un itinerario sin crear una cuenta.
- Se cubren la compartición privada por correo y la publicación social.
- Se evita ampliar el alcance con edición colaborativa.

### Costos y cuestiones pendientes
- Definir autorización de destinatarios, caducidad y revocación de enlaces.
- La publicación social depende de las capacidades, permisos y políticas de la plataforma; su visibilidad también puede depender de su configuración.
- Proteger los datos incluidos en el itinerario.

## Trazabilidad
- Requisitos de interoperabilidad con correo y redes sociales.
- Requisito de privacidad: acceso limitado a personas designadas.
