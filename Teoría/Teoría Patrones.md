# Patrones de diseño

> **Bibliografía principal:** *Design Patterns: Elements of Reusable Object-Oriented Software*, Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides (GoF).
>
> **Objetivo:** comprender los patrones de diseño, reconocer cuándo utilizarlos y justificar su elección dentro del diseño de un sistema. Se incluyen también conexiones con atributos de calidad, tácticas arquitectónicas y el método ADD.

## Índice

1. [¿Qué es un patrón de diseño?](#1-qué-es-un-patrón-de-diseño)
2. [Cómo se describe un patrón](#2-cómo-se-describe-un-patrón)
3. [Clasificación de los patrones GoF](#3-clasificación-de-los-patrones-gof)
4. [Patrones creacionales](#4-patrones-creacionales)
5. [Patrones estructurales](#5-patrones-estructurales)
6. [Patrones de comportamiento](#6-patrones-de-comportamiento)
7. [Relación entre patrones y tácticas](#7-relación-entre-patrones-y-tácticas)
8. [Cómo pasar de las tácticas a los patrones](#8-cómo-pasar-de-las-tácticas-a-los-patrones)
9. [Ejemplo aplicado a un sistema de viajes](#9-ejemplo-aplicado-a-un-sistema-de-viajes)
10. [Cómo documentar las decisiones en ADD](#10-cómo-documentar-las-decisiones-en-add)
11. [Cómo estudiar los patrones](#11-cómo-estudiar-los-patrones)
12. [Síntesis final](#12-síntesis-final)

---

## 1. ¿Qué es un patrón de diseño?

Un patrón de diseño describe una solución reutilizable para un problema recurrente de diseño de software dentro de un contexto determinado.

No es una clase prediseñada que se copia literalmente ni un algoritmo que resuelve cualquier problema. Es una descripción de los elementos que participan en una solución, sus responsabilidades, sus relaciones y las consecuencias de organizarlos de cierta manera.

Un patrón permite reutilizar **experiencia de diseño**: en lugar de resolver desde cero un problema conocido, podemos partir de una solución conceptual y adaptarla al contexto.

### 1.1. ¿Qué problemas resuelven?

Durante el diseño orientado a objetos aparecen problemas recurrentes:

- ¿Cómo crear objetos sin acoplar el código cliente a clases concretas?
- ¿Cómo permitir que un comportamiento varíe sin modificar la clase que lo utiliza?
- ¿Cómo integrar dos componentes cuyas interfaces son incompatibles?
- ¿Cómo agregar funcionalidades sin crear una gran cantidad de subclases?
- ¿Cómo permitir que varios objetos reaccionen a un cambio sin que el emisor conozca los detalles de cada receptor?

Los patrones ofrecen formas conocidas de abordar estas dificultades.

### 1.2. ¿Qué NO es un patrón?

- No es una regla que deba aplicarse siempre.
- No garantiza automáticamente buena calidad.
- No reemplaza el análisis de requerimientos y restricciones.
- No determina por sí solo una arquitectura completa.
- No equivale a una librería, un framework o una tecnología específica.

Un patrón puede mejorar un aspecto del diseño y perjudicar otro. Por ejemplo, desacoplar objetos puede facilitar la modificación, pero también aumentar la cantidad de interfaces, clases y relaciones que una persona debe comprender.

**Principio fundamental:** un patrón es útil cuando el problema que resuelve y sus beneficios justifican los costes que introduce.

---

## 2. Cómo se describe un patrón

El GoF utiliza una estructura para describir patrones. Estos son los elementos principales que conviene reconocer al estudiarlos.

| Elemento | Qué significa |
|---|---|
| **Nombre e intención** | Identifica el patrón y resume qué busca conseguir. |
| **Motivación** | Presenta una situación que permite comprender el problema y la necesidad de la solución. |
| **Aplicabilidad** | Describe cuándo tiene sentido utilizarlo. |
| **Estructura** | Representa los elementos participantes y sus relaciones, habitualmente mediante UML. |
| **Participantes** | Explica las responsabilidades de las clases u objetos que forman parte de la solución. |
| **Colaboraciones** | Describe cómo interactúan los participantes para cumplir el objetivo. |
| **Consecuencias** | Analiza beneficios, costes y compromisos. |
| **Implementación** | Discute cuestiones prácticas para llevar el patrón al código. |
| **Usos conocidos y patrones relacionados** | Presenta aplicaciones y conexiones con otras soluciones. |

No todos los patrones necesitan exactamente el mismo razonamiento de implementación. Esta estructura es una guía para comprenderlos, no una lista de casilleros que hay que completar mecánicamente.

### 2.1. Participantes y estructura

**Participantes no significa necesariamente clases concretas.** Son roles dentro de la solución. Una clase puede asumir más de un rol y un rol puede tener distintas implementaciones.

**La estructura no alcanza para entender un patrón.** Dos patrones pueden tener diagramas superficialmente parecidos, pero resolver problemas diferentes. Hay que entender su intención y sus colaboraciones.

Por ejemplo, Adapter y Decorator pueden utilizar un objeto que envuelve a otro. Sin embargo:

- **Adapter** cambia la interfaz que ve el cliente.
- **Decorator** conserva una interfaz compatible y agrega responsabilidades.

---

## 3. Clasificación de los patrones GoF

El catálogo contiene **23 patrones**, organizados en tres familias:

| Familia | Cantidad | Propósito |
|---|---:|---|
| **Creacionales** | 5 | Abordan la creación de objetos y el desacoplamiento entre su construcción y su utilización. |
| **Estructurales** | 7 | Abordan la composición y las relaciones entre clases y objetos. |
| **De comportamiento** | 11 | Abordan la distribución de responsabilidades, la comunicación y la organización de algoritmos. |
| **Total** | **23** | |

La clasificación expresa el propósito principal de cada patrón, no todos sus posibles efectos sobre el diseño. Un patrón creacional puede favorecer la modificabilidad; uno estructural puede facilitar la integración; y uno de comportamiento puede permitir cambiar una política de negocio sin alterar el código que la utiliza.

---

## 4. Patrones creacionales

Los patrones creacionales abordan decisiones relacionadas con la construcción y selección de objetos.

### 4.1. Abstract Factory — Fábrica abstracta

**Intención:** proporcionar una interfaz para crear familias de objetos relacionados o compatibles sin especificar sus clases concretas.

**Problema típico:** una aplicación soporta distintos conjuntos de componentes y cada conjunto debe mantener coherencia entre sus elementos.

**Ejemplo:** una aplicación necesita crear objetos compatibles con distintos proveedores de servicios. Una fábrica concreta puede crear el conjunto de objetos correspondiente a cada integración.

**Consecuencias:**

- Facilita cambiar de familia de productos.
- Reduce la dependencia de clases concretas.
- Agregar un nuevo tipo de producto a todas las familias puede requerir modificar las fábricas.

### 4.2. Builder — Constructor

**Intención:** separar la construcción de un objeto complejo de su representación, de modo que el mismo proceso pueda construir distintas representaciones.

**Problema típico:** un objeto requiere varios pasos de construcción, combinaciones de opciones o reglas de configuración.

**Ejemplo:** construir un itinerario complejo con distintos tipos de actividades, validaciones y opciones.

**Consecuencias:**

- Permite controlar el proceso de construcción.
- Separa responsabilidades.
- Introduce colaboradores adicionales.

### 4.3. Factory Method — Método fábrica

**Intención:** definir una interfaz para crear un objeto, dejando que las subclases decidan qué clase concreta instanciar.

**Problema típico:** una clase necesita crear objetos, pero no debería fijar de antemano la clase concreta que utilizará.

**Ejemplo:** una clase base de importación define cómo se procesa un archivo, mientras que las subclases determinan qué analizador concreto crear.

**Consecuencias:**

- Reduce la dependencia de clases concretas.
- Permite delegar decisiones de creación.
- Puede introducir jerarquías de clases y extender la creación mediante herencia.

### 4.4. Prototype — Prototipo

**Intención:** especificar los tipos de objetos a crear mediante un prototipo y crear nuevos objetos copiando uno existente.

**Problema típico:** crear una instancia desde una configuración existente resulta más conveniente que reconstruirla desde cero o depender de su clase concreta.

**Ejemplo:** duplicar una plantilla de actividad de viaje con sus propiedades iniciales y luego personalizar la copia.

**Consecuencias:**

- Puede simplificar la creación de objetos configurados.
- Requiere definir cuidadosamente qué significa copiar.
- Hay que considerar copias superficiales, profundas y referencias compartidas.

### 4.5. Singleton — Instancia única

**Intención:** asegurar que una clase tenga una única instancia y proporcionar un punto de acceso global a ella.

**Problema típico:** existe una necesidad real de coordinar el acceso a una única instancia de un recurso o servicio.

**Ejemplo:** un objeto que administra una configuración compartida en una aplicación, siempre que su unicidad esté realmente justificada.

**Consecuencias:**

- Controla la cantidad de instancias.
- El acceso global puede ocultar dependencias.
- Puede complicar las pruebas.
- No resuelve automáticamente los problemas de concurrencia.

### 4.6. Diferencias entre los creacionales

| Comparación | Diferencia principal |
|---|---|
| **Abstract Factory vs. Factory Method** | Abstract Factory crea familias de productos relacionados; Factory Method delega la elección del producto concreto mediante un método que pueden redefinir las subclases. |
| **Builder vs. Abstract Factory** | Builder se centra en el proceso de construcción y la representación resultante; Abstract Factory se centra en familias de productos. |
| **Prototype vs. Factory Method** | Prototype crea objetos copiando prototipos; Factory Method delega la creación a implementaciones concretas. |
| **Singleton vs. los demás** | Su objetivo distintivo es restringir la instancia y proporcionar acceso a ella. |

---

## 5. Patrones estructurales

Los patrones estructurales abordan la composición de clases y objetos.

### 5.1. Adapter — Adaptador

**Intención:** convertir la interfaz de una clase en otra que esperan los clientes, permitiendo colaborar a clases que de otro modo serían incompatibles.

**Problema típico:** integrar una API externa con una interfaz distinta de la que espera el sistema.

**Ejemplo:** un proveedor externo ofrece `crearBooking()` con sus propios tipos, mientras que el sistema necesita una interfaz `crearReserva()`. El adaptador traduce entre ambos contratos.

**Consecuencias:**

- Facilita la integración.
- Aísla incompatibilidades.
- Agrega una capa de traducción que debe mantenerse.

### 5.2. Bridge — Puente

**Intención:** desacoplar una abstracción de su implementación para que ambas puedan variar independientemente.

**Problema típico:** existen dos dimensiones de variación y combinarlas mediante herencia produciría demasiadas subclases.

**Ejemplo:** un sistema de notificaciones distingue entre tipos de notificación y mecanismos de entrega. La abstracción puede trabajar con distintas implementaciones de envío.

**Consecuencias:**

- Permite variar independientemente la abstracción y la implementación.
- Evita combinaciones innecesarias de subclases.
- Introduce una estructura más elaborada.

### 5.3. Composite — Compuesto

**Intención:** componer objetos en estructuras de árbol y permitir que los clientes traten uniformemente los objetos individuales y las composiciones.

**Problema típico:** una estructura jerárquica contiene elementos simples y grupos de elementos.

**Ejemplo:** un itinerario contiene actividades individuales y grupos de actividades; ciertas operaciones pueden aplicarse tanto a un elemento como a una composición.

**Consecuencias:**

- Simplifica el tratamiento de estructuras jerárquicas.
- Puede complicar las restricciones sobre qué tipos de elementos puede contener cada composición.

### 5.4. Decorator — Decorador

**Intención:** agregar responsabilidades a un objeto dinámicamente, proporcionando una alternativa flexible a la extensión mediante subclases.

**Problema típico:** se necesita agregar funcionalidad opcional sin modificar la clase original ni crear numerosas subclases.

**Ejemplo:** envolver un servicio de consulta para agregar medición de tiempos o registro de operaciones sin modificar su implementación principal.

**Consecuencias:**

- Permite combinar responsabilidades.
- Evita algunas jerarquías de herencia.
- Una cadena larga de decoradores puede dificultar el diagnóstico y la comprensión del comportamiento final.

### 5.5. Facade — Fachada

**Intención:** proporcionar una interfaz unificada y simplificada para un conjunto de interfaces de un subsistema.

**Problema típico:** un cliente debe interactuar con demasiados detalles internos de un subsistema.

**Ejemplo:** un servicio de preparación de viaje ofrece una operación de alto nivel que coordina reservas, validaciones y consultas internas.

**Consecuencias:**

- Reduce la complejidad que ve el cliente.
- Disminuye la dependencia de los detalles internos.
- Una fachada mal diseñada puede concentrar demasiadas responsabilidades.

### 5.6. Flyweight — Peso ligero

**Intención:** utilizar compartición para soportar eficientemente grandes cantidades de objetos de grano fino.

**Problema típico:** existen muchísimos objetos similares y el consumo de memoria resulta importante.

**Ejemplo:** una aplicación con numerosas representaciones similares comparte información invariable y mantiene por separado los datos particulares de cada instancia.

**Consecuencias:**

- Puede reducir el consumo de memoria.
- Obliga a distinguir entre estado intrínseco compartido y estado extrínseco específico de cada uso.

### 5.7. Proxy — Apoderado o sustituto

**Intención:** proporcionar un sustituto o representante de otro objeto para controlar el acceso a él.

**Problema típico:** se necesita controlar el acceso, retrasar la inicialización o representar un objeto remoto.

**Ejemplo:** un objeto representante retrasa la carga de un recurso costoso hasta que se necesita, o controla el acceso a un servicio remoto.

**Consecuencias:**

- Permite controlar acceso e inicialización.
- Puede facilitar la interacción con recursos remotos.
- Puede añadir latencia y ocultar costes de operación.

### 5.8. Diferencias entre los estructurales

| Comparación | Diferencia principal |
|---|---|
| **Adapter vs. Facade** | Adapter adapta una interfaz a otra; Facade simplifica el acceso a un subsistema. |
| **Adapter vs. Bridge** | Adapter hace compatibles interfaces existentes; Bridge organiza desde el diseño dos dimensiones que deben variar independientemente. |
| **Decorator vs. Proxy** | Decorator agrega responsabilidades conservando una interfaz compatible; Proxy representa otro objeto y controla el acceso a él. |
| **Composite vs. Decorator** | Composite organiza objetos en jerarquías de partes y conjuntos; Decorator envuelve un objeto para agregarle responsabilidades. |
| **Facade vs. Mediator** | Facade simplifica la interfaz hacia un subsistema; Mediator organiza la interacción entre colegas que colaboran. |

---

## 6. Patrones de comportamiento

Los patrones de comportamiento se centran en algoritmos, comunicación y distribución de responsabilidades.

### 6.1. Chain of Responsibility — Cadena de responsabilidad

**Intención:** evitar acoplar el emisor de una petición a su receptor, dando a varios objetos la posibilidad de manejarla.

**Problema típico:** distintos objetos pueden atender una petición y no se quiere fijar un único receptor.

**Ejemplo:** una solicitud pasa por validaciones de formato, permisos y reglas de negocio, cada una representada por un manejador.

**Consecuencias:**

- Desacopla el emisor de los receptores.
- Permite reorganizar los manejadores.
- No garantiza que una petición sea atendida; depende de cómo se configure la cadena.

### 6.2. Command — Comando

**Intención:** encapsular una petición como un objeto, permitiendo parametrizar clientes con distintas peticiones y encolar o registrar solicitudes.

**Problema típico:** una operación necesita representarse como una entidad independiente.

**Ejemplo:** representar "cancelar reserva" como una operación que puede ejecutarse, registrarse o incorporarse a una cola.

**Consecuencias:**

- Separa quien solicita una acción de quien la ejecuta.
- Facilita registrar o encolar operaciones.
- No hace que cualquier operación sea reversible automáticamente.

### 6.3. Interpreter — Intérprete

**Intención:** definir una representación de la gramática de un lenguaje y un intérprete para evaluar expresiones de ese lenguaje.

**Problema típico:** se necesita interpretar un lenguaje sencillo o una gramática específica.

**Ejemplo:** interpretar expresiones simples de búsqueda o filtros definidos por el usuario.

**Consecuencias:**

- Facilita representar y ampliar gramáticas sencillas.
- Una gramática compleja puede hacer que el conjunto de clases crezca demasiado.

### 6.4. Iterator — Iterador

**Intención:** proporcionar una forma de acceder secuencialmente a los elementos de una colección sin exponer su representación subyacente.

**Problema típico:** recorrer una colección sin conocer cómo están almacenados sus elementos.

**Ejemplo:** recorrer las actividades de un itinerario sin conocer si están almacenadas en una lista, un árbol u otra estructura.

**Consecuencias:**

- Separa el recorrido de la estructura de almacenamiento.
- Hay que definir qué ocurre si la colección cambia durante la iteración.

### 6.5. Mediator — Mediador

**Intención:** definir un objeto que encapsula cómo interactúa un conjunto de objetos, reduciendo las referencias directas entre ellos.

**Problema típico:** muchos objetos se conocen entre sí y sus dependencias se vuelven difíciles de mantener.

**Ejemplo:** un coordinador organiza la interacción entre componentes de una interfaz o entre colaboradores de un flujo de trabajo.

**Consecuencias:**

- Reduce dependencias entre colegas.
- El mediador puede convertirse en un componente demasiado complejo si concentra toda la lógica.

### 6.6. Memento — Recuerdo

**Intención:** capturar y externalizar el estado interno de un objeto para poder restaurarlo después, sin exponer los detalles de su representación.

**Problema típico:** se necesita recuperar un estado anterior.

**Ejemplo:** guardar el estado anterior de un editor para permitir recuperar una versión previa.

**Consecuencias:**

- Facilita la restauración de estados.
- Puede consumir memoria.
- Requiere definir qué estado debe preservarse.

### 6.7. Observer — Observador

**Intención:** definir una dependencia de uno a muchos de modo que, cuando un objeto cambia de estado, sus dependientes sean notificados y puedan actualizarse.

**Problema típico:** varios objetos necesitan reaccionar a cambios sin quedar fuertemente acoplados al emisor.

**Ejemplo:** cuando cambia el estado de una reserva, varios elementos interesados actualizan su representación.

**Consecuencias:**

- Reduce la dependencia directa entre emisor y observadores.
- Puede dificultar el seguimiento de las notificaciones.
- El orden de actualización y la gestión de errores requieren atención.

### 6.8. State — Estado

**Intención:** permitir que un objeto altere su comportamiento cuando cambia su estado interno, dando la impresión de que cambia de clase.

**Problema típico:** el comportamiento depende del estado y existen muchos condicionales para decidir qué hacer.

**Ejemplo:** una reserva tiene distintos estados y las operaciones disponibles varían según esté pendiente, confirmada o cancelada.

**Consecuencias:**

- Organiza comportamientos asociados a estados.
- Reduce condicionales dispersos.
- Introduce clases de estado y requiere controlar las transiciones.

### 6.9. Strategy — Estrategia

**Intención:** definir una familia de algoritmos, encapsular cada uno y hacerlos intercambiables.

**Problema típico:** una operación puede ejecutarse mediante distintas políticas o algoritmos.

**Ejemplo:** seleccionar distintos algoritmos de ordenamiento o de cálculo de costes para un itinerario mediante una interfaz común.

**Consecuencias:**

- Facilita variar algoritmos sin modificar el cliente.
- Puede introducir más clases.
- Alguien debe seleccionar la estrategia adecuada.

### 6.10. Template Method — Método plantilla

**Intención:** definir el esqueleto de un algoritmo en una operación y delegar algunos pasos a las subclases, preservando el orden general del proceso.

**Problema típico:** varios procesos comparten una estructura general, pero algunos pasos varían.

**Ejemplo:** distintos procesos de importación siguen las etapas de leer, validar y guardar, pero implementan de forma diferente la lectura de cada formato.

**Consecuencias:**

- Reutiliza el flujo común.
- Facilita variar pasos específicos.
- Acopla las variantes a una jerarquía de herencia.

### 6.11. Visitor — Visitante

**Intención:** representar una operación que se ejecuta sobre elementos de una estructura de objetos, permitiendo agregar nuevas operaciones sin incorporar el comportamiento a cada clase de elemento.

**Problema típico:** hay que agregar nuevas operaciones a una estructura de clases relativamente estable.

**Ejemplo:** aplicar distintas operaciones, como generar un informe o exportar información, sobre varios tipos de elementos de un modelo.

**Consecuencias:**

- Facilita agregar operaciones cuando la estructura de elementos es estable.
- Agregar nuevos tipos de elementos puede exigir modificar los visitantes.

### 6.12. Diferencias entre los patrones de comportamiento

| Comparación | Diferencia principal |
|---|---|
| **Strategy vs. State** | Strategy permite elegir entre algoritmos alternativos; State organiza el comportamiento que depende del estado interno y de sus transiciones. |
| **Strategy vs. Template Method** | Strategy utiliza composición para intercambiar algoritmos; Template Method utiliza herencia para variar pasos de un algoritmo común. |
| **Observer vs. Mediator** | Observer notifica cambios a dependientes; Mediator centraliza cómo interactúan varios objetos. |
| **Command vs. Strategy** | Command representa una petición como un objeto; Strategy representa un algoritmo intercambiable. |
| **Chain of Responsibility vs. Mediator** | Chain of Responsibility propaga una petición entre posibles manejadores; Mediator coordina interacciones entre colegas. |
| **Memento vs. Command** | Memento conserva estado; Command representa una operación. Pueden combinarse para implementar deshacer, pero cumplen funciones distintas. |

---

## 7. Relación entre patrones y tácticas

Esta sección es una **ampliación aplicada a arquitectura de software**. La relación que se presenta no constituye una clasificación original del GoF.

### 7.1. Conceptos que no hay que confundir

- **Atributo de calidad:** propiedad del sistema que nos interesa, como modificabilidad, disponibilidad, rendimiento o seguridad.
- **Táctica arquitectónica:** decisión de diseño que busca influir en una respuesta de calidad concreta.
- **Patrón de diseño:** solución reutilizable que organiza clases u objetos para resolver un problema de diseño.
- **Implementación:** código que materializa esa solución.

Un patrón puede ayudar a implementar una táctica, pero no es sinónimo de táctica. Una táctica tampoco determina necesariamente un patrón único.

### 7.2. Mapa de relaciones posibles

| Atributo de calidad | Intención táctica | Patrones GoF que pueden ayudar | Precaución |
|---|---|---|---|
| **Modificabilidad** | Encapsular variaciones y reducir dependencias. | Strategy, Adapter, Bridge, Factory Method, Abstract Factory. | Cada abstracción agrega estructura que también debe mantenerse. |
| **Testabilidad** | Aislar el objeto bajo prueba y controlar sus colaboradores. | Strategy, Adapter, Factory Method, Abstract Factory. | La sustitución debe estar permitida por el diseño. |
| **Integrabilidad** | Adaptar interfaces incompatibles y aislar proveedores. | Adapter, Facade, Bridge. | La compatibilidad semántica requiere más que traducir nombres y tipos. |
| **Extensibilidad** | Incorporar variantes o comportamientos nuevos con cambios localizados. | Strategy, Factory Method, Abstract Factory, Decorator, Visitor. | Cada patrón favorece determinadas formas de extensión y puede dificultar otras. |
| **Rendimiento** | Evitar trabajo repetido, limitar costes o compartir recursos. | Flyweight, Proxy; Decorator en algunos casos. | Ninguno garantiza por sí solo un aumento del rendimiento; hay que medirlo. |
| **Seguridad** | Interponer controles y restringir el acceso a operaciones. | Proxy. | Un Proxy no garantiza seguridad si los controles se pueden eludir o están mal implementados. |
| **Disponibilidad** | Organizar la reacción a cambios de estado o la coordinación ante eventos. | State, Observer o Chain of Responsibility en situaciones concretas. | La redundancia, la detección de fallos y la recuperación requieren mecanismos más amplios. |
| **Usabilidad** | Simplificar la interacción con funcionalidades complejas. | Facade, Command, Memento. | Son ayudas de diseño; no sustituyen la evaluación de la experiencia del usuario. |

**Importante:** la tabla muestra relaciones posibles, no equivalencias. Los patrones GoF no constituyen un catálogo de tácticas arquitectónicas y no existe una correspondencia uno a uno entre cada atributo de calidad y un patrón.

### 7.3. Ejemplo A: modificabilidad e intercambio de algoritmos

**Situación:** el sistema calcula el coste de un viaje y se prevé incorporar nuevas políticas de cálculo.

**Intención táctica:** encapsular la variación y reducir el impacto de incorporar un algoritmo nuevo.

**Patrón posible: Strategy.** Cada algoritmo implementa un contrato común y el código que solicita el cálculo no necesita conocer los detalles internos de cada variante.

**Trade-off:** agregamos clases y una decisión sobre qué estrategia usar. Si solo existe un algoritmo y no se prevén variaciones, la estructura puede no justificarse.

### 7.4. Ejemplo B: integrabilidad e incorporación de proveedores

**Situación:** un proveedor expone una API distinta de la interfaz que necesita el sistema.

**Intención táctica:** aislar la dependencia externa y encapsular la traducción entre interfaces.

**Patrón posible: Adapter.** El adaptador convierte las operaciones del contrato interno en llamadas al proveedor y traduce las respuestas.

**Trade-off:** la lógica central queda menos expuesta a la API externa, pero hay que mantener la traducción, los errores y las diferencias semánticas.

### 7.5. Ejemplo C: simplificar el acceso a un subsistema

**Situación:** un cliente necesita invocar varias operaciones internas en un orden determinado para preparar una reserva.

**Intención:** reducir la complejidad que el cliente debe conocer y limitar su dependencia de los detalles internos.

**Patrón posible: Facade.** Se ofrece una interfaz de alto nivel que coordina las operaciones internas.

**Trade-off:** simplifica el uso del subsistema, pero hay que evitar que la fachada se convierta en el lugar donde se acumule toda la lógica de negocio.

---

## 8. Cómo pasar de las tácticas a los patrones

Hasta las tácticas, podés razonar con conceptos relativamente abstractos: reducir dependencias, aislar fallos, controlar la concurrencia o separar responsabilidades.

Cuando llegás a patrones, empezás a decidir cómo se concretan esas intenciones mediante colaboradores con responsabilidades definidas.

La transición **no debería ser**:

> Necesito modificabilidad, entonces uso Strategy.

Debería ser:

> Necesito modificabilidad porque se esperan cambios frecuentes en una parte del comportamiento. Identifico qué parte varía, qué parte debe permanecer estable, quién debería depender de quién y qué mecanismos permiten aislar la variación. Strategy es una alternativa posible si el problema consiste en intercambiar algoritmos.

### 8.1. Método de razonamiento en seis pasos

1. **Identificar el driver.** Puede ser un escenario de calidad, un requerimiento funcional importante o una restricción.
2. **Precisar qué debe variar o qué problema debe resolverse.** ¿Varían los algoritmos, las clases concretas que se crean, las interfaces externas, las responsabilidades o el comportamiento según el estado?
3. **Identificar los elementos que tienen que colaborar.** Determinar quién solicita una operación, quién la realiza, quién selecciona una variante y quién conoce los detalles concretos.
4. **Buscar una solución apropiada.** Comparar patrones candidatos con el problema. También considerar una solución más simple que no use un patrón explícito.
5. **Evaluar consecuencias y alternativas.** ¿Qué dependencias desaparecen? ¿Cuáles aparecen? ¿Qué cambios quedan localizados? ¿Qué coste de comprensión o ejecución se agrega?
6. **Refinar el diseño.** Definir interfaces, responsabilidades, relaciones y, cuando aporte valor, diagramas de clases o de secuencia. Después implementar y probar.

Esta secuencia es una guía de razonamiento, no una nueva fase formal de ADD. Los patrones son herramientas que pueden aparecer durante el refinamiento de los elementos arquitectónicos.

---

## 9. Ejemplo aplicado a un sistema de viajes

Supongamos que el sistema debe permitir asociar reservas a itinerarios y que las reservas pueden provenir de proveedores externos.

Uno de los drivers es la modificabilidad: agregar un proveedor nuevo no debería obligar a modificar toda la lógica de reservas.

### 9.1. Del driver a la decisión de diseño

**Driver**

Agregar un proveedor nuevo debe requerir cambios localizados.

**Problema de diseño**

Si el servicio de reservas contiene condicionales y llamadas específicas para cada proveedor, cada nueva integración aumenta el acoplamiento y el riesgo de modificar lógica existente.

**Intención táctica**

Encapsular las diferencias entre proveedores y hacer que el servicio de reservas dependa de un contrato estable.

**Alternativa de diseño**

Definir una interfaz común para los proveedores y aislar las llamadas particulares detrás de adaptadores.

### 9.2. ¿Qué patrones considerar?

- **Adapter:** traduce la interfaz común a la API de cada proveedor.
- **Factory Method o una fábrica simple:** si necesitamos seleccionar y construir la implementación apropiada.
- **Strategy:** si además existen algoritmos intercambiables, como distintas políticas para seleccionar un proveedor.

No necesariamente necesitamos los tres. La elección depende de qué variaciones existen realmente.

### 9.3. Estructura conceptual

```text
                 Servicio de reservas
                          |
                          v
               Interfaz común del proveedor
                          |
                 +--------+--------+
                 |                 |
                 v                 v
             Adaptador A       Adaptador B
                 |                 |
                 v                 v
             Proveedor A       Proveedor B
```

La decisión importante no es que existan cuatro cajas. Es que **el servicio de reservas no dependa directamente de los detalles particulares de cada proveedor**.

### 9.4. Posible interfaz de implementación

```java
interface ProveedorReservas {
    Reserva crearReserva(SolicitudReserva solicitud);
    EstadoReserva consultarEstado(String idReserva);
}
```

Los adaptadores implementarían esa interfaz, traduciendo los datos y las operaciones al formato de cada proveedor. El servicio de reservas dependería de `ProveedorReservas`, no de `ProveedorAAdapter` ni de `ProveedorBAdapter`.

Este es un ejemplo ilustrativo de implementación, no una especificación obligatoria de la arquitectura.

### 9.5. Beneficios y costes

| Beneficio esperado | Coste o riesgo |
|---|---|
| Agregar proveedores sin reescribir la lógica central. | Más interfaces, clases y configuración. |
| Probar el servicio con un proveedor simulado. | Hay que mantener contratos y adaptadores coherentes. |
| Aislar las particularidades de cada API externa. | El adaptador puede complicarse si los proveedores difieren mucho. |

---

## 10. Cómo documentar las decisiones en ADD

Los patrones no son un paso obligatorio e independiente de ADD. Se utilizan cuando una decisión de diseño necesita una solución conocida y el patrón resulta apropiado.

En cada iteración, conviene registrar el razonamiento.

### 10.1. Qué documentar

| Artefacto | Qué debería mostrar |
|---|---|
| **Escenario de calidad** | Estímulo, contexto, respuesta y medida de éxito esperada. |
| **Justificación de iteración ADD** | Por qué se eligieron esos drivers y qué elementos se van a refinar. |
| **Vista de componentes y conectores** | Componentes principales e interacciones; puede mostrar dónde se implementa una táctica. |
| **Vista de módulos o clases** | Responsabilidades, interfaces, dependencias y colaboraciones que concretan el diseño. |
| **ADR** | Decisión significativa, alternativas evaluadas y consecuencias. |
| **Código y pruebas** | Realización concreta del diseño y evidencia de su comportamiento. |

No todo patrón de diseño merece un ADR. Si la decisión es local, reversible y no afecta de manera importante a la arquitectura, puede bastar con documentarla en el código o en el diseño detallado.

El criterio es la importancia de la decisión, no el hecho de haber utilizado un patrón.

### 10.2. Ejemplo de registro de decisión

- **Driver:** escenario de modificabilidad relativo a incorporar proveedores.
- **Elemento a refinar:** componente o módulo responsable de gestionar reservas.
- **Problema:** dependencia directa entre la lógica de reservas y las API externas.
- **Alternativas:** llamadas directas, interfaz común con adaptadores u otra solución.
- **Decisión:** aislar los proveedores mediante un contrato común y adaptadores.
- **Consecuencias:** cambios más localizados y pruebas más sencillas; a cambio, más abstracciones y código de integración.
- **Validación:** incorporar un proveedor simulado o nuevo y verificar que la lógica central no necesita cambios, salvo los puntos de configuración o selección definidos.

El diagrama de componentes puede mostrar la separación a nivel arquitectónico; el diagrama de clases puede detallar los roles de Adapter.

---

## 11. Cómo estudiar los patrones

Para estudiar cada patrón, intentá responder estas preguntas:

1. **Problema:** ¿qué dificultad concreta aparece?
2. **Intención:** ¿qué busca conseguir?
3. **Estructura:** ¿qué roles participan y cómo colaboran?
4. **Calidad:** ¿qué atributo puede favorecer y cuáles son los costes?
5. **Elección:** ¿cuándo lo usarías y cuándo sería innecesario?
6. **Conexión con tácticas:** ¿qué táctica podría ayudar a materializar y por qué?

No hace falta memorizar los 23 patrones con el mismo nivel de profundidad desde el primer día. Para practicar el razonamiento, conviene comenzar con:

- **Strategy:** variación de algoritmos.
- **Adapter:** integración de interfaces incompatibles.
- **Observer:** notificación de cambios.
- **Factory Method:** creación de objetos concretos.
- **Facade:** simplificación del acceso a subsistemas.
- **Decorator:** incorporación flexible de responsabilidades.
- **State:** comportamiento dependiente del estado.
- **Command:** representación de peticiones como objetos.

Estos patrones permiten practicar problemas diferentes de diseño y aprender a justificar decisiones.

### 11.1. Preguntas para autoevaluarte

- ¿En qué se diferencian Adapter y Facade?
- ¿Por qué Strategy puede favorecer la modificabilidad?
- ¿Qué diferencia existe entre Strategy y State?
- ¿Por qué Singleton puede complicar las pruebas?
- ¿Cuándo preferirías Builder en lugar de Abstract Factory?
- ¿Qué relación existe entre un patrón de diseño y una táctica arquitectónica?
- ¿Por qué no conviene elegir un patrón solamente porque aparece asociado a un atributo de calidad?
- ¿Cuándo una decisión basada en un patrón merece un ADR?

---

## 12. Síntesis final

Los patrones GoF representan soluciones a problemas recurrentes de diseño orientado a objetos. Sus beneficios dependen del contexto en el que se aplican.

- **Creacionales:** cómo crear objetos y desacoplar su construcción de su uso.
- **Estructurales:** cómo componer objetos y clases.
- **De comportamiento:** cómo distribuir responsabilidades, organizar algoritmos y coordinar interacciones.

Para relacionarlos con las tácticas, no memorices equivalencias. Identificá primero la calidad que querés favorecer, después la variación o dependencia que necesitás controlar y finalmente el patrón que podría resolver ese problema.

Para relacionarlos con ADD, recordá que los patrones pueden aparecer durante el refinamiento de un elemento arquitectónico. Si una decisión requiere detallar cómo colaboran objetos, un diagrama de clases puede ser útil; si la decisión afecta a la estructura del sistema, probablemente también necesites reflejarla en una vista arquitectónica.

**La idea central es que no tenés que saltar de una táctica a una clase.** Entre ambas hay decisiones de diseño que justifican las responsabilidades, interfaces y relaciones. Los patrones son herramientas para resolver esas decisiones, no un paso que debas completar mecánicamente.

### Bibliografía principal

Gamma, E., Helm, R., Johnson, R. y Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

El catálogo y sus tres familias corresponden al GoF. Las relaciones con atributos de calidad, tácticas y ADD constituyen una ampliación aplicada para conectar el diseño orientado a objetos con la arquitectura de software.

