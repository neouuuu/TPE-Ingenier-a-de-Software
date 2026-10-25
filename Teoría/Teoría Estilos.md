# Estilos arquitectónicos de software

## Introducción

Este apunte toma como base la **taxonomía clásica de estilos arquitectónicos**, organizando los estilos en familias según cómo se estructuran los componentes y cómo interactúan.

El objetivo es contar con una clasificación coherente para estudiar, sin mezclar categorías clásicas con patrones de diseño, estilos de despliegue y enfoques organizacionales.

Para cada familia se analiza:

- La idea central.
- Los componentes y conectores.
- Las características principales.
- Los estilos representativos.
- Los efectos posibles sobre los atributos de calidad.

---

## 1. ¿Qué es un estilo arquitectónico?

Un **estilo arquitectónico** define una forma general de organizar un sistema mediante tres elementos:

- **Componentes:** unidades que realizan procesamiento o almacenan información.
- **Conectores:** mecanismos que permiten la interacción entre componentes.
- **Restricciones:** reglas que establecen cómo pueden organizarse y relacionarse esos elementos.

Un estilo aporta una estructura general y condiciona las propiedades del sistema, pero **no garantiza por sí solo determinados atributos de calidad**. Sus beneficios y costos dependen de cómo se aplique y del contexto del sistema.

---

## 2. Las cinco familias clásicas

### 2.1. Data Flow — Flujo de datos

#### Idea central

Los datos atraviesan una secuencia de componentes que los transforman. La arquitectura se organiza alrededor del procesamiento de esos datos.

#### Esquema conceptual

```text
Entrada de datos
      |
      v
+-------------+
|  Filtro A   |
+-------------+
      |
      v
+-------------+
|  Filtro B   |
+-------------+
      |
      v
Salida de datos
```

*Esquema ilustrativo de Pipe-and-Filter.*

#### Componentes y conectores

- **Componentes:** etapas de procesamiento o filtros.
- **Conectores:** canales que transportan datos entre etapas.

#### Características

- Cada etapa transforma una entrada en una salida.
- Las etapas pueden reutilizarse.
- Si el procesamiento lo permite, distintas etapas pueden ejecutarse en paralelo.
- Las etapas pueden tener dependencias respecto del formato de los datos que reciben y producen.

#### Atributos de calidad

Puede favorecer:

- **Reutilización:** las etapas pueden aprovecharse en distintos flujos.
- **Modificabilidad:** es posible cambiar una etapa sin modificar necesariamente las demás, siempre que se mantengan los contratos de intercambio.
- **Rendimiento:** el paralelismo o el procesamiento incremental pueden mejorar el aprovechamiento de recursos.

Posibles costos:

- La conversión de datos entre etapas puede introducir sobrecarga.
- Los formatos incompatibles pueden dificultar la integración.
- La ejecución secuencial de etapas puede limitar el rendimiento.

#### Estilos representativos

**Batch Sequential**

Cada etapa procesa un conjunto de datos y entrega el resultado a la siguiente. Las etapas suelen ejecutarse secuencialmente.

**Pipe-and-Filter**

Los filtros procesan datos y los *pipes* los conectan. Puede permitir procesamiento incremental o concurrente, según la implementación.

**Diferencia clave:** Batch Sequential suele trabajar con lotes completos entre etapas, mientras que Pipe-and-Filter puede permitir que los datos fluyan progresivamente entre filtros.

---

### 2.2. Call-and-Return — Llamada y retorno

#### Idea central

El sistema se organiza en unidades que invocan operaciones de otras unidades y reciben el control o un resultado cuando finaliza la operación.

#### Esquema conceptual

```text
       +------------------+
       |  Módulo principal|
       +------------------+
          /            \
         v              v
   +-----------+  +-----------+
   | Módulo A  |  | Módulo B  |
   +-----------+  +-----------+
```

Las llamadas transfieren el control a otros módulos, que pueden devolver un resultado al finalizar.

#### Componentes y conectores

