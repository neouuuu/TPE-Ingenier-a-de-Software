# Guía de trabajo y sustento teórico — Diseño de la arquitectura de Trotamundos mediante ADD

## 1. Objetivo y enfoque general

El trabajo práctico consiste en diseñar la arquitectura de software del sistema **Trotamundos**, aplicando el método **ADD (Attribute-Driven Design)**, documentando las decisiones arquitectónicas y desarrollando un prototipo que demuestre la viabilidad de la solución propuesta.

La consigna requiere documentar las iteraciones y sus artefactos, realizar al menos cuatro iteraciones ADD y registrar las decisiones arquitectónicas mediante ADR (*Architecture Decision Records*) siguiendo el formato MADR. También se deben elaborar las vistas arquitectónicas pertinentes y mantener la trazabilidad entre los requerimientos, las decisiones, la arquitectura y el código.

La idea central de ADD es que **la arquitectura se construye de manera iterativa, tomando decisiones justificadas por los requerimientos y, especialmente, por los atributos de calidad que el sistema debe satisfacer**.

Cada iteración debe abordar un objetivo de diseño concreto, seleccionar los drivers relevantes, refinar uno o más elementos arquitectónicos, documentar las decisiones tomadas y analizar si la solución obtenida satisface el objetivo planteado.

La metodología de trabajo se organizará en las siguientes etapas:

1. Analizar el enunciado y delimitar el sistema.
2. Identificar y especificar los requerimientos.
3. Capturar y priorizar los drivers arquitectónicos.
4. Diseñar la arquitectura mediante iteraciones ADD.
5. Documentar las decisiones y las vistas arquitectónicas.
6. Implementar y probar el prototipo.
7. Evaluar los resultados y ajustar el diseño cuando sea necesario.

---

## 2. Análisis inicial y delimitación del sistema

Antes de comenzar las iteraciones ADD, es necesario comprender el problema, identificar los requerimientos y establecer qué forma parte del sistema y qué queda fuera de sus límites.

### 2.1. Diagrama de contexto

El diagrama de contexto representa el sistema como una unidad y muestra sus interacciones con los actores y sistemas externos.

Su objetivo es establecer:

- El límite del sistema que se va a diseñar.
- Los actores que interactúan con él.
- Los sistemas externos con los que se comunica.
- Las principales interacciones y los intercambios de información.

El contexto define el alcance conceptual del sistema, pero no determina por sí solo qué funcionalidades se implementarán en el prototipo. El alcance de la implementación puede ser más acotado y debe quedar explícitamente documentado.

### 2.2. Identificación de los requerimientos

A partir del enunciado, se deben identificar los requerimientos funcionales, los atributos de calidad, las restricciones y las preocupaciones relevantes.

Los requerimientos funcionales describen **qué debe hacer el sistema**.

Los casos de uso constituyen una forma de especificar los requerimientos funcionales. Deben identificar el objetivo del actor, el comportamiento esperado, el flujo principal y las alternativas relevantes cuando corresponda.

No es necesario crear un caso de uso independiente por cada requisito. Varios requisitos relacionados pueden formar parte de un mismo caso de uso.

Además, se asignan identificadores estables a los requisitos y casos de uso, por ejemplo, RF-01 o CU-01, para poder referenciarlos posteriormente.

---

## 3. Atributos de calidad y escenarios

Los atributos de calidad describen propiedades del sistema que condicionan su diseño, como rendimiento, disponibilidad, escalabilidad, seguridad, interoperabilidad, evolucionabilidad y usabilidad.

Deben especificarse mediante un escenario concreto que permita comprender qué se espera del sistema y, cuando corresponda, medir si lo consigue.

### 3.1. Escenarios de atributos de calidad

Cada escenario se describe mediante seis elementos:

1. **Fuente del estímulo:** quién o qué origina la situación.
2. **Estímulo:** el evento o la condición que se produce.
3. **Entorno:** las condiciones en las que ocurre.
4. **Artefacto:** la parte del sistema afectada.
5. **Respuesta:** el comportamiento que debe tener el sistema.
6. **Medida de respuesta:** el criterio cuantificable o verificable que permite evaluar el resultado.

