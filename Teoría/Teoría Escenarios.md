# Escenarios de atributos de calidad

## 1. ¿Qué es un escenario de atributo de calidad?

Un **escenario de atributo de calidad** describe una situación concreta que permite especificar cómo debería comportarse un sistema frente a un estímulo, para evaluar un atributo de calidad como rendimiento, disponibilidad, seguridad o modificabilidad.

Su objetivo es convertir una necesidad de calidad, que muchas veces es ambigua, en una descripción **concreta, verificable y, cuando sea posible, medible**.

Por ejemplo, decir:

> El sistema debe tener buen rendimiento.

es demasiado ambiguo. En cambio:

> Cuando 500 usuarios consulten sus itinerarios simultáneamente, el sistema deberá responder el 95 % de las consultas en menos de 2 segundos.

es mucho más útil para el diseño y la evaluación de la arquitectura.

Los valores del ejemplo son ilustrativos: en un proyecto real deben justificarse a partir de los requerimientos y las necesidades de los interesados.

---

## 2. Las seis partes de un escenario

Todo escenario de atributo de calidad se construye a partir de seis elementos.

| Parte | ¿Qué describe? | Pregunta orientativa |
|---|---|---|
| **1. Fuente del estímulo** | Quién o qué origina el estímulo. | ¿Quién o qué provoca la situación? |
| **2. Estímulo** | El evento, solicitud, cambio o condición que afecta al sistema. | ¿Qué sucede? |
| **3. Entorno** | Las condiciones en las que ocurre el estímulo. | ¿En qué condiciones ocurre? |
| **4. Artefacto** | El elemento del sistema que recibe o procesa el estímulo. Puede ser el sistema completo o uno de sus componentes. | ¿Qué parte del sistema se ve afectada? |
| **5. Respuesta** | Lo que se espera que haga el sistema ante el estímulo. | ¿Cómo debería reaccionar? |
| **6. Medida de respuesta** | El criterio observable que permite comprobar si la respuesta es satisfactoria. | ¿Cómo verificamos que respondió correctamente? |

### Template general de seis partes

```text
Atributo de calidad: [atributo]

1. Fuente del estímulo:
   [Quién o qué origina la situación]

2. Estímulo:
   [Evento, solicitud, cambio o condición]

3. Entorno:
   [Condiciones en las que ocurre]

4. Artefacto:
   [Sistema o componente afectado]

5. Respuesta:
   [Comportamiento esperado]

6. Medida de respuesta:
   [Métrica o criterio verificable]
```

### Ejemplo completo

Supongamos que estamos diseñando un sistema de planificación de viajes que permite crear itinerarios y asociarles reservas.

**Atributo: rendimiento**

| Parte | Escenario |
|---|---|
| Fuente | Usuarios autenticados. |
| Estímulo | Solicitan consultar sus itinerarios. |
| Entorno | El sistema opera con 500 usuarios concurrentes y una carga habitual de datos. |
| Artefacto | Servicio de consulta de itinerarios. |
| Respuesta | El sistema procesa las consultas y devuelve los itinerarios solicitados. |
| Medida de respuesta | El 95 % de las consultas responde en menos de 2 segundos. |

Este escenario permite evaluar una decisión arquitectónica: por ejemplo, si la forma de consultar los itinerarios y acceder a los datos es adecuada para la carga prevista.

---

## 3. Templates y ejemplos por atributo de calidad

Los siguientes templates se basan en las seis partes y adaptan el contenido a cada atributo. Los ejemplos utilizan el sistema de viajes como contexto común para facilitar su aplicación al proyecto.

## 3.1. Disponibilidad (*Availability*)

**¿Qué busca?**

Que el sistema o una funcionalidad esté operativo y pueda utilizarse cuando se necesita. Interesa especialmente cómo responde ante fallos y cuánto tarda en recuperarse.

### Template

- **Fuente:** usuario, componente interno, infraestructura o servicio externo.
- **Estímulo:** caída, interrupción, pérdida de conexión o fallo de un componente.
- **Entorno:** operación normal, carga elevada, mantenimiento o situación de fallo.
- **Artefacto:** sistema, servicio o componente cuya disponibilidad importa.
- **Respuesta:** detectar el fallo, mantener el servicio, activar una alternativa o recuperarse.
- **Medida de respuesta:** tiempo de recuperación, porcentaje de disponibilidad, duración de la interrupción o proporción de solicitudes atendidas.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Infraestructura que aloja el servicio de itinerarios. |
| Estímulo | Una instancia del servicio deja de funcionar. |
| Entorno | El sistema está en producción y recibe solicitudes de usuarios. |
| Artefacto | Servicio de consulta de itinerarios. |
| Respuesta | El sistema detecta el fallo y redirige las solicitudes a una instancia disponible. |
| Medida de respuesta | El servicio vuelve a atender solicitudes en menos de 30 segundos y no pierde los itinerarios confirmados. |

