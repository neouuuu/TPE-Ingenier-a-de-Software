# Tácticas arquitectónicas de software

## Introducción

La diferencia fundamental entre un estilo y una táctica arquitectónica es la siguiente:

- **Estilo arquitectónico:** define una organización general de los componentes y sus relaciones.
- **Táctica arquitectónica:** es una decisión de diseño más específica que busca influir en un atributo de calidad, como disponibilidad, rendimiento, seguridad o modificabilidad.

Una táctica no suele definir toda la arquitectura: puede aplicarse dentro de diferentes estilos arquitectónicos.

Por ejemplo, una arquitectura en capas puede utilizar:
- **Caché** para mejorar el rendimiento.
- **Autenticación y autorización** para controlar el acceso.
- **Redundancia** para aumentar la disponibilidad.

El enfoque clásico para estudiar tácticas consiste en relacionarlas con los atributos de calidad que ayudan a satisfacer.

La cuarta edición de *Software Architecture in Practice* organiza este tema alrededor de atributos como disponibilidad, desplegabilidad, eficiencia energética, integrabilidad, modificabilidad, rendimiento, seguridad funcional (*safety*), seguridad informática (*security*), testeabilidad y usabilidad.

> **Nota sobre el alcance:** este apunte es una síntesis conceptual ampliada, no un catálogo exhaustivo ni una transcripción literal de todas las tácticas del libro. Las denominaciones y clasificaciones exactas deben contrastarse con la bibliografía de la cátedra.

---

## 1. Disponibilidad (*Availability*)

### Objetivo

Que el sistema esté operativo y accesible cuando se necesita, incluso ante fallas.

Las tácticas se pueden entender según tres objetivos generales: **detectar fallas, recuperarse de ellas y prevenirlas**.

### 1.1. Detectar fallas

| Táctica | Descripción |
|---|---|
| Monitorización | Observar el estado de componentes y servicios. |
| Detección de excepciones | Identificar errores durante la ejecución. |
| Heartbeat | Comprobar periódicamente si un componente sigue respondiendo. |

**Ejemplo:** un monitor detecta que un servicio dejó de responder.

### 1.2. Recuperarse de fallas

| Táctica | Descripción |
|---|---|
| Redundancia activa o pasiva | Disponer de otra instancia que pueda continuar el servicio. |
| Failover | Cambiar a una instancia alternativa cuando falla la principal. |
| Reintentos | Volver a intentar una operación cuando el error es transitorio. |
| Rollback o recuperación de estado | Restaurar una situación consistente cuando corresponde. |

**Ejemplo:** si una instancia cae, el balanceador dirige las solicitudes a otra instancia disponible.

### 1.3. Prevenir fallas

- **Eliminar puntos únicos de falla:** evitar que un único componente pueda detener todo el sistema.
- **Controlar la carga:** impedir que la saturación provoque una caída en cadena.
- **Actualizar o reparar componentes de forma controlada:** reducir las interrupciones durante el mantenimiento.

**Ejemplo:** distribuir las instancias y sus dependencias para que una sola falla no interrumpa todo el servicio.

### Idea clave

La disponibilidad no depende solamente de tener varias instancias. También requiere detectar las fallas, decidir cómo recuperarse y evitar que un problema se propague.

---

## 2. Desplegabilidad (*Deployability*)

### Objetivo

Poder instalar, actualizar o reemplazar versiones del sistema de manera rápida, controlada y con bajo riesgo.

### Tácticas representativas

| Táctica | Descripción |
|---|---|
| Automatizar el despliegue | Ejecutar los pasos mediante scripts o pipelines reproducibles. |
| Despliegues graduales | Liberar una versión a un subconjunto de usuarios antes de extenderla. |
| Rollback | Volver a una versión anterior si la nueva presenta problemas. |
| Reducir el acoplamiento entre componentes desplegables | Evitar que un cambio obligue a desplegar innecesariamente todo el sistema. |
| Monitorear la nueva versión | Comprobar su comportamiento antes de ampliar el despliegue. |

**Ejemplo:** desplegar una versión nueva primero al 5 % de los usuarios, medir errores y latencia y luego ampliar progresivamente.

### Idea clave

