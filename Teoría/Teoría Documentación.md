# Documentación de arquitecturas de software

## Introducción

La **documentación arquitectónica** permite comunicar, comprender, analizar y mantener las decisiones y estructuras de un sistema.

Como la arquitectura tiene múltiples dimensiones, ningún documento o diagrama alcanza para describirla por completo. Es necesario utilizar distintas perspectivas y artefactos, según qué se quiera comunicar y quién necesite esa información.

---

## 1. Vistas arquitectónicas

### ¿Qué es una vista arquitectónica?

Una **vista arquitectónica** representa una perspectiva particular de la arquitectura, elegida para responder determinadas preguntas.

Cada vista muestra los elementos y las relaciones relevantes para un propósito específico.

### Tipos de vistas

| Vista | ¿Qué documenta? | ¿Para qué sirve? |
|---|---|---|
| **Módulos** | Organización estática del código: módulos, paquetes, capas y dependencias. | Construcción, mantenibilidad, análisis del impacto de cambios y testing. |
| **Componentes y conectores (C&C)** | Elementos en ejecución, sus responsabilidades e interacciones. | Analizar rendimiento, disponibilidad y comunicación. |
| **Asignación (*Allocation*)** | Relación entre el software y su entorno: infraestructura, nodos, equipos, etc. | Analizar despliegue, seguridad, rendimiento y disponibilidad. |

### 1.1. Vista de módulos

Representa cómo se organiza el software desde una perspectiva estática.

Puede mostrar:
- Módulos y paquetes.
- Capas.
- Dependencias entre módulos.
- Organización de las responsabilidades.

**Pregunta que responde:** ¿Cómo está organizado el código y qué dependencias existen entre sus partes?

### 1.2. Vista de componentes y conectores (C&C)

Representa los elementos que interactúan durante la ejecución del sistema y los mecanismos mediante los cuales se comunican.

Puede mostrar:
- Componentes en ejecución.
- Responsabilidades de cada componente.
- Conectores y mecanismos de comunicación.
- Interacciones entre componentes.

**Pregunta que responde:** ¿Qué elementos interactúan durante la ejecución y cómo se comunican?

### 1.3. Vista de asignación (*Allocation*)

Representa la relación entre los elementos de software y los elementos de su entorno.

Puede mostrar:
- Nodos de infraestructura.
- Distribución de componentes.
- Relación entre software y hardware.
- Asignación a entornos o equipos, según el propósito de la vista.

**Pregunta que responde:** ¿Dónde se ejecuta cada parte del sistema y cómo se relaciona con su entorno?

### 1.4. Relación entre las vistas

Una arquitectura puede necesitar varias vistas porque cada una muestra aspectos diferentes.

Además, las vistas no tienen por qué corresponderse una a una: **un módulo de código no necesariamente equivale a un único componente en ejecución**.

Por ejemplo, un módulo puede contribuir a varios componentes de ejecución, o varios módulos pueden formar parte de un mismo componente.

También se puede documentar el comportamiento mediante diagramas de secuencia, actividad, estados y casos de uso, entre otros.

> **Idea clave:** las vistas son perspectivas complementarias de una misma arquitectura, no descripciones independientes de sistemas diferentes.

---

## 2. Estrategias de documentación

La estrategia de documentación depende de dos factores:

1. Qué tan fácil es compartir la documentación.
2. Qué tan difícil es modificarla.

### Estrategias

| Estrategia | Característica | Interpretación |
|---|---|---|
| **Tribal** | Conocimiento informal, transmitido entre personas. | Fácil de cambiar, difícil de compartir. |
| **Communal** | Documentación compartida y fácil de actualizar. | Estado deseable para el trabajo cotidiano de un equipo. |
| **Formal** | Documentación estructurada, controlada y costosa de modificar. | Se utiliza cuando el contexto lo exige. |
| **Waste of Time** | Documentación difícil de compartir y de mantener. | Situación que se busca evitar. |

### ¿Qué conviene recordar?

El objetivo no es documentar absolutamente todo, sino documentar **lo necesario para la audiencia adecuada, con un costo de mantenimiento razonable**.

La documentación debe aportar valor: facilitar la comunicación, conservar decisiones relevantes y permitir comprender la arquitectura.

---

## 3. Architecture Haiku

### ¿Qué es?

Un **Architecture Haiku** es un resumen muy breve de la arquitectura, generalmente de una página.

### ¿Qué contiene?

Sintetiza los aspectos principales de la arquitectura, como:

- Objetivos del negocio.
- Atributos de calidad prioritarios.
- Patrones arquitectónicos.
- Decisiones principales y su justificación.

### ¿Cuándo se utiliza?