- **Componentes:** módulos, procedimientos, funciones u objetos.
- **Conectores:** llamadas a procedimientos, funciones o métodos.

#### Características

- Puede presentar una estructura jerárquica.
- Las relaciones entre unidades determinan el flujo de control.
- El comportamiento de un componente puede depender de los componentes que invoca.
- Las llamadas pueden ser locales o, en algunos casos, remotas.

#### Atributos de calidad

Puede favorecer:

- **Comprensibilidad:** una estructura jerárquica puede facilitar el seguimiento del flujo de control.
- **Modificabilidad:** la división en módulos puede ayudar a separar responsabilidades.
- **Testabilidad:** los módulos pueden probarse individualmente si sus dependencias están bien definidas.

Posibles costos:

- Las dependencias excesivas pueden perjudicar la modificabilidad.
- Una cadena larga de llamadas puede afectar el rendimiento.
- Los componentes muy acoplados pueden resultar difíciles de probar por separado.

#### Estilos representativos

**Main Program and Subroutines**

Un programa principal coordina subrutinas que realizan tareas específicas.

**Object-Oriented**

Los objetos encapsulan estado y comportamiento e interactúan mediante invocaciones de métodos. Es un estilo de organización que también puede combinarse con otros estilos arquitectónicos.

**Layered Architecture**

Los componentes se organizan en capas con responsabilidades diferentes y restricciones sobre sus dependencias.

**Client-Server**

Los clientes solicitan servicios y los servidores los proporcionan. Cuando las solicitudes se implementan mediante llamadas remotas, aparece una relación de llamada y retorno distribuida.

> **Importante:** estos estilos no son idénticos entre sí. Comparten la importancia de las invocaciones, pero difieren en la organización de los componentes y en las restricciones que establecen.

---

### 2.3. Independent Components — Componentes independientes

#### Idea central

Los componentes tienen cierto grado de autonomía y se coordinan mediante mecanismos de comunicación, sin que necesariamente exista una jerarquía central de llamadas.

#### Esquema conceptual

```text
+---------------+       +---------------+
| Componente A  |<----->| Componente B  |
+---------------+       +---------------+
         \                    /
          \    Mensajes      /
           \   o eventos    /
            v              v
              +---------------+
              | Componente C  |
              +---------------+
```

El diagrama es ilustrativo: las conexiones concretas dependen del mecanismo de comunicación utilizado.

#### Componentes y conectores

- **Componentes:** procesos, servicios o unidades de ejecución independientes.
- **Conectores:** mensajes, eventos, canales de comunicación o mecanismos de sincronización.

#### Características

- Los componentes pueden ejecutarse concurrentemente.
- Pueden comunicarse sin conocer todos los detalles internos de los demás.
- La comunicación puede ser directa o mediada por un intermediario.
- El grado de acoplamiento depende del protocolo y de las dependencias que existan entre los componentes.

#### Atributos de calidad

Puede favorecer:

- **Escalabilidad:** ciertos componentes pueden escalarse de manera independiente.
- **Modificabilidad:** es posible cambiar un componente sin alterar los demás si se mantienen los contratos de comunicación.
- **Concurrencia:** distintas unidades pueden realizar tareas simultáneamente.

Posibles costos:

- La comunicación distribuida puede dificultar el diagnóstico de fallos.
- La entrega, el orden y la duplicación de mensajes pueden introducir problemas adicionales.
- La coordinación entre componentes puede afectar la confiabilidad.

#### Estilos representativos

**Communicating Processes**

Procesos concurrentes que se comunican mediante mensajes u otros mecanismos de intercambio.

**Event-Based / Publish-Subscribe**

Los productores publican eventos y los consumidores interesados los reciben, frecuentemente mediante un intermediario.

#### Diferencia respecto de Call-and-Return

La coordinación no depende necesariamente de una cadena directa de llamadas.

En Publish-Subscribe, por ejemplo, un publicador puede desconocer qué componentes consumirán sus eventos. Esto reduce ciertas dependencias directas, aunque siguen existiendo contratos relacionados con los eventos.