La desplegabilidad busca que los cambios puedan llegar a producción de forma controlada y recuperable. No se limita a automatizar la instalación: también importa cómo se libera una versión, cómo se detectan problemas y cómo se revierte el cambio.

---

## 3. Eficiencia energética (*Energy Efficiency*)

### Objetivo

Realizar el trabajo requerido consumiendo una cantidad aceptable de energía.

### Tácticas o estrategias relevantes

- **Reducir trabajo innecesario:** evitar cálculos, consultas o transferencias que no aportan valor.
- **Controlar la frecuencia de procesamiento:** no ejecutar tareas con más frecuencia de la necesaria.
- **Administrar recursos:** ajustar el uso de CPU, memoria, almacenamiento y red.
- **Agrupar operaciones cuando conviene:** reducir costos repetidos de activación o comunicación.
- **Elegir algoritmos eficientes:** reducir el costo computacional para una misma tarea.

**Ejemplo:** agrupar escrituras en una operación por lotes en vez de activar repetidamente un dispositivo para cada escritura.

### Trade-offs

Las decisiones de eficiencia energética pueden entrar en conflicto con otros atributos.

Por ejemplo, mantener muchas réplicas activas puede mejorar la disponibilidad, pero aumentar el consumo energético.

### Idea clave

No se trata simplemente de utilizar menos recursos, sino de consumir energía de forma razonable para realizar el trabajo que el sistema necesita.

---

## 4. Integrabilidad (*Integrability*)

### Objetivo

Que componentes o sistemas desarrollados por separado puedan combinarse y funcionar correctamente juntos.

### Tácticas representativas

| Táctica | Descripción |
|---|---|
| Definir interfaces explícitas | Especificar operaciones, entradas, salidas y errores. |
| Acordar formatos y protocolos | Establecer cómo se representan e intercambian los datos. |
| Usar adaptadores | Traducir entre interfaces incompatibles sin modificar necesariamente los componentes originales. |
| Aislar dependencias externas | Evitar que los detalles de un sistema externo se propaguen por toda la aplicación. |
| Validar contratos de integración | Comprobar que las interacciones cumplen las expectativas acordadas. |

**Ejemplo:** integrar una API de reservas externa mediante un adaptador que traduzca su respuesta al modelo interno del sistema.

### Idea clave

La integrabilidad no significa solamente que dos sistemas puedan conectarse: también deben poder **entenderse e intercambiar información correctamente**.

---

## 5. Modificabilidad (*Modifiability*)

### Objetivo

Reducir el costo, el esfuerzo y el riesgo de cambiar el sistema.

Las tácticas buscan principalmente limitar cuánto código y cuántos componentes hay que modificar ante un cambio.

### 5.1. Reducir el impacto de los cambios

| Táctica | Descripción |
|---|---|
| Encapsular | Ocultar decisiones internas detrás de una interfaz. |
| Usar intermediarios | Evitar dependencias directas entre componentes. |
| Separar responsabilidades | Concentrar cada responsabilidad en un lugar coherente. |
| Limitar dependencias | Reducir la cantidad de módulos afectados por una modificación. |

**Ejemplo:** cambiar el proveedor de mapas modificando un adaptador en vez de alterar toda la lógica de negocio.

### 5.2. Facilitar la extensión

- **Usar abstracciones e interfaces estables:** permitir implementaciones alternativas.
- **Diferir decisiones:** postergar elecciones que no es necesario fijar desde el inicio.
- **Restringir variaciones:** definir explícitamente qué aspectos pueden cambiar y cómo.

**Ejemplo:** permitir distintos proveedores de pago mediante una interfaz común.

### Advertencia

Una abstracción adicional no siempre mejora la modificabilidad. Si no existe una variación real o probable, puede agregar complejidad sin aportar un beneficio suficiente.

### Idea clave

La modificabilidad busca que un cambio tenga un impacto acotado y previsible. Para conseguirlo, importan el acoplamiento, la cohesión y la distribución de responsabilidades.

---

## 6. Rendimiento (*Performance*)

### Objetivo

Responder dentro de límites aceptables de tiempo, capacidad de procesamiento o latencia.