La formulación debe ser lo suficientemente precisa para orientar decisiones arquitectónicas y permitir evaluar posteriormente el resultado.

---

## 4. Drivers arquitectónicos

### 4.1. ¿Qué es un driver arquitectónico?

Un driver arquitectónico es un requerimiento, una restricción o una preocupación relevante que influye significativamente en las decisiones de arquitectura.

**No todo requerimiento es automáticamente un driver arquitectónico.** Un requisito puede ser importante para la funcionalidad del sistema sin condicionar de manera significativa su estructura. En cambio, algunos requerimientos de calidad, restricciones o necesidades funcionales pueden obligar a tomar decisiones arquitectónicas específicas.

Los drivers constituyen las entradas que guían el diseño. Permiten determinar qué problemas arquitectónicos deben resolverse primero, qué elementos conviene refinar y qué decisiones deben justificarse.

### 4.2. Tipos de información que deben analizarse

- **Requerimientos funcionales:** comportamientos y servicios que debe ofrecer el sistema.
- **Atributos de calidad:** propiedades que debe satisfacer y escenarios que permitan evaluarlas.
- **Restricciones:** condiciones obligatorias que limitan las alternativas posibles, como tecnologías impuestas, protocolos o exigencias de infraestructura.
- **Preocupaciones (*concerns*):** temas importantes para los interesados que deben considerarse, aunque todavía no estén expresados como requisitos precisos.

### 4.3. Identificación y priorización

El proceso recomendado es:

1. Extraer los requerimientos funcionales.
2. Identificar actores, objetivos, casos de uso y comportamientos relevantes.
3. Capturar los atributos de calidad y expresarlos mediante escenarios.
4. Identificar las restricciones aplicables.
5. Registrar las preocupaciones relevantes y aclarar las que sean ambiguas.
6. Determinar cuáles de estos elementos influyen significativamente en la arquitectura.
7. Priorizar los drivers según su importancia, sus riesgos y su impacto en el diseño.

### 4.4. Tabla de drivers arquitectónicos

Se recomienda mantener una tabla consolidada con los siguientes campos:

| Campo | Propósito |
|---|---|
| ID | Identificador estable del elemento. |
| Tipo | Requerimiento funcional, escenario de calidad, restricción o preocupación. |
| Descripción | Formulación concreta del requisito o necesidad. |
| Prioridad | Importancia relativa para el diseño. |
| Fuente | Parte del enunciado o interesado del que proviene. |
| Justificación arquitectónica | Explicación de por qué puede influir en la arquitectura. |
| Estado u observaciones | Supuestos, ambigüedades o cuestiones pendientes. |

La tabla debe permitir distinguir los requisitos originales de los drivers seleccionados.

Los drivers seleccionados guiarán las iteraciones ADD. 

---

## 5. Conceptos fundamentales de diseño arquitectónico

Para aplicar ADD correctamente, es necesario distinguir tres conceptos: conceptos de diseño, estructura arquitectónica y representación de esa estructura.

### 5.1. Conceptos de diseño

Son las soluciones generales que se seleccionan para abordar los drivers. Pueden incluir estilos arquitectónicos, patrones y tácticas.

Un estilo arquitectónico define una organización general; un patrón resuelve un problema recurrente de diseño; una táctica busca influir en un atributo de calidad mediante un mecanismo más específico. Estos conceptos pueden complementarse.

### 5.2. Estructura arquitectónica

Es la solución concreta que se construye al aplicar los conceptos de diseño elegidos. Incluye los elementos arquitectónicos, sus responsabilidades, sus interfaces y sus relaciones.

### 5.3. Representación arquitectónica

Es el medio utilizado para comunicar y documentar la estructura resultante. Puede incluir diagramas UML, descripciones textuales, tablas de responsabilidades y otras representaciones adecuadas.

La relación entre estos conceptos es:

**Drivers → conceptos de diseño → estructura arquitectónica → vistas y documentación.**

---

## 6. Método ADD 3.0: los siete pasos

El diseño arquitectónico se desarrollará siguiendo los siete pasos de ADD 3.0.

### Paso 1. Revisar las entradas del diseño

Se revisan los requerimientos, los escenarios de atributos de calidad, las restricciones, las preocupaciones, los supuestos y las decisiones existentes que puedan afectar la iteración.

