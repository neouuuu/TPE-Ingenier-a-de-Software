# Restricciones — Trotamundos

Una restricción limita las alternativas de diseño. Se distingue entre condiciones del enunciado, restricciones implícitas y decisiones aceptadas en ADR (que pueden revisarse mediante otra decisión).

## 1. Impuestas por el enunciado

| ID | Restricción | Tipo | Fuente |
|---|---|---|---|
| CON-01 | Aplicar ADD con al menos cuatro iteraciones. | Proceso | Enunciado |
| CON-02 | Registrar decisiones con ADR en formato MADR. | Proceso | Enunciado |
| CON-03 | Elaborar vistas arquitectónicas pertinentes. | Proceso | Enunciado |
| CON-04 | Documentar el proceso y sus artefactos en la wiki/repositorio. | Proceso | Enunciado |
| CON-05 | Usar enfoque spec-driven para diseño e implementación. | Proceso | Enunciado |
| CON-06 | Construir un prototipo trazable y coherente con arquitectura/especificaciones. | Entregable | Enunciado |
| CON-07 | Acotar el prototipo al cronograma. | Organizacional | Enunciado |
| CON-08 | Mantener los drivers priorizados como base del diseño salvo revisión explícita del alcance. | Proceso | Enunciado/cátedra |
| CON-09 | Ofrecer cliente web y móvil. | Técnica | Descripción del sistema |
| CON-10 | Integrarse con proveedores turísticos mediante APIs estándar que estos ofrezcan. | Técnica | RF-11 |
| CON-11 | Preparar el sistema para operación global/multirregión. | Negocio/técnica | Enunciado |
| CON-12 | Interoperar con proveedores de correo y redes sociales mediante capacidades disponibles. | Técnica | Enunciado |
| CON-13 | Incluir módulo avanzado; se eligió sistema de recomendación (Opción A). | Alcance | ADR-005 |

## 2. Implícitas

| ID | Restricción | Motivo/estado |
|---|---|---|
| CON-14 | Cumplir normativa de protección de datos aplicable a las regiones de operación. | Debe confirmarse el alcance legal aplicable. |
| CON-15 | Acceder al correo solo con autorización expresa y respetar permisos/términos del proveedor. | Seguridad y condiciones de API. |
| CON-16 | Consultar reservas no implica que Trotamundos efectúe una compra/reserva automáticamente. | Límite de alcance. |

## 3. Decisiones aceptadas que condicionan el diseño

| ID | Decisión | ADR | Efecto |
|---|---|---|---|
| DEC-01 | Compartir por enlace seguro de correo y publicación social; destinatarios pueden no tener cuenta y solo visualizan. | ADR-001 | Se necesita autorización para enlaces sin identidad local y publicación social explícita. |
| DEC-02 | Diseñar integración técnica directa con la agencia preferida mediante adaptador, condicionada a verificar API compatible. | ADR-002 | RF-15 no se considera implementado hasta validar proveedor y API. |
| DEC-03 | Acceso analítico individual solo para tareas autorizadas; priorizar agregación/desidentificación cuando alcance. | ADR-003 | Control de acceso, auditoría y política de datos. |
| DEC-04 | Usar servicio externo de mapas; proveedor pendiente. | ADR-004 | Aislar dependencia y definir fallback. |
| DEC-05 | Sistema de recomendación, Opción A. | ADR-005 | Definir datos, interfaz y evaluación. |
| DEC-06 | Registrar interacciones para evaluar/refinar recomendaciones; sin reentrenamiento inmediato obligatorio. | ADR-006 | ADR-006 sigue propuesto hasta aceptación explícita; el diseño ADD trata la idea como requisito de la consigna y deja la táctica concreta abierta. |
| DEC-07 | Reserva asociada a cero o un viaje; puede quedar sin asignar. | ADR-007 | Asociación opcional y validación de unicidad. |

## 4. Restricciones tecnológicas pendientes

| ID | Tema | Estado |
|---|---|---|
| CON-T1 | Lenguaje y framework del prototipo | Por decidir según capacidades y cronograma. |
| CON-T2 | Infraestructura/proveedor de ejecución | Por decidir según costo y alcance. |
| CON-T3 | APIs de correo, viajes y agencia | Etapa 5; no asumir capacidades no verificadas. |
| CON-T4 | Presupuesto y límites de uso de nube/mapas | Por validar antes de fijar tecnología. |