Las tácticas actúan principalmente sobre dos aspectos: **la demanda de trabajo y los recursos disponibles**.

### 6.1. Administrar la demanda

| Táctica | Descripción |
|---|---|
| Reducir el trabajo por solicitud | Eliminar cálculos o accesos redundantes. |
| Controlar la frecuencia de eventos | Evitar procesar más eventos de los necesarios. |
| Priorizar tareas | Dar preferencia a operaciones críticas. |
| Limitar la carga | Controlar cuánto trabajo se admite simultáneamente. |

**Ejemplo:** evitar recalcular un informe completo cada vez que un usuario consulta un dato.

### 6.2. Administrar recursos

- **Introducir concurrencia:** ejecutar tareas independientes simultáneamente.
- **Mantener múltiples copias:** distribuir solicitudes entre réplicas.
- **Aumentar recursos disponibles:** disponer de más capacidad de procesamiento o memoria.
- **Reducir la sobrecarga de comunicación:** minimizar intercambios innecesarios entre componentes.

**Ejemplo:** procesar solicitudes independientes en paralelo para reducir el tiempo de espera.

### 6.3. Tácticas conocidas

| Táctica | Beneficio esperado | Posible costo |
|---|---|---|
| Caching | Evitar cálculos o accesos costosos repetidos. | Invalidez de datos, consumo de memoria y problemas de consistencia. |
| Concurrencia | Ejecutar varias tareas simultáneamente. | Contención, sincronización y condiciones de carrera. |
| Replicación | Distribuir solicitudes entre varias instancias. | Mayor consumo de recursos y coordinación adicional. |
| Balanceo de carga | Repartir solicitudes entre recursos disponibles. | Sobrecarga de coordinación y posibles desequilibrios. |

### Idea clave

Estas estrategias no son intercambiables en todos los casos. Una caché puede reducir la latencia, pero introduce problemas de invalidación y consistencia; la concurrencia puede aumentar el rendimiento, pero también generar contención.

Antes de elegir una táctica, conviene identificar qué está causando la demora.

---

## 7. Seguridad funcional (*Safety*)

### Objetivo

Evitar que el sistema provoque situaciones peligrosas o consecuencias inaceptables para las personas, los equipos o el entorno.

No debe confundirse con *security*: aquí se busca prevenir daños accidentales o comportamientos peligrosos, no principalmente ataques intencionales.

### Tácticas relevantes

- **Detectar condiciones peligrosas:** identificar estados fuera de los límites permitidos.
- **Interbloqueos y restricciones:** impedir operaciones incompatibles o peligrosas.
- **Fail-safe:** ante determinadas fallas, pasar a un estado seguro.
- **Monitorear límites:** verificar que las variables críticas se mantengan dentro de rangos aceptables.
- **Aislar funciones críticas:** evitar que una falla no crítica comprometa una función de seguridad.

**Ejemplo:** un sistema de control detiene una máquina si detecta que la temperatura supera un umbral peligroso.

### Advertencia

El estado seguro debe definirse para cada contexto. Detenerse puede ser seguro en una máquina, pero no necesariamente en todos los sistemas.

### Idea clave

La seguridad funcional busca evitar daños provocados por el comportamiento del sistema, incluidos errores y fallas accidentales.

---

## 8. Seguridad informática (*Security*)

### Objetivo

Proteger la confidencialidad, integridad y disponibilidad de los activos frente a acciones no autorizadas.

### 8.1. Prevenir ataques o accesos indebidos

| Táctica | Descripción |
|---|---|
| Autenticación | Verificar quién es el usuario o sistema. |
| Autorización | Determinar qué acciones puede realizar. |
| Mínimo privilegio | Otorgar solamente los permisos necesarios. |
| Cifrado | Proteger datos almacenados o transmitidos. |
| Validación de entradas | Rechazar datos que no cumplan las reglas esperadas. |

**Ejemplo:** un usuario puede autenticarse correctamente, pero solo acceder a las reservas que está autorizado a consultar.

### 8.2. Detectar y responder

- **Auditoría y registros:** registrar operaciones relevantes.
- **Monitoreo de actividad:** detectar patrones sospechosos.
- **Limitar intentos:** dificultar ataques automatizados.
- **Aislar componentes:** contener el impacto de una vulnerabilidad.