El objetivo es comprender qué información está disponible y qué necesidades deben orientar el diseño.

### Paso 2. Establecer el objetivo de la iteración seleccionando drivers

Se define qué problema arquitectónico se quiere resolver y se seleccionan los drivers que condicionan ese objetivo.

Una iteración debe tener un propósito concreto. 

No es suficiente indicar que se trabajará sobre un componente determinado. Debe explicarse qué problema se pretende resolver y por qué es relevante.

### Paso 3. Elegir uno o más elementos del sistema para refinar

Se selecciona el elemento arquitectónico que será objeto del diseño. En las primeras iteraciones puede ser el sistema completo; en iteraciones posteriores puede ser un subsistema o componente previamente identificado.

**La selección de elementos depende del objetivo de la iteración y de los drivers relevantes.** No existe una correspondencia automática entre un driver y un componente.

Un driver puede afectar varios elementos, y un mismo elemento puede verse condicionado por distintos drivers. Por eso hay que justificar por qué el elemento seleccionado es el lugar adecuado para tomar las decisiones necesarias.

Para priorizar elementos a refinar, conviene considerar:

- Si concentran drivers de alta prioridad.
- Si presentan riesgos técnicos importantes.
- Si contienen decisiones difíciles de revertir.
- Si son complejos o están insuficientemente definidos.
- Si condicionan el diseño de otros elementos.

No se deben seleccionar componentes únicamente porque todavía no se han detallado. Un elemento puede quedar pendiente si no es relevante para el objetivo actual.

### Paso 4. Elegir conceptos de diseño para satisfacer los drivers

Se evalúan y seleccionan los estilos, patrones, tácticas y demás conceptos de diseño adecuados para resolver el problema de la iteración.

La selección debe justificarse a partir de los drivers, considerando las alternativas razonables y sus consecuencias.

### Paso 5. Instanciar elementos arquitectónicos, asignar responsabilidades y definir interfaces

Se construye la estructura concreta mediante la aplicación de los conceptos de diseño seleccionados.

Las actividades incluyen:

- Identificar los elementos arquitectónicos necesarios.
- Crear elementos o refinar los existentes.
- Asignar responsabilidades claras.
- Definir interfaces y contratos.
- Establecer relaciones y dependencias.
- Determinar cómo colaboran los elementos para satisfacer los drivers.

No todas las iteraciones deben crear componentes nuevos. Algunas pueden redefinir responsabilidades, introducir una interfaz, modificar dependencias o establecer un mecanismo de comunicación entre elementos existentes.

### Paso 6. Generar vistas y registrar decisiones de diseño

Se documenta la solución obtenida mediante las vistas arquitectónicas pertinentes y se registran las decisiones significativas mediante ADR.

Las vistas deben mostrar las estructuras relevantes para el objetivo de la iteración. No es necesario producir todos los tipos de diagramas en cada iteración.

Los ADR documentan por qué se tomaron decisiones arquitectónicas, qué alternativas se evaluaron y qué consecuencias se esperan.

### Paso 7. Analizar el diseño actual y revisar el objetivo de la iteración

Se evalúa si la solución satisface los drivers y el objetivo definidos.

Es necesario analizar:

- Qué requerimientos quedan satisfechos y con qué fundamento.
- Qué riesgos persisten.
- Qué compromisos introduce la solución.
- Qué aspectos requieren mayor detalle.
- Qué decisiones podrían necesitar revisión.
- Qué elementos deben refinarse en iteraciones posteriores.

---

## 7. Cómo seleccionar componentes a partir de los drivers

La relación entre drivers y componentes es una de las decisiones centrales del proceso ADD.

En cada iteración se debe responder:

1. ¿Qué problema arquitectónico se intenta resolver?
2. ¿Qué drivers justifican ese objetivo?
3. ¿Qué elementos están involucrados?
4. ¿Por qué conviene refinar esos elementos?
5. ¿Qué decisiones se necesitan tomar?
6. ¿Cómo se evaluará si el resultado satisface el objetivo?

Esta justificación debe quedar registrada para que el proceso de diseño sea comprensible y trazable.

---

## 8. Documentación arquitectónica