**Clave:** disponibilidad no significa únicamente evitar fallos. También importa detectarlos, recuperarse y mantener las funciones necesarias.

---

## 3.2. Modificabilidad (*Modifiability*)

**¿Qué busca?**

Que el sistema pueda modificarse para incorporar funcionalidades, cambiar reglas o adaptar componentes sin que los cambios se propaguen innecesariamente.

### Template

- **Fuente:** desarrollador, equipo de mantenimiento o responsable del producto.
- **Estímulo:** solicitud de cambio, incorporación de una funcionalidad o modificación de una regla.
- **Entorno:** desarrollo, mantenimiento o evolución de una versión existente.
- **Artefacto:** módulo, componente, interfaz o conjunto de componentes afectados.
- **Respuesta:** permitir el cambio limitando el impacto sobre otras partes del sistema.
- **Medida de respuesta:** tiempo de implementación, cantidad de componentes modificados, esfuerzo requerido o cantidad de pruebas de regresión necesarias.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Equipo de desarrollo. |
| Estímulo | Se solicita integrar un nuevo proveedor de reservas. |
| Entorno | El sistema ya está en producción y debe conservar sus integraciones actuales. |
| Artefacto | Subsistema de integración con proveedores de reservas. |
| Respuesta | El equipo incorpora el nuevo proveedor mediante un adaptador, sin modificar la lógica central de los itinerarios. |
| Medida de respuesta | La integración se completa en un máximo de 3 días de desarrollo y no requiere cambios en los componentes de itinerarios existentes. |

**Clave:** el escenario ayuda a decidir cómo separar responsabilidades, encapsular variaciones y establecer interfaces. Las métricas de esfuerzo y tiempo deben acordarse según el proyecto.

---

## 3.3. Rendimiento (*Performance*)

**¿Qué busca?**

Que el sistema responda dentro de límites aceptables cuando procesa solicitudes, eventos o cálculos bajo determinadas condiciones de carga.

### Template

- **Fuente:** usuario, sistema externo o componente que genera solicitudes.
- **Estímulo:** solicitud, evento, consulta o procesamiento.
- **Entorno:** carga, concurrencia, volumen de datos y recursos disponibles.
- **Artefacto:** sistema, servicio, operación o componente que procesa el estímulo.
- **Respuesta:** procesar la solicitud y producir el resultado esperado.
- **Medida de respuesta:** latencia, tiempo de respuesta, rendimiento por unidad de tiempo, uso de CPU o memoria, según corresponda.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Usuarios autenticados. |
| Estímulo | Consultan el detalle de sus itinerarios. |
| Entorno | Hay 500 usuarios concurrentes y el sistema opera con la carga prevista. |
| Artefacto | Servicio de consulta de itinerarios. |
| Respuesta | El sistema recupera y devuelve la información solicitada. |
| Medida de respuesta | El 95 % de las consultas se completa en menos de 2 segundos. |

**Clave:** rendimiento no es sinónimo de escalabilidad. El rendimiento describe cómo se comporta el sistema bajo unas condiciones dadas; la escalabilidad se relaciona con cómo cambia ese comportamiento al aumentar la carga o los recursos.

---

## 3.4. Seguridad (*Security*)

**¿Qué busca?**

Proteger la información y las operaciones del sistema frente a accesos, modificaciones o acciones no autorizadas.

### Template

- **Fuente:** usuario legítimo, usuario no autorizado, sistema externo o posible atacante.
- **Estímulo:** intento de acceso, consulta, modificación, eliminación o ejecución de una operación protegida.
- **Entorno:** sesión autenticada o no autenticada, operación normal o intento de abuso.
- **Artefacto:** recurso, dato, servicio u operación protegida.
- **Respuesta:** autenticar, autorizar, rechazar, limitar o registrar la acción según corresponda.
- **Medida de respuesta:** porcentaje de intentos no autorizados bloqueados, tiempo de detección, ausencia de accesos indebidos o generación de registros de auditoría.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Usuario autenticado que no es propietario de un itinerario. |
| Estímulo | Intenta consultar o modificar ese itinerario. |
| Entorno | El usuario tiene una sesión válida, pero carece de permisos sobre el recurso solicitado. |
| Artefacto | Servicio de gestión de itinerarios y su mecanismo de autorización. |
| Respuesta | El sistema deniega la operación y no revela información del itinerario. |
| Medida de respuesta | El 100 % de las solicitudes no autorizadas de la prueba son rechazadas y no se expone información protegida. |