**Ejemplo:** registrar accesos administrativos y alertar ante intentos repetidos de autenticación fallida.

### Trade-offs

Las tácticas concretas dependen de las amenazas y de los activos que se quieran proteger. Agregar controles puede aumentar la latencia y la complejidad, por lo que deben responder a riesgos identificados.

### Idea clave: *safety* no es *security*

| Safety | Security |
|---|---|
| Evita situaciones peligrosas y daños accidentales. | Protege frente a acciones no autorizadas y amenazas. |
| Se preocupa por estados peligrosos y fallas. | Se preocupa por accesos, ataques y uso indebido. |
| Ejemplo: detener una máquina ante una temperatura peligrosa. | Ejemplo: impedir que un usuario acceda a datos ajenos. |

---

## 9. Testeabilidad (*Testability*)

### Objetivo

Facilitar la comprobación de que el sistema se comporta correctamente y detectar fallas con un esfuerzo razonable.

### Tácticas representativas

- **Controlar y observar el estado interno:** facilitar la inspección del comportamiento durante las pruebas.
- **Separar componentes:** permitir probar unidades sin ejecutar todo el sistema.
- **Usar interfaces sustituibles:** reemplazar dependencias externas por dobles de prueba (*test doubles*).
- **Automatizar pruebas:** ejecutar verificaciones repetibles.
- **Reducir el no determinismo:** controlar factores que hacen que una prueba produzca resultados diferentes en ejecuciones equivalentes.

**Ejemplo:** probar la lógica de asignación de reservas con un repositorio simulado, sin conectarse a la base de datos real.

### Idea clave

Una arquitectura testeable permite verificar comportamientos de forma **aislada, repetible y observable**.

---

## 10. Usabilidad (*Usability*)

### Objetivo

Que los usuarios puedan realizar sus tareas de manera efectiva, comprensible y con un esfuerzo adecuado.

### Tácticas representativas

| Táctica | Descripción |
|---|---|
| Deshacer y cancelar | Permitir revertir o abandonar operaciones. |
| Mantener consistencia en la interfaz | Usar comportamientos y convenciones previsibles. |
| Dar retroalimentación | Comunicar el resultado de una acción y el estado del sistema. |
| Guiar la interacción | Ayudar al usuario a comprender qué puede hacer a continuación. |
| Recordar información útil | Evitar que el usuario tenga que introducir repetidamente los mismos datos, cuando sea apropiado. |

**Ejemplo:** al crear una reserva, mostrar un resumen antes de confirmar y permitir volver atrás para corregir los datos.

### Idea clave

Las tácticas de usabilidad no son únicamente decisiones estéticas. Pueden requerir cambios en el flujo de control, el estado y la interfaz del sistema.

---

## 11. Tabla comparativa para repasar

Esta tabla resume los objetivos y las tácticas representativas. No es un catálogo exhaustivo de todas las tácticas de la cuarta edición de *Software Architecture in Practice*.

| Atributo de calidad | ¿Qué busca? | Tácticas representativas |
|---|---|---|
| **Disponibilidad** | Continuar operando ante fallas. | Detección de fallas, redundancia, failover y recuperación. |
| **Desplegabilidad** | Liberar cambios de forma controlada. | Automatización, despliegues graduales y rollback. |
| **Eficiencia energética** | Reducir el consumo para realizar el trabajo requerido. | Reducir trabajo innecesario y administrar recursos. |
| **Integrabilidad** | Combinar componentes o sistemas correctamente. | Interfaces explícitas, adaptadores y contratos. |
| **Modificabilidad** | Reducir el costo de los cambios. | Encapsulación, abstracción y limitación de dependencias. |
| **Rendimiento** | Responder dentro de límites temporales. | Caché, concurrencia, réplicas y balanceo de carga. |
| **Seguridad funcional (*safety*)** | Evitar situaciones peligrosas. | Detección de condiciones peligrosas, estado seguro y aislamiento. |
| **Seguridad informática (*security*)** | Proteger activos frente a accesos indebidos. | Autenticación, autorización, mínimo privilegio y cifrado. |
| **Testeabilidad** | Facilitar la verificación del comportamiento. | Observabilidad, aislamiento e interfaces sustituibles. |
| **Usabilidad** | Facilitar que los usuarios realicen sus tareas. | Deshacer, retroalimentación, consistencia y guía. |

