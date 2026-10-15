Este documento refleja la teoría en la que me sustento para llevar acabo el trabajo.
La información fue sacada de las slides de la cátedra y de la bibliografía brindada, "Software Architecture in Practice" y "Designing Software Architectures" (para ADD).

Cosas de ADD:

ADD significa Attribute-Driven Design (diseño dirigido por atributos).
Es un método de diseño arquitectónico en el que construís la arquitectura de un sistema de manera iterativa, tomando decisiones de diseño guiadas por los requisitos y, especialmente, por los atributos de calidad que el sistema necesita satisfacer.
La idea central es que no diseñás toda la arquitectura de una vez. La vas construyendo por etapas, tomando decisiones justificadas y refinando la solución a medida que avanzás.

Es un método para tomar decisiones arquitectónicas justificadas por los drivers, refinando progresivamente la estructura del sistema.





Cosas de Drivers:

antes de empezar a tomar decisiones arquitectónicas, necesitás entender los requisitos y determinar cuáles van a influir realmente en la arquitectura.
Pero hay una distinción que te va a ahorrar muchos problemas.
2.1. ¿Qué es un driver arquitectónico?
Un driver arquitectónico es un requisito, una restricción o una preocupación relevante que influye de manera significativa en las decisiones de arquitectura.
No todo requisito es necesariamente un driver arquitectónico.

Extraer los requisitos funcionales. Identificar actores, objetivos, casos de uso y comportamientos relevantes.



Capturar los atributos de calidad. Identificar los atributos importantes y expresarlos mediante escenarios de seis partes.



Identificar las restricciones. Por ejemplo, tecnologías impuestas, protocolos obligatorios, normativas o límites de infraestructura.



Identificar las preocupaciones (concerns). Temas que importan a los interesados y que deben considerarse en el diseño, aunque todavía no estén expresados como requisitos precisos.



Priorizar y seleccionar los drivers. Evaluar cuáles condicionan más la arquitectura según su importancia, sus riesgos y las necesidades del proyecto.


primero especificás los requisitos y escenarios; después identificás cuáles son arquitectónicamente relevantes y los priorizás como drivers. La tabla de drivers selecciona y organiza información previa; no debería inventar los requisitos.




Requerimientos funcionales:

Escenarios de atributos de calidad:

Otros:





Cosas de herramientas arquitectónicas:

Estilos:

Tácticas:

Patrones:



Documentación:

no tenés que crear una vista nueva para cada componente que refinás. Si una iteración agrega detalle a un componente existente, actualizás la vista que corresponda. Si la decisión no cambia una vista particular, no hay motivo para duplicarla. Lo importante es que las vistas finales sean coherentes con las decisiones documentadas.



