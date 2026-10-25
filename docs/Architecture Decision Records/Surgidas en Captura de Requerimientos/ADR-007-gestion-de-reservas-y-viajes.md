# ADR-007: Gestión y asignación de reservas a viajes

- **Estado:** Aceptado
- **Fecha:** 2026-10-15
- **Categoría:** Diseño funcional y modelo de dominio

## Contexto

El sistema debe permitir al usuario registrar reservas manualmente, importarlas automáticamente desde correos electrónicos y organizarlas dentro de sus viajes.

Sin embargo, una reserva puede incorporarse al sistema antes de que exista el viaje al que corresponde o antes de que el usuario determine esa asociación. Por este motivo, la incorporación de una reserva no puede depender obligatoriamente de su asignación inmediata a un viaje.

Además, el sistema debe permitir consultar las reservas organizadas por viaje y facilitar la organización posterior de aquellas que todavía no estén asignadas.

## Decisión

Se adoptan las siguientes decisiones para la gestión de reservas:

1. **Relación entre reservas y viajes:** una reserva puede estar asociada a cero o un viaje como máximo. Un viaje puede contener múltiples reservas, pero una reserva no puede pertenecer simultáneamente a varios viajes.

2. **Registro manual:** el usuario puede registrar una reserva y asociarla opcionalmente a un viaje existente. También puede completar el registro sin realizar esa asociación.

3. **Importación automática:** el sistema debe poder identificar y registrar reservas a partir de correos electrónicos sin exigir que estén asociadas previamente a un viaje. No debe establecer asociaciones que no estén justificadas por la información disponible.

4. **Separación de responsabilidades:** la incorporación de una reserva y su organización dentro de un viaje son responsabilidades funcionales diferenciadas. El registro manual puede incluir una asignación opcional, pero esta no reemplaza la posibilidad de organizar la reserva posteriormente.

5. **Gestión de reservas pendientes:** el sistema debe permitir identificar y consultar las reservas que no están asociadas a ningún viaje, para que el usuario pueda organizarlas posteriormente.

6. **Asignación posterior:** el usuario puede asociar una reserva pendiente a un viaje existente o, cuando la funcionalidad de gestión de viajes lo permita, a un nuevo viaje. Toda asignación debe respetar la regla de asociación única.

## Alternativas consideradas

### A. Exigir la asignación al registrar cada reserva

Se descarta porque impide registrar reservas cuando el viaje correspondiente todavía no existe o no ha sido identificado.

### B. Asignar automáticamente todas las reservas importadas

Se descarta como comportamiento obligatorio porque la información de un correo puede ser insuficiente para determinar el viaje correcto, lo que podría generar asociaciones incorrectas.

### C. Permitir que una reserva pertenezca a varios viajes

Se descarta porque contradice la regla de dominio adoptada y podría producir inconsistencias al consultar y gestionar las reservas.

### D. Unificar la incorporación y la organización en una única operación obligatoria

Se descarta porque introduce una dependencia innecesaria entre registrar una reserva y organizarla. Se mantiene la posibilidad de realizar ambas acciones juntas en el registro manual cuando el usuario lo desee.

## Consecuencias

### Positivas

- Permite registrar reservas aunque el viaje correspondiente todavía no exista.
- Permite importar reservas automáticamente sin exigir intervención inmediata del usuario.
- Facilita la organización progresiva de los viajes.
- Evita que una reserva quede asociada simultáneamente a varios viajes.
- Mantiene diferenciadas las responsabilidades de incorporación y organización.
- Permite identificar y gestionar las reservas que todavía no están asignadas.

### Implicaciones para el diseño

- El modelo de dominio debe representar la asociación con un viaje como opcional.
- Las operaciones de registro, modificación y asignación deben validar la regla de asociación única.
- Las consultas deben permitir recuperar las reservas de un viaje y las que permanecen sin asignar.
- El procesamiento automático de correos debe poder finalizar aunque una reserva no tenga un viaje asociado.
- La arquitectura deberá resolver estas responsabilidades de acuerdo con los drivers seleccionados durante las iteraciones ADD, sin presuponer de antemano una distribución concreta de componentes.

## Trazabilidad

- **Requerimientos funcionales:** RF-01, RF-02, RF-03, RF-05 y RF-08.
- **Casos de uso:** CU-01, CU-02, CU-03, CU-05 y CU-07.
- **Reglas de negocio:** RN-01 a RN-05, relativas a la asociación y organización de reservas (definidas en [Reglas de negocio](../../An%C3%A1lisis%20del%20dominio/Reglas%20de%20negocio.md)).

## Notas

Este ADR documenta decisiones funcionales y de dominio. No determina todavía tecnologías, mecanismos de persistencia ni componentes arquitectónicos concretos.

Las decisiones arquitectónicas que implementen estas reglas se documentarán en ADR posteriores cuando sean justificadas por los drivers arquitectónicamente significativos.