Cuando se necesita comunicar rápidamente la idea general de la arquitectura y mantener una visión compartida entre las personas involucradas.

### Idea clave

El Haiku **resume la arquitectura, pero no reemplaza la documentación detallada**.

Es útil para comprender rápidamente la dirección general del diseño sin tener que leer todos los documentos arquitectónicos.

---

## 4. Architecture Decision Records (ADR)

### ¿Qué son?

Los **Architecture Decision Records (ADR)** son registros que documentan una decisión arquitectónica significativa y el razonamiento detrás de ella.

Su objetivo es conservar la justificación de las decisiones y mantener su trazabilidad histórica.

### ¿Cómo se documentan?

Habitualmente, se utiliza un archivo Markdown por decisión.

Un ADR puede contener las siguientes secciones:

| Sección | Contenido |
|---|---|
| **Título** | Identificador y descripción de la decisión. |
| **Contexto** | Problema y circunstancias relevantes que motivan la decisión. |
| **Decisión** | Alternativa elegida. |
| **Estado** | Situación de la decisión: propuesta, aceptada, reemplazada, etc. |
| **Consecuencias** | Beneficios, costos y efectos negativos derivados de la decisión. |

### ¿Cuándo se crea un ADR?

Cuando se toma una decisión arquitectónica importante que conviene conservar y justificar.

No toda decisión de implementación necesita un ADR. Se utiliza principalmente para decisiones significativas que afectan la estructura, las propiedades o la evolución del sistema.

### Ejemplo

Supongamos que un sistema debe integrar distintos proveedores externos de reservas.

Una decisión arquitectónica consiste en definir una interfaz común y utilizar adaptadores para cada proveedor.

El ADR podría registrar:

- **Contexto:** se necesita integrar proveedores con APIs diferentes.
- **Decisión:** definir una interfaz común y encapsular las diferencias en adaptadores.
- **Consecuencias positivas:** se reduce el impacto de cambiar o incorporar proveedores.
- **Consecuencias negativas:** se agrega una capa de abstracción y mantenimiento.

### ¿Qué pasa si cambia una decisión?

Si una decisión cambia, se registra su reemplazo sin perder el registro anterior. De esta manera, el equipo puede comprender qué se decidió, por qué se hizo y cómo evolucionó la arquitectura.

> **Idea clave:** un ADR explica qué se decidió y por qué. No es solamente una descripción de la solución final.

---

## 5. Views & Beyond

### ¿Qué es?

**Views & Beyond** es un enfoque para organizar la documentación de una arquitectura mediante vistas y documentación complementaria.

Parte de la idea de que las vistas son esenciales, pero necesitan explicaciones y relaciones que permitan comprender la arquitectura en conjunto.

### ¿Qué incluye?

Suele contemplar:

- **Descripción general del sistema:** contexto y propósito.
- **Vistas arquitectónicas:** representación de las estructuras relevantes y explicación de sus elementos.
- **Relaciones entre vistas:** correspondencias y dependencias entre distintas perspectivas.
- **Trazabilidad entre arquitectura y requerimientos:** relación entre decisiones arquitectónicas y necesidades del sistema.
- **Justificación de las decisiones:** motivos y criterios detrás del diseño.
- **Guía para navegar la documentación:** organización que permita encontrar la información necesaria.

### ¿Cuándo se utiliza?

Cuando se necesita describir la arquitectura de forma sistemática para distintos *stakeholders*, como desarrolladores, responsables técnicos, responsables del negocio u otras personas interesadas.

### Idea clave

Los diagramas por sí solos no alcanzan. También hay que explicar los elementos, sus responsabilidades y las relaciones relevantes.

Views & Beyond permite organizar las distintas vistas y la información complementaria para que la documentación resulte coherente y útil.

---

## 6. High-Level Design (HLD)

### ¿Qué es?

Un documento de **High-Level Design (HLD)** registra un conjunto de decisiones de diseño relacionadas para una parte del sistema, a alto nivel.

Su propósito es comunicar cómo se piensa resolver una funcionalidad o problema importante sin llegar todavía al detalle completo de implementación.

### Estructura habitual

#### 1. Description

Describe el contexto funcional y del dominio.

Puede incluir:
- El problema que se quiere resolver.
- La funcionalidad involucrada.
- El contexto relevante para comprender el diseño.

#### 2. Solution Design

Presenta las decisiones de diseño, su justificación y las vistas relevantes.

Puede incluir:
- Componentes y responsabilidades.
- Interacciones entre componentes.
- Decisiones arquitectónicas.
- Diagramas necesarios para comprender la solución.

#### 3. Quality-Attribute Analysis

Explica cómo se abordan los atributos de calidad y con qué evidencia.