La documentación debe mostrar tanto el proceso de diseño como el resultado arquitectónico. Para ello, conviene distinguir tres artefactos principales: el registro de iteración ADD, los ADR y las vistas arquitectónicas.

### 8.1. Registro de una iteración ADD

Se recomienda mantener una ficha por iteración con los siguientes campos:

1. **Identificador y objetivo:** qué problema arquitectónico se intenta resolver.
2. **Entradas revisadas:** requerimientos, escenarios, restricciones, decisiones existentes y supuestos relevantes.
3. **Drivers seleccionados:** identificadores de los elementos que justifican el objetivo.
4. **Elementos a refinar:** componentes o subsistemas elegidos y justificación de la selección.
5. **Conceptos de diseño:** estilos, patrones, tácticas u otras soluciones consideradas, con su justificación.
6. **Estructura resultante:** elementos creados o modificados, responsabilidades, interfaces y relaciones.
7. **Vistas afectadas:** diagramas elaborados o actualizados.
8. **Decisiones registradas:** referencias a los ADR correspondientes.
9. **Evaluación:** grado de cumplimiento del objetivo, riesgos restantes y cuestiones pendientes.
10. **Próximos pasos:** elementos o problemas que conviene abordar en iteraciones posteriores.

El registro ADD y los ADR no son lo mismo: el primero documenta el desarrollo de una iteración; los segundos registran decisiones arquitectónicas específicas.

### 8.2. Architecture Decision Records (ADR)

Un ADR es un registro enfocado y versionable de una decisión arquitectónica significativa. Permite comprender por qué se eligió una solución y cuáles son las consecuencias de esa elección.

La consigna exige utilizar el formato **MADR (Markdown Any Decision Records)**.

Una estructura habitual de MADR contiene:

- **Título e identificador:** expresan la decisión de manera clara y permiten referenciarla.
- **Estado:** indica si está propuesta, aceptada, rechazada, reemplazada u otro estado previsto por la plantilla.
- **Contexto y problema:** describe la situación que hace necesaria la decisión.
- **Drivers de decisión:** identifica los requerimientos, atributos de calidad y restricciones relevantes.
- **Opciones consideradas:** presenta las alternativas razonables evaluadas.
- **Decisión:** establece qué opción se eligió y por qué.
- **Consecuencias:** registra beneficios, costos, riesgos, limitaciones y compromisos introducidos por la elección.

#### ¿Cuándo se crea un ADR?

Se crea cuando se toma una decisión arquitectónica que vale la pena conservar y justificar. No es necesario esperar a que termine la iteración.

El proceso habitual es:

1. Identificar un problema arquitectónico.
2. Analizar los drivers que condicionan la decisión.
3. Considerar alternativas razonables.
4. Seleccionar una opción y justificarla.
5. Registrar la decisión y sus consecuencias en un ADR.
6. Actualizar las vistas afectadas.
7. Si la decisión cambia posteriormente, actualizar el estado y registrar la relación con la nueva decisión, conservando la trazabilidad histórica.

No existe una correspondencia obligatoria de un ADR por iteración. Una iteración puede producir varios ADR, una decisión puede surgir en distintos momentos del diseño y una iteración puede no requerir un ADR nuevo.

### 8.3. Vistas arquitectónicas y diagramas

Las vistas arquitectónicas representan diferentes estructuras del sistema. Cada una permite responder preguntas específicas.

Se deben elegir según las decisiones tomadas, los drivers relevantes y la información que se necesita comunicar.

#### Vista de módulos

Representa la organización lógica o estática del software, sus módulos, paquetes y dependencias.

Un diagrama de paquetes UML puede utilizarse para mostrar esta estructura. Los diagramas de clases pueden aportar más detalle cuando sea necesario.

Sirve para analizar cuestiones como la separación de responsabilidades, el acoplamiento y la organización del código.

#### Vista de componentes y conectores (C&C)

Representa los elementos que interactúan durante la ejecución y las relaciones de comunicación entre ellos.

Un diagrama de componentes UML puede utilizarse para mostrar componentes, interfaces y conexiones.

Los diagramas de secuencia UML pueden complementar esta vista al describir cómo colaboran los elementos para ejecutar un escenario concreto.