---

### 2.4. Data-Centered — Centrada en datos

#### Idea central

Un almacén de datos compartido constituye el elemento central de la arquitectura. Los demás componentes colaboran leyendo o modificando esa información.

#### Esquema conceptual

```text
+---------------+       +---------------+
| Componente A  |       | Componente B  |
+---------------+       +---------------+
         \                    /
          \                  /
           v                v
        +----------------------+
        | Repositorio compartido|
        +----------------------+
           ^                ^
          /                  \
         /                    \
+---------------+       +---------------+
| Componente C  |       | Otros módulos |
+---------------+       +---------------+
```

#### Componentes y conectores

- **Componentes:** el repositorio o almacén central y los módulos que acceden a él.
- **Conectores:** consultas, lecturas, escrituras y operaciones de acceso a datos.

#### Características

- Los componentes pueden intercambiar información mediante el almacén sin comunicarse directamente entre sí.
- El repositorio funciona como un punto común de acceso a la información.
- Los componentes dependen, en alguna medida, de la estructura de los datos y de las reglas de acceso.

#### Atributos de calidad

Puede favorecer:

- **Integración:** distintos componentes pueden acceder a una fuente común de información.
- **Consistencia:** puede facilitar que los datos se administren de manera centralizada.
- **Modificabilidad:** algunos componentes pueden cambiar internamente sin alterar a los demás si se conserva el contrato del repositorio.

Posibles costos:

- El repositorio puede convertirse en un cuello de botella.
- Puede constituir un punto único de falla si no existen mecanismos de redundancia y recuperación.
- Los cambios en el modelo de datos pueden afectar a muchos componentes.

#### Estilos representativos

**Repository**

Los componentes acceden a un repositorio común de datos, normalmente persistentes.

**Blackboard**

Varios componentes especializados colaboran sobre una estructura de datos compartida. Cada uno puede aportar información parcial hasta alcanzar una solución.

#### Diferencia entre Repository y Blackboard

- **Repository:** enfoque general de almacenamiento y acceso compartido a datos.
- **Blackboard:** enfoque de colaboración en el que distintos especialistas aportan resultados parciales sobre un problema común.

---

### 2.5. Virtual Machine — Máquina virtual

#### Idea central

El sistema proporciona una abstracción que permite interpretar instrucciones, ejecutar un lenguaje o evaluar reglas, en lugar de implementar directamente cada comportamiento mediante instrucciones nativas.

#### Esquema conceptual

```text
+----------------------+
| Programa o conjunto  |
| de reglas            |
+----------------------+
           |
           v
+----------------------+
| Intérprete o motor   |
| de reglas            |
+----------------------+
           |
           v
+----------------------+
| Operaciones          |
| ejecutadas           |
+----------------------+
```

#### Componentes y conectores

- **Componentes:** intérprete, motor de ejecución, representación de instrucciones o conjunto de reglas.
- **Conectores:** invocaciones, flujo de instrucciones y mecanismos de evaluación.

#### Características

- Introduce un nivel de abstracción entre la descripción del comportamiento y su ejecución.
- Permite definir comportamientos mediante instrucciones o reglas.
- Puede facilitar la adaptación del comportamiento sin modificar toda la implementación subyacente.

#### Atributos de calidad

Puede favorecer:

- **Portabilidad:** una misma representación puede ejecutarse en distintos entornos si existe un motor compatible.
- **Flexibilidad:** el comportamiento puede cambiar modificando instrucciones o reglas.
- **Modificabilidad:** ciertos cambios pueden realizarse en las reglas sin alterar el motor.

Posibles costos:

- La interpretación puede agregar sobrecarga de rendimiento.
- El motor puede aumentar la complejidad del sistema.
- El lenguaje o las reglas pueden requerir validación y mecanismos de diagnóstico específicos.

#### Estilos representativos

**Interpreter**

Interpreta instrucciones expresadas en un lenguaje o representación definida.

**Rule-Based System**

