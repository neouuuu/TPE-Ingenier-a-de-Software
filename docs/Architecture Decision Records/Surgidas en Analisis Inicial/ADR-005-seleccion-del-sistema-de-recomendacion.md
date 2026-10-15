# ADR-005: Selección del módulo avanzado de sistema de recomendación

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto
La consigna requiere seleccionar e incorporar al menos uno de los módulos funcionales avanzados. La opción A consiste en un sistema que analiza el historial y las preferencias de los usuarios para sugerir alternativas de alojamiento, transporte o rutas. También requiere un esquema *human-in-the-loop*: los usuarios pueden aceptar sugerencias o ajustar parámetros para refinar el modelo.

## Decisión
Trotamundos incorporará la **Opción A: Sistema de recomendación**.

El módulo analizará el historial y las preferencias de los usuarios para generar sugerencias proactivas de alojamiento, transporte o rutas. El usuario podrá aceptar recomendaciones o ajustar parámetros para contribuir a su refinamiento.

## Alternativas consideradas
- **Opción A:** sistema de recomendación.
- **Opción B:** asistente virtual conversacional (chatbot).

Se elige la Opción A como funcionalidad avanzada del alcance del sistema.

## Consecuencias
### Positivas
- Personaliza sugerencias de viaje.
- Aprovecha el historial y las preferencias para aportar valor.
- Permite ajustar o mejorar recomendaciones mediante la interacción del usuario.

### Costos y cuestiones pendientes
- Definir responsabilidades e interfaces del módulo.
- Definir qué datos necesita y cómo accede a ellos.
- Evaluar calidad y utilidad de las recomendaciones.
- Considerar privacidad, rendimiento y evolución del módulo.

## Trazabilidad
- Requisito avanzado, Opción A: Sistema de recomendación.
- Requisito *human-in-the-loop*.
- Requisitos aplicables de seguridad, privacidad y rendimiento.
