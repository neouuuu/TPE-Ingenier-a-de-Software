# ADR-004: Integración con un servicio externo de mapas y navegación

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto
Trotamundos debe ofrecer una interfaz rica y aprovechar capacidades nativas de dispositivos móviles, como el GPS. El módulo de recomendación también puede sugerir alternativas de rutas. Se decidió utilizar un servicio externo de mapas para obtener información geográfica y asistir en la consulta y cálculo de rutas.

## Decisión
Trotamundos se integrará con un servicio externo de mapas y navegación para consultar ubicaciones, rutas y estimaciones de distancia o duración. El proveedor concreto aún no está seleccionado.

El GPS del dispositivo y el servicio externo son capacidades distintas: el GPS puede proporcionar la ubicación del dispositivo, mientras que el servicio puede aportar mapas, datos geográficos y cálculo de rutas.

## Alternativas consideradas
- Desarrollar internamente mapas y cálculo de rutas.
- Integrarse con un servicio externo especializado.
- Utilizar únicamente la ubicación GPS sin un servicio externo de mapas o rutas.

Se elige la integración externa para aprovechar capacidades especializadas y evitar desarrollar toda esa funcionalidad desde cero.

## Consecuencias
### Positivas
- Incorpora información geográfica y rutas a la experiencia de viaje.
- Puede apoyar las recomendaciones de rutas.
- Reduce la necesidad de implementar internamente todas las capacidades cartográficas.

### Costos y cuestiones pendientes
- Dependencia de la disponibilidad, latencia, límites de uso y condiciones del proveedor.
- Definir el comportamiento cuando el servicio no esté disponible.
- Seleccionar proveedor y especificar su API.
- Considerar permisos y protección de datos al usar la ubicación del usuario.

## Trazabilidad
- Requisito de interfaz rica y capacidades nativas como GPS.
- Funcionalidad de recomendación de rutas.
