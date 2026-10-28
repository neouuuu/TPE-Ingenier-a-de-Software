# Reglas de negocio

Reglas del dominio que el sistema debe respetar, independientemente de cómo se diseñe. Las reglas RN-01 a RN-05 son las que cita el [ADR-007](Architecture%20Decision%20Records/Surgidas%20en%20Captura%20de%20Requerimientos/ADR-007-gestion-de-reservas-y-viajes.md) y se deducen de sus decisiones.

## Asociación y organización de reservas

| ID | Regla | Origen (ADR-007) | RF | CU |
|---|---|---|---|---|
| **RN-01** | Una reserva está asociada a **cero o un viaje** como máximo. Nunca pertenece a varios viajes a la vez. | Decisión 1 | RF-05 | CU-02, CU-03, CU-05 |
| **RN-02** | Un viaje puede contener **varias reservas**. | Decisión 1 | RF-01, RF-05 | CU-01, CU-05 |
| **RN-03** | Incorporar una reserva y organizarla en un viaje son responsabilidades **separadas**: registrar una reserva no exige asignarla a un viaje. En el registro manual la asignación es opcional y puede hacerse en el mismo paso, pero no reemplaza la posibilidad de organizarla después. | Decisiones 2 y 4 | RF-02, RF-05 | CU-02, CU-05 |
| **RN-04** | Las reservas importadas desde correo **no se asignan automáticamente** a un viaje salvo que la información disponible lo justifique. Si no lo justifica, quedan **sin asignar**. | Decisión 3 | RF-08 | CU-07 |
| **RN-05** | Las reservas **sin asignar** deben poder identificarse y consultarse, y asignarse luego a un viaje existente o, si la gestión de viajes lo permite, a uno nuevo. Toda asignación respeta RN-01. | Decisiones 5 y 6 | RF-01, RF-03, RF-05 | CU-01, CU-03, CU-05 |

## Reglas pendientes de definir

Estas reglas aparecen como pendientes en los casos de uso y todavía **no tienen número**. Cuando se decidan, se agregan a esta tabla.

| Tema | Dónde aparece | Qué falta definir |
|---|---|---|
| Deduplicación de reservas | CU-07 (alternativas) | Cuándo dos reservas se consideran la misma, y qué fuente prevalece (ver CRN-04) |
| Eliminación de reservas | CU-04 (postcondición) | Si se borra definitivamente o se conserva según una política de eliminación |
| Viaje completado | CU-06, RF-06 | Qué condiciones hacen que un viaje se considere completado, y quién lo archiva |
| Justificación de una asignación automática | RN-04 | Qué información alcanza para asociar una reserva importada a un viaje |
| Compartición | CU-15, ADR-001 | Expiración, revocación y permisos del enlace compartido |
