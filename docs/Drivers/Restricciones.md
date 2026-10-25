# Restricciones — Trotamundos

Una **restricción** es una condición obligatoria que limita las alternativas de diseño. Se separan en tres grupos: las que impone el enunciado, las que son implícitas y las **decisiones ya tomadas** en los ADR del repo, que el diseño debe respetar mientras no se revisen.

## 1. Restricciones impuestas por el enunciado

| ID | Restricción | Tipo | Fuente |
|---|---|---|---|
| **CON-01** | El diseño debe aplicar el método **ADD**, con **mínimo 4 iteraciones**. | Proceso | Enunciado §1, §4 |
| **CON-02** | Las decisiones se documentan con **ADRs en formato MADR**. | Proceso | Enunciado §4 |
| **CON-03** | Deben elaborarse las **vistas arquitectónicas** adecuadas (módulos, componentes y conectores, despliegue, secuencia, etc.). | Proceso | Enunciado §4 |
| **CON-04** | Los artefactos y las iteraciones se capturan en una **Wiki** (por ejemplo, GitHub) con actualizaciones periódicas que muestren el trabajo de cada integrante. | Proceso | Enunciado §4 |
| **CON-05** | Se recomienda enfáticamente el enfoque **Spec-driven development**, tanto para el diseño como para la implementación. | Proceso | Enunciado §4 |
| **CON-06** | Debe desarrollarse un **prototipo** que demuestre la viabilidad de la arquitectura. El código debe ser trazable, consistente con la arquitectura documentada y respetar las especificaciones. | Entregable | Enunciado §1, §5 |
| **CON-07** | El trabajo es grupal y con cronograma estipulado: el **alcance del prototipo debe acotarse**. | Organizacional | Enunciado §2 |
| **CON-08** | Los requerimientos y atributos de calidad priorizados son **drivers inmutables** durante el ADD. | Proceso | Enunciado §3 |
| **CON-09** | El sistema debe ofrecerse en **web y móvil**. | Técnica | Enunciado, descripción del sistema |
| **CON-10** | La integración con proveedores de viajes debe hacerse mediante **APIs estándar**, según las interfaces que cada proveedor ofrezca. | Técnica | Enunciado, RF-11 |
| **CON-11** | El sistema debe ser **global** y estar preparado para **operar en múltiples regiones**. | Negocio | Enunciado, Usabilidad e internacionalización |
| **CON-12** | Debe interoperar con **proveedores de correo** y **redes sociales** para escanear mensajes y compartir itinerarios. | Técnica | Enunciado, Interoperabilidad |
| **CON-13** | Se debe incorporar **al menos un módulo avanzado**. El equipo eligió la **Opción A: sistema de recomendación**, con esquema *human-in-the-loop* (ver ADR-005). | Alcance | Enunciado, requerimientos avanzados |

## 2. Restricciones implícitas

Surgen del tipo de sistema, no figuran como texto en el enunciado.

| ID | Restricción | Tipo | Motivo |
|---|---|---|---|
| **CON-14** | Cumplimiento de la **normativa de protección de datos personales** de las regiones donde se opere (por ejemplo, GDPR y la Ley 25.326 de Argentina). | Legal | El sistema procesa información personal y correos. Debe confirmarse con la cátedra si se evalúa |
| **CON-15** | El acceso al correo requiere **autorización expresa del usuario** y debe respetar las condiciones de uso de cada proveedor. | Legal / Técnica | Diagrama de contexto: «solicita acceso autorizado a correos» |
| **CON-16** | Las consultas a proveedores **no implican que Trotamundos haga reservas**: el sistema solo lee y refleja información. | Alcance | Notas del diagrama de contexto |

## 3. Decisiones previas del repo que acotan el diseño

Son decisiones **aceptadas** en ADRs que el diseño toma como punto de partida. No las impone el enunciado, así que si el equipo las revisa, esta lista debe actualizarse.

| ID | Decisión | ADR | Estado | Efecto en el diseño |
|---|---|---|---|---|
| **DEC-01** | Se comparte por **correo** (enlace seguro) y por **red social** (una red por publicación). Los destinatarios **no necesitan cuenta** y **no pueden editar**. | ADR-001 | Aceptado | La autorización de acceso debe funcionar sin cuenta de Trotamundos. No hay edición colaborativa |
| **DEC-02** | La derivación a la **agencia de viajes** es **indirecta**: se muestran sus datos de contacto y el usuario se comunica por fuera. Sin integración técnica. | ADR-002 | Aceptado | RF-15 queda con poco impacto estructural. Revisar si el requisito exige integración directa |
| **DEC-03** | La analítica puede acceder a datos individuales **solo para tareas autorizadas y con controles**, priorizando datos agregados o desidentificados. «Monetizar» no significa vender datos personales. | ADR-003 | Aceptado | Se necesita control de acceso por rol, auditoría y desidentificación |
| **DEC-04** | Se usa un **servicio externo de mapas y navegación**. El proveedor aún no está elegido. El GPS del dispositivo es una capacidad aparte. | ADR-004 | Aceptado | Nueva dependencia externa. Falta definir el comportamiento cuando no esté disponible |
| **DEC-05** | Se incorpora la **Opción A: sistema de recomendación**. | ADR-005 | Aceptado | Hay que diseñar el módulo, sus datos y su interacción con el usuario |
| **DEC-06** | Se registran las **interacciones** con las recomendaciones para refinarlas. Sin reentrenamiento tras cada interacción. | ADR-006 | **Propuesto** | Pendiente de confirmar |
| **DEC-07** | Una reserva se asocia a **cero o un viaje**. Las reservas importadas pueden quedar **sin asignar**. La incorporación y la organización son responsabilidades separadas. | ADR-007 | Aceptado | El modelo de dominio debe tener la asociación opcional y validar la asignación única |

## 4. Restricciones de tecnología (por definir)

El enunciado **no impone** lenguaje, framework, proveedor de nube, base de datos ni presupuesto. Si el equipo o la cátedra tienen preferencias (o si hay límites de costo para el prototipo), conviene registrarlas aquí como restricciones **antes de la primera iteración**:

| ID | Restricción | Estado |
|---|---|---|
| CON-T1 | Lenguaje y framework del prototipo | Por definir |
| CON-T2 | Proveedor de nube o entorno de ejecución del prototipo | Por definir |
| CON-T3 | Proveedor de correo y APIs reales usadas en el prototipo | Por definir (pendiente en el resumen del sistema) |
| CON-T4 | Presupuesto y límites de uso de servicios de pago (mapas, nube) | Por definir |