Representa parte del comportamiento mediante reglas que un motor evalúa para decidir qué acciones ejecutar.

---

## 3. Comparación general de las familias

| Familia | ¿Qué organiza principalmente? | Conectores típicos | Ejemplos |
|---|---|---|---|
| **Data Flow** | Transformaciones de datos | Pipes y transferencia de datos | Pipe-and-Filter, Batch Sequential |
| **Call-and-Return** | Invocaciones y flujo de control | Llamadas y retornos | Main Program/Subroutines, Layered Architecture |
| **Independent Components** | Componentes autónomos y comunicación | Mensajes y eventos | Communicating Processes, Publish-Subscribe |
| **Data-Centered** | Acceso a información compartida | Lecturas, escrituras y consultas | Repository, Blackboard |
| **Virtual Machine** | Interpretación o ejecución de reglas | Instrucciones y evaluación | Interpreter, Rule-Based System |

### Pregunta clave para distinguirlas

Cuando tengas que identificar una familia, preguntate:

**¿Cuál es el principio organizador predominante del sistema?**

- Transformar datos → **Data Flow**.
- Invocar operaciones y transferir el control → **Call-and-Return**.
- Coordinar unidades autónomas mediante comunicación → **Independent Components**.
- Compartir un almacén de información → **Data-Centered**.
- Interpretar instrucciones o evaluar reglas → **Virtual Machine**.

---

## 4. ¿Dónde quedan los otros patrones y enfoques?

No es necesario forzar todos los conceptos arquitectónicos dentro de las cinco familias clásicas. Algunos describen aspectos diferentes de la arquitectura.

| Concepto | ¿Qué organiza o describe? | Observación |
|---|---|---|
| **Ports and Adapters** | El núcleo de negocio y sus interfaces con el exterior | Separa la lógica central de las tecnologías y sistemas externos. |
| **SOA** | Capacidades ofrecidas mediante servicios | Los servicios pueden comunicarse mediante llamadas o mensajes. |
| **Microservices** | Servicios pequeños y desplegables de forma independiente | Implica decisiones de modularidad, comunicación y despliegue. |
| **Multi-Tier** | Distribución de componentes en niveles de ejecución | Describe principalmente una organización de despliegue. |
| **MVC** | Responsabilidades de presentación, modelo y control | Organiza la interacción entre responsabilidades de la aplicación. |
| **Event-Driven Architecture** | Comportamiento organizado alrededor de eventos | Puede utilizar Publish-Subscribe como mecanismo de comunicación. |
| **Center of Competence** | Organización y colaboración de personas o equipos | No es un estilo estructural clásico de software. |
| **Open Source Contribution** | Colaboración mediante contribuciones a un proyecto | Se enfoca en la organización del trabajo. |
| **Big Ball of Mud** | Estructura arquitectónica desordenada y difícil de mantener | Es un antipatrón, no una solución arquitectónica recomendable. |

### ¿Se pueden combinar?

Sí. Las familias clásicas no son mutuamente excluyentes ni abarcan por sí solas todas las arquitecturas modernas.

Por ejemplo, una aplicación podría:

- Tener una **estructura lógica en capas**.
- Desplegarse en varios **niveles de ejecución**.
- Utilizar **eventos** para comunicar algunos componentes.
- Guardar la información en un **repositorio compartido**.
- Incorporar un intérprete para ejecutar reglas de negocio configurables.

Cada concepto describe una dimensión o un principio organizador que puede coexistir con otros.

---

## 5. Relación con los atributos de calidad

Un estilo arquitectónico influye en los atributos de calidad porque impone determinadas estructuras, dependencias y formas de comunicación.

Sin embargo, no existe una correspondencia automática del tipo «estilo X garantiza calidad Y». Los resultados dependen de las decisiones concretas de diseño y de implementación.