**Clave:** autenticación y autorización no son lo mismo. Autenticar permite comprobar quién es el usuario; autorizar determina qué puede hacer.

---

## 3.5. Usabilidad (*Usability*)

**¿Qué busca?**

Que las personas puedan comprender y utilizar el sistema para realizar sus tareas de manera efectiva, con el nivel de aprendizaje y esfuerzo esperado.

### Template

- **Fuente:** usuario con determinado perfil o nivel de experiencia.
- **Estímulo:** necesidad de completar una tarea, aprender una función, recuperarse de un error o deshacer una acción.
- **Entorno:** primer uso, uso habitual, situación de presión o contexto de accesibilidad especificado.
- **Artefacto:** interfaz o funcionalidad con la que interactúa el usuario.
- **Respuesta:** guiar, informar, validar, facilitar la tarea o permitir recuperarse de errores.
- **Medida de respuesta:** tiempo para completar la tarea, porcentaje de tareas exitosas, cantidad de errores o necesidad de asistencia.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Usuario nuevo del sistema. |
| Estímulo | Necesita crear un itinerario y agregar una actividad. |
| Entorno | Es su primer uso y no cuenta con asistencia externa. |
| Artefacto | Interfaz de creación y edición de itinerarios. |
| Respuesta | El sistema guía al usuario mediante campos claros, validaciones y confirmaciones. |
| Medida de respuesta | Al menos el 90 % de los participantes de una prueba completa la tarea en menos de 3 minutos, sin asistencia. |

**Clave:** la usabilidad debe evaluarse con usuarios y tareas concretas. Decir que una interfaz es «intuitiva» no constituye una medida suficiente.

---

## 3.6. Testabilidad (*Testability*)

**¿Qué busca?**

Que sea posible verificar el comportamiento del sistema, detectar defectos y determinar si cumple sus requisitos con un esfuerzo razonable.

### Template

- **Fuente:** desarrollador, tester o sistema automatizado de pruebas.
- **Estímulo:** necesidad de verificar una funcionalidad, ejecutar una prueba o reproducir un fallo.
- **Entorno:** pruebas unitarias, de integración, de sistema o de regresión.
- **Artefacto:** componente, servicio, interfaz o comportamiento que se quiere verificar.
- **Respuesta:** permitir controlar las condiciones de prueba, observar resultados y aislar el comportamiento bajo evaluación.
- **Medida de respuesta:** tiempo de preparación y ejecución, proporción de casos automatizados, reproducibilidad o porcentaje de resultados verificables.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Equipo de testing. |
| Estímulo | Necesita verificar la lógica que asocia una reserva a un itinerario. |
| Entorno | Se ejecutan pruebas automatizadas sin depender de proveedores externos reales. |
| Artefacto | Componente responsable de asociar reservas e itinerarios. |
| Respuesta | El componente permite sustituir la dependencia externa por un doble de prueba y comprobar el resultado de la asociación. |
| Medida de respuesta | La batería de pruebas automatizadas puede ejecutarse sin conexión a proveedores externos y verifica todos los casos definidos para esa funcionalidad. |

**Clave:** una buena separación de responsabilidades y dependencias facilita las pruebas. La cobertura de código, por sí sola, no demuestra que un sistema esté correctamente probado.

---

## 3.7. Integrabilidad (*Integrability*)

**¿Qué busca?**

Que el sistema pueda incorporar e interactuar correctamente con componentes o sistemas externos, respetando sus contratos, protocolos y formatos.

### Template

- **Fuente:** sistema externo, proveedor o componente que se integra.
- **Estímulo:** envío o recepción de datos, invocación de una operación o cambio en una interfaz externa.
- **Entorno:** condiciones de comunicación, versiones, formatos y disponibilidad del sistema externo.
- **Artefacto:** interfaz de integración, adaptador o componente consumidor.
- **Respuesta:** traducir formatos, comunicarse mediante el protocolo acordado, validar los datos y manejar errores.
- **Medida de respuesta:** porcentaje de intercambios exitosos, tiempo de integración, conformidad con el contrato o cantidad de cambios internos necesarios ante una modificación externa.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Un proveedor externo de reservas. |
| Estímulo | El proveedor devuelve una reserva en el formato definido por su API. |
| Entorno | El sistema opera normalmente y el proveedor cumple su contrato de integración. |
| Artefacto | Adaptador del proveedor de reservas. |
| Respuesta | El adaptador transforma la respuesta externa al modelo interno y entrega los datos al subsistema de reservas. |
| Medida de respuesta | El 100 % de los casos válidos de la batería de integración se transforma correctamente y los casos inválidos se manejan según el contrato definido. |

