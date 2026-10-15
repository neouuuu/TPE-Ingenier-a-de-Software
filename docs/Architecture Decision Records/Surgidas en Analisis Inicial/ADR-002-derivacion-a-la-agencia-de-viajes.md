# ADR-002: Derivación indirecta a la agencia de viajes preferida

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto
Trotamundos debe facilitar la resolución de problemas relacionados con los viajes mediante la agencia preferida del usuario. No se ha definido una API ni un mecanismo de integración técnica con la agencia. Se prioriza mantener acotado el alcance inicial.

## Decisión
Trotamundos facilitará los datos de contacto o la vía de contacto de la agencia preferida. El usuario se comunicará con ella mediante un canal externo. Por ahora no habrá integración técnica directa entre Trotamundos y la agencia.

## Alternativas consideradas
- Integración técnica directa con la agencia.
- Derivación indirecta del usuario.
- No contemplar la agencia en el flujo del sistema.

Se elige la derivación indirecta por su menor complejidad y porque no requiere definir contratos o APIs de una agencia específica.

## Consecuencias
### Positivas
- Mantiene acotado el alcance.
- Evita depender de una API no definida.
- Permite al usuario contactar a su agencia preferida por un canal externo.

### Costos y cuestiones pendientes
- La resolución continúa fuera de Trotamundos.
- El sistema no podrá intercambiar automáticamente los datos del caso ni conocer su estado mediante una integración.
- Revisar esta decisión si se determina que el requisito de resolución de problemas exige una integración técnica directa.

## Trazabilidad
- Requisito funcional de resolución de problemas mediante la agencia preferida.
- Decisión de limitar la integración técnica en el alcance inicial.