| Familia | Posibles beneficios | Riesgos o costos |
|---|---|---|
| **Data Flow** | Reutilización, separación de transformaciones y posible paralelismo | Sobrecarga de transferencia y conversión de datos |
| **Call-and-Return** | Estructura comprensible, modularidad y flujo de control explícito | Acoplamiento entre módulos y costo de llamadas sucesivas |
| **Independent Components** | Concurrencia, escalabilidad y menor dependencia directa en algunos diseños | Complejidad de comunicación, coordinación y diagnóstico |
| **Data-Centered** | Integración y acceso compartido a información | Cuellos de botella, dependencia del modelo de datos y posibles puntos únicos de falla |
| **Virtual Machine** | Portabilidad, flexibilidad y separación entre descripción y ejecución | Sobrecarga de interpretación y complejidad del motor |

Para evaluar una arquitectura, no alcanza con reconocer su estilo. También hay que identificar los escenarios de calidad relevantes y analizar si las decisiones arquitectónicas ayudan a satisfacerlos.

---

## 6. Qué conviene recordar para el examen

### Resumen conceptual

- **Data Flow:** lo central es transformar y transferir datos entre etapas.
- **Call-and-Return:** lo central es quién invoca a quién y cómo fluye el control.
- **Independent Components:** lo central es la autonomía de los componentes y su comunicación.
- **Data-Centered:** lo central es el almacén de información compartida.
- **Virtual Machine:** lo central es interpretar instrucciones o evaluar reglas mediante un motor.

### Método para analizar una arquitectura

Cuando te presenten una arquitectura, seguí estos pasos:

1. **Identificá los componentes.** ¿Qué unidades realizan el trabajo o almacenan información?
2. **Identificá los conectores.** ¿Cómo interactúan esas unidades: llamadas, eventos, transferencia de datos, consultas?
3. **Identificá las restricciones.** ¿Qué relaciones están permitidas o prohibidas?
4. **Reconocé el principio organizador predominante.** ¿Qué familia explica mejor la estructura principal?
5. **Analizá los atributos de calidad.** ¿Qué beneficios y costos introduce esa organización?
6. **Considerá combinaciones.** ¿El sistema utiliza más de un estilo o describe dimensiones diferentes, como estructura lógica y despliegue?

### Preguntas de autoevaluación

- ¿Cuál es la diferencia principal entre Batch Sequential y Pipe-and-Filter?
- ¿Por qué Object-Oriented y Layered Architecture no describen exactamente la misma organización?
- ¿Qué diferencia existe entre una llamada directa y una comunicación basada en eventos?
- ¿Por qué un repositorio compartido puede facilitar la integración y, al mismo tiempo, convertirse en un cuello de botella?
- ¿Qué distingue a Blackboard de un Repository convencional?
- ¿Qué ventaja ofrece un intérprete y qué costo potencial introduce?
- ¿Por qué Microservices y Multi-Tier no deben tratarse automáticamente como sinónimos?
- ¿Por qué una arquitectura puede combinar varios estilos?

---

## 7. Síntesis final

La taxonomía clásica permite razonar sobre la arquitectura a partir de su **principio de organización predominante**: flujo de datos, llamadas, componentes independientes, datos compartidos o interpretación de instrucciones.

Para comprender un estilo, no basta con memorizar su nombre. Es necesario entender:

- Cómo se organizan sus componentes.
- Qué conectores utilizan.
- Qué restricciones establece.
- Qué atributos de calidad puede favorecer.
- Qué costos o riesgos puede introducir.

Los estilos arquitectónicos son herramientas conceptuales para tomar y justificar decisiones de diseño. No son categorías completamente excluyentes ni recetas que garanticen una arquitectura de calidad.

## Bibliografía y alcance del apunte

La clasificación presentada corresponde a una **taxonomía clásica de estilos arquitectónicos**, complementada con explicaciones y ejemplos para facilitar el estudio.

Los apartados sobre atributos de calidad y la comparación con enfoques modernos son una síntesis conceptual; no deben interpretarse como una transcripción literal de una única fuente bibliográfica. Para una entrega académica, conviene contrastar los nombres y la clasificación exacta con la bibliografía indicada por la cátedra.
