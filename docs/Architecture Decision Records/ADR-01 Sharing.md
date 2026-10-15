# ADR-000X: Compartir itinerarios mediante redes sociales y correo electrónico

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto

Trotamundos debe permitir compartir itinerarios y contemplar la interoperabilidad con redes sociales. Además, debe garantizar que únicamente las personas específicamente designadas puedan visualizar los itinerarios compartidos.

El enunciado no establece que los destinatarios deban tener una cuenta en Trotamundos ni define un mecanismo concreto para compartir itinerarios con acceso restringido.

Es necesario elegir una solución que contemple tanto la difusión de itinerarios en redes sociales como el acceso restringido para destinatarios específicos.

## Atributos de calidad y requerimientos relacionados

- **Seguridad y privacidad:** restringir la visualización de los itinerarios compartidos a las personas autorizadas.
- **Interoperabilidad:** permitir compartir itinerarios mediante redes sociales.
- **Usabilidad:** ofrecer mecanismos de uso compartido accesibles para los usuarios.

## Alternativas consideradas

1. **Compartir únicamente mediante redes sociales.** Aprovechar las opciones de publicación y privacidad de las plataformas externas. No cumple el requisito de estringir la visualización de los itinerarios compartidos a las personas autorizadas.
2. **Compartir únicamente mediante correo electrónico.** Enviar enlaces a destinatarios específicos, sin integrar redes sociales. No cumple el requisito de permitir compartir itinerarios mediante redes sociales.
3. **Combinar redes sociales y correo electrónico.** Permitir la publicación mediante redes sociales y el acceso restringido mediante enlaces enviados por correo electrónico.

## Decisión

Se adopta la tercera alternativa: Trotamundos ofrecerá dos modalidades para compartir itinerarios:

- **Redes sociales:** permitir compartir itinerarios mediante la integración con plataformas sociales. La visibilidad de las publicaciones estará sujeta a las opciones de privacidad de cada plataforma.
- **Correo electrónico:** permitir designar destinatarios y enviarles un enlace seguro para consultar el itinerario. El acceso deberá estar restringido a las personas autorizadas, de acuerdo con el requerimiento de seguridad.

Los destinatarios podrán consultar los itinerarios compartidos, pero no modificarlos, ya que pueden no ser usuarios del sistema, entonces, la edición colaborativa no forma parte del alcance definido.

El mecanismo concreto de protección de los enlaces —por ejemplo, su vinculación con los destinatarios, revocación o vencimiento— deberá definirse durante el diseño detallado.

## Consecuencias

### Positivas

- Se contemplan tanto la difusión en redes sociales como el acceso restringido a destinatarios específicos.
- Se evita exigir que los destinatarios tengan una cuenta en Trotamundos sin que exista un requerimiento que lo establezca.
- Se mantiene separada la privacidad controlada por Trotamundos de la privacidad gestionada por plataformas externas.

### Negativas y compromisos

- La integración con redes sociales dependerá de las capacidades y restricciones de las plataformas seleccionadas.
- El mecanismo de enlaces seguros deberá diseñarse e implementarse para evitar accesos no autorizados.
- La publicación en redes sociales no permite garantizar que únicamente las personas designadas puedan visualizar el contenido, ya que la visibilidad también depende de la plataforma externa.
- Se deberán definir las medidas necesarias para proteger la información incluida en los itinerarios compartidos.

## Referencias

- Requerimiento de interoperabilidad con redes sociales para compartir itinerarios.
- Requerimiento de seguridad y privacidad relativo al acceso exclusivo de personas específicamente designadas.