#### Vista de asignación

Representa cómo se relaciona el software con su entorno de ejecución, infraestructura u otros recursos.

Un diagrama de despliegue UML puede mostrar nodos, entornos de ejecución y artefactos desplegados cuando esas decisiones sean relevantes.

La vista de asignación es más amplia que el despliegue: puede abarcar otras relaciones entre elementos de software y recursos o entornos.

La pregunta correcta no es «¿qué diagrama tengo que dibujar en esta iteración?», sino «¿qué decisión arquitectónica necesito tomar y qué representación me permite comunicarla y evaluarla?».

### 8.4. Relación entre iteraciones, ADR y vistas

Los tres artefactos se complementan:

- **Registro ADD:** explica qué se hizo durante la iteración, qué se intentó resolver y cómo se evaluó el resultado.
- **ADR:** explica por qué se tomó una decisión arquitectónica concreta, qué alternativas se consideraron y qué consecuencias introduce.
- **Vista arquitectónica:** muestra cómo queda estructurado el sistema como resultado de las decisiones.

Una decisión puede afectar varias vistas y un registro ADD puede referenciar varios ADR. No es necesario copiar el contenido completo de un ADR en el registro de la iteración ni repetir toda su justificación dentro de los diagramas.

Lo importante es mantener referencias consistentes entre los artefactos.

---

## 9. Especificaciones, contratos e implementación

El trabajo también requiere un prototipo que demuestre la viabilidad de la arquitectura. Por ello, el diseño debe poder traducirse en especificaciones verificables y en código coherente con la arquitectura documentada.

La consigna recomienda utilizar un enfoque de *spec-driven development*, tanto para el diseño con ADD como para la implementación.

Según el alcance del prototipo, las especificaciones pueden incluir:

- Contratos de APIs.
- Interfaces entre componentes.
- Formatos y estructuras de datos.
- Comportamientos esperados.
- Reglas de validación.
- Escenarios de prueba.
- Criterios de aceptación.
- Requisitos de calidad que puedan medirse.

No es necesario documentar individualmente cada función del código. El nivel de detalle debe ser suficiente para implementar, verificar y demostrar los comportamientos acordados.

Debe mantenerse la trazabilidad entre:

**Requerimientos → drivers → decisiones arquitectónicas → estructura y vistas → especificaciones → implementación y pruebas.**

Por ejemplo, si un escenario exige que una actualización externa se refleje en el itinerario dentro de cinco minutos, debe ser posible identificar qué decisiones arquitectónicas contribuyen a satisfacerlo, qué parte del sistema implementa ese comportamiento y cómo se comprobará en el prototipo.

La evaluación también debe considerar las limitaciones del prototipo. Que una solución funcione en una demostración acotada no demuestra automáticamente que satisfaga las exigencias de escala global, disponibilidad o rendimiento de producción.

---

## 10. Secuencia práctica para comenzar

Antes de iniciar las iteraciones ADD, el trabajo debería avanzar en este orden:

1. Leer y descomponer la especificación de Trotamundos.
2. Definir el alcance del sistema y elaborar el diagrama de contexto.
3. Identificar los requerimientos funcionales y documentar los casos de uso necesarios.
4. Identificar los atributos de calidad y redactar escenarios de seis partes que respeten las medidas y condiciones del enunciado.
5. Registrar las restricciones, preocupaciones y supuestos relevantes.
6. Elaborar y priorizar la tabla de drivers arquitectónicos.
7. Seleccionar el objetivo de la primera iteración ADD a partir de los drivers prioritarios.
8. Elegir los elementos a refinar y justificar esa selección.
9. Evaluar conceptos de diseño y alternativas.
10. Construir la estructura arquitectónica concreta, definiendo responsabilidades, interfaces y relaciones.
11. Registrar las decisiones significativas mediante ADR y actualizar las vistas afectadas.
12. Analizar el resultado y definir qué debe abordarse en la siguiente iteración.
13. Repetir el proceso hasta obtener una arquitectura suficientemente definida para el alcance del trabajo y cumplir con el mínimo de cuatro iteraciones.
14. Desarrollar y probar el prototipo, manteniendo la documentación y la implementación alineadas.