La cuarta edición también dedica atención a otros atributos de calidad y a cómo adaptar el análisis cuando las necesidades de un sistema no encajan en una lista estándar.

---

## 12. Cómo aplicar tácticas en un ejercicio de ADD

Lo importante no es memorizar una lista aislada, sino saber **cuándo elegir una táctica y cómo justificarla**.

### Ejemplo: el sistema debe seguir funcionando cuando falla una instancia

**1. Driver**

Disponibilidad. Un escenario concreto podría exigir que, ante la caída de una instancia, el servicio se recupere dentro de un tiempo máximo.

**2. Problema arquitectónico**

Una única instancia es un punto único de falla.

**3. Tácticas elegidas**

Redundancia, detección de fallas y *failover*.

**4. Decisión de diseño**

Desplegar dos instancias y definir cómo detectar la falla y dirigir las solicitudes a la instancia disponible.

**5. Trade-offs**

- Mayor disponibilidad potencial.
- Mayor costo de infraestructura.
- Necesidad de gestionar el estado compartido y la consistencia.
- Posible complejidad adicional de operación y monitoreo.

**6. Evaluación**

Comprobar mediante el escenario de calidad que el tiempo de recuperación cumple el objetivo requerido.

### Flujo general de aplicación

```text
Driver o escenario de calidad
            |
            v
Identificar el problema arquitectónico
            |
            v
Seleccionar una táctica adecuada
            |
            v
Definir la decisión de diseño
            |
            v
Analizar beneficios y trade-offs
            |
            v
Evaluar si se cumple el escenario
```

### Relación con ADD

En ADD, las tácticas ayudan a convertir los drivers en decisiones arquitectónicas concretas. Después se documentan los componentes, conectores, restricciones y consecuencias de esas decisiones.

No se trata de elegir una táctica solamente porque se relaciona con un atributo: hay que justificar que responde al problema concreto y evaluar sus efectos secundarios.

---

## 13. Lo que tenés que recordar

### Tres ideas centrales

**1. El atributo de calidad define el objetivo; la táctica propone cómo influir en él.**

Si necesitás mejorar el rendimiento, no elegís una caché automáticamente: primero identificás qué está causando la demora.

**2. Las tácticas tienen consecuencias y trade-offs.**

Una decisión puede mejorar un atributo y perjudicar otro. Por ejemplo, la redundancia puede mejorar la disponibilidad, pero aumentar los costos y el consumo energético.

**3. En ADD, las tácticas ayudan a transformar los drivers en decisiones arquitectónicas concretas.**

Después hay que documentar los componentes, conectores, restricciones y consecuencias de esas decisiones.

### Preguntas de autoevaluación

- ¿Cuál es la diferencia entre un estilo arquitectónico y una táctica?
- ¿Por qué la disponibilidad requiere algo más que redundancia?
- ¿Cómo se diferencian el rendimiento y la eficiencia energética?
- ¿Qué diferencia hay entre integrabilidad y modificabilidad?
- ¿Por qué una abstracción adicional puede perjudicar la modificabilidad?
- ¿Qué ventajas y costos puede introducir una caché?
- ¿Cuál es la diferencia entre *safety* y *security*?
- ¿Cómo puede una arquitectura mejorar la testeabilidad?
- ¿Por qué conviene evaluar los trade-offs antes de elegir una táctica?
- ¿Cómo se relacionan las tácticas con los drivers y las decisiones de ADD?

---

## Bibliografía y alcance

La referencia principal para profundizar en estos temas es:

- *Software Architecture in Practice*, 4.ª edición.
  - Capítulo 3: diseño con tácticas.
  - Capítulos 4 a 13: desarrollo de atributos de calidad, según la organización de esa edición.

Este documento es una síntesis conceptual ampliada. Para estudiar con precisión las denominaciones que utiliza la cátedra, conviene contrastar especialmente las listas y clasificaciones de tácticas de cada capítulo con el libro.