**Clave:** integrabilidad no es simplemente «poder conectarse». También importa que los sistemas intercambien información con semántica, formatos y errores correctamente definidos.

---

## 3.8. Desplegabilidad (*Deployability*)

**¿Qué busca?**

Que las nuevas versiones, cambios o componentes puedan instalarse y ponerse en funcionamiento de manera controlada, con un riesgo y un esfuerzo aceptables.

### Template

- **Fuente:** equipo de operaciones, pipeline de integración y despliegue continuo o responsable de una versión.
- **Estímulo:** solicitud de despliegue, actualización o reversión de una versión.
- **Entorno:** producción, entorno de pruebas, mantenimiento programado o servicio activo.
- **Artefacto:** aplicación, servicio o unidad desplegable.
- **Respuesta:** instalar, configurar, verificar la nueva versión y, si corresponde, revertir el cambio.
- **Medida de respuesta:** tiempo de despliegue, duración de la interrupción, porcentaje de despliegues exitosos o tiempo de reversión.

### Ejemplo

| Parte | Escenario |
|---|---|
| Fuente | Pipeline automatizado de despliegue. |
| Estímulo | Se publica una nueva versión del servicio de itinerarios. |
| Entorno | El sistema está en producción y recibe solicitudes. |
| Artefacto | Servicio de itinerarios y su proceso de despliegue. |
| Respuesta | El sistema despliega la nueva versión, ejecuta verificaciones y permite volver a la versión anterior si las comprobaciones fallan. |
| Medida de respuesta | El despliegue finaliza en menos de 10 minutos, sin interrupción perceptible para los usuarios; si falla la verificación, se revierte en menos de 5 minutos. |

**Clave:** desplegabilidad no es lo mismo que disponibilidad. La primera se centra en la facilidad y seguridad de instalar cambios; la segunda, en que el servicio esté operativo cuando se necesita. Ambas se relacionan.

---

## 3.9. Seguridad operacional (*Safety*)

**¿Qué busca?**

Evitar que el sistema provoque situaciones peligrosas o daños inaceptables. Se diferencia de la seguridad informática: *safety* se ocupa de evitar accidentes o condiciones peligrosas; *security*, de proteger frente a acciones maliciosas o no autorizadas.

Este atributo es especialmente relevante en sistemas físicos, médicos, industriales, automotrices o de infraestructura crítica. No todos los sistemas necesitan un escenario específico de *safety*.

### Template

- **Fuente:** usuario, sensor, componente interno o entorno físico.
- **Estímulo:** condición peligrosa, valor fuera de rango, fallo o combinación de eventos que podría causar daño.
- **Entorno:** condiciones normales, operación degradada o situación de riesgo.
- **Artefacto:** función crítica, controlador o componente que puede contribuir a la situación peligrosa.
- **Respuesta:** detectar la condición, impedir la operación peligrosa, pasar a un estado seguro o alertar.
- **Medida de respuesta:** tiempo máximo para detectar o controlar la condición, proporción de situaciones peligrosas mitigadas o cumplimiento de un límite de seguridad definido.

### Ejemplo ilustrativo

| Parte | Escenario |
|---|---|
| Fuente | Sensor de temperatura de un sistema industrial. |
| Estímulo | La temperatura supera el umbral de seguridad establecido. |
| Entorno | El sistema está operando y el sensor funciona dentro de sus condiciones especificadas. |
| Artefacto | Controlador del equipo. |
| Respuesta | El controlador detiene la operación peligrosa y genera una alerta. |
| Medida de respuesta | La operación se detiene en menos de 1 segundo desde la detección del umbral y se registra el evento. |

**Clave:** el ejemplo es de un sistema industrial, no del sistema de viajes. La medida real debe surgir del análisis de riesgos y de los requisitos de seguridad aplicables.

---

## 3.10. Eficiencia energética (*Energy Efficiency*)

**¿Qué busca?**

Que el sistema realice el trabajo requerido utilizando una cantidad razonable de energía, especialmente cuando el consumo energético es relevante para el dominio o la infraestructura.

### Template

- **Fuente:** usuario, sistema externo o proceso programado.
- **Estímulo:** solicitud, tarea o carga de procesamiento.
- **Entorno:** volumen de trabajo, hardware disponible y condiciones de operación.
- **Artefacto:** proceso, servicio o sistema que consume energía.
- **Respuesta:** completar el trabajo evitando procesamiento, comunicación o consumo innecesarios.
- **Medida de respuesta:** energía consumida por