Puede incluir:
- Atributos de calidad relevantes.
- Escenarios que debe satisfacer la solución.
- Decisiones que contribuyen a satisfacerlos.
- Trade-offs y limitaciones identificadas.

#### 4. Issues

Registra las incertidumbres, los supuestos y las cuestiones pendientes.

Puede incluir:
- Decisiones que todavía deben tomarse.
- Supuestos que necesitan validación.
- Riesgos o problemas sin resolver.

### ¿Cuándo se utiliza?

Cuando hay que comunicar el diseño general de una funcionalidad o parte importante del sistema.

### Idea clave

El HLD **no es diseño detallado**. Es un documento vivo que debe actualizarse cuando cambian las decisiones o los supuestos que las sustentan.

---

## 7. Diferencias entre los artefactos

Cada artefacto responde una pregunta distinta.

| Artefacto | Pregunta que responde |
|---|---|
| **Vista arquitectónica** | ¿Cómo está estructurado o cómo se comporta el sistema desde una perspectiva? |
| **Architecture Haiku** | ¿Cuál es la idea general de la arquitectura? |
| **ADR** | ¿Qué decisión se tomó y por qué? |
| **HLD** | ¿Cómo se diseña, a alto nivel, una parte del sistema y qué decisiones involucra? |
| **Views & Beyond** | ¿Cómo organizamos una descripción arquitectónica completa mediante vistas y sus relaciones? |

### Forma rápida de memorizarlo

- **Vista:** muestra una estructura o perspectiva.
- **Haiku:** resume la arquitectura.
- **ADR:** registra y justifica una decisión.
- **HLD:** reúne decisiones relacionadas para diseñar una parte del sistema a alto nivel.
- **Views & Beyond:** organiza la documentación arquitectónica mediante vistas y documentación complementaria.

---

## 8. Cómo se complementan en un proyecto

Estos artefactos no son alternativas excluyentes: pueden utilizarse juntos porque resuelven necesidades diferentes.

Por ejemplo, en un proyecto desarrollado mediante ADD:

1. Se identifican los drivers arquitectónicos y las necesidades del sistema.
2. Se seleccionan las decisiones relevantes durante las iteraciones de diseño.
3. Se registran las decisiones significativas mediante ADR.
4. Se actualizan las vistas arquitectónicas afectadas por las decisiones.
5. Se utiliza un HLD cuando hace falta explicar el diseño general de una parte importante del sistema.
6. Se organiza la documentación mediante un enfoque como Views & Beyond.
7. Se puede mantener un Architecture Haiku para comunicar rápidamente la visión general.

Este flujo es ilustrativo: no implica que todos los proyectos deban utilizar obligatoriamente todos los artefactos ni que exista un orden rígido para producirlos.

---

## 9. Lo que tenés que recordar para el examen

### Preguntas de autoevaluación

- ¿Por qué una única vista no alcanza para documentar toda la arquitectura?
- ¿Qué diferencia existe entre una vista de módulos y una vista de componentes y conectores?
- ¿Qué información aporta una vista de asignación?
- ¿Por qué un módulo no necesariamente equivale a un componente en ejecución?
- ¿Qué caracteriza a las estrategias Tribal, Communal, Formal y Waste of Time?
- ¿Qué es un Architecture Haiku y qué limitaciones tiene?
- ¿Qué información debe registrar un ADR?
- ¿Por qué conviene conservar un ADR reemplazado?
- ¿Qué aporta Views & Beyond más allá de los diagramas?
- ¿Qué diferencia existe entre un HLD y un ADR?
- ¿Cómo se complementan las vistas, los ADR y el HLD durante un proceso de diseño arquitectónico?

### Síntesis final

La documentación arquitectónica busca que las personas puedan comprender el sistema, analizar sus propiedades y conocer las razones detrás de las decisiones de diseño.

Para lograrlo, se utilizan artefactos complementarios:

- Las **vistas** representan perspectivas de la arquitectura.
- El **Haiku** comunica su idea general.
- Los **ADR** conservan las decisiones y su justificación.
- El **HLD** explica el diseño de una parte del sistema a alto nivel.
- **Views & Beyond** organiza las vistas y la información complementaria en una descripción arquitectónica coherente.

La documentación útil no es necesariamente la más extensa: es la que comunica la información correcta a la audiencia adecuada y puede mantenerse a medida que evoluciona el sistema.

## Bibliografía y alcance

Este apunte organiza y explica los conceptos del material de estudio proporcionado. Para una entrega académica, conviene verificar con la bibliografía de la cátedra los nombres exactos, las estructuras recomendadas y el alcance específico de cada enfoque, especialmente Views & Beyond, Architecture Haiku y High-Level Design.

