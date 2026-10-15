# ADR-006: Uso de interacciones para refinar las recomendaciones

- **Estado:** Propuesto
- **Fecha:** 2026-10-15

## Contexto
El módulo de recomendación utilizará el historial y las preferencias para sugerir alternativas de alojamiento, transporte y rutas. La consigna requiere un esquema *human-in-the-loop*: el usuario puede aceptar sugerencias o ajustar parámetros para refinar continuamente el modelo.

## Decisión propuesta
Registrar las interacciones relevantes con las recomendaciones —por ejemplo, aceptar una sugerencia o modificar parámetros— para que puedan utilizarse al evaluar y mejorar el comportamiento del recomendador.

La estrategia concreta de uso de estos datos, así como la frecuencia y el mecanismo de actualización del modelo, se definirán durante el diseño. Esta decisión no implica reentrenar el modelo inmediatamente después de cada interacción.

## Alternativas consideradas
- No registrar las interacciones.
- Registrar las interacciones y utilizarlas para evaluar y mejorar las recomendaciones.
- Actualizar automáticamente el modelo después de cada interacción.

Se propone la segunda alternativa porque conserva señales útiles para la mejora continua sin imponer una estrategia de actualización específica.

## Consecuencias
### Positivas
- Permite evaluar la utilidad de las recomendaciones.
- Habilita mejoras a partir de las interacciones.
- Mantiene flexibilidad para decidir cómo y cuándo actualizar el modelo.

### Costos y cuestiones pendientes
- Definir eventos registrados y plazo de conservación.
- Controlar el acceso a esos datos.
- Decidir si el refinamiento se realizará mediante ajustes de parámetros, análisis periódico, reentrenamiento u otra estrategia.
- Evaluar cómo evitar que las señales registradas degraden las recomendaciones.

## Trazabilidad
- Requisito avanzado de sistema de recomendación.
- Requisito *human-in-the-loop*.
- ADR-003: uso de datos para analítica y mejora del servicio.
- ADR-005: selección del módulo de recomendación.
