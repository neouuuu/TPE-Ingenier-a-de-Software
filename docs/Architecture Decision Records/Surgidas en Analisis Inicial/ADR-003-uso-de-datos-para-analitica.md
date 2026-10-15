# ADR-003: Uso de datos de viajes para analítica y mejora del servicio

- **Estado:** Aceptado
- **Fecha:** 2026-10-15

## Contexto
Trotamundos recopilará datos analíticos de viajes —tendencias, destinos y cancelaciones— para generar valor para el propio servicio y su negocio. El módulo de recomendación también utiliza el historial y las preferencias de los usuarios. El análisis puede requerir datos individuales, pero no implica que todo el equipo tenga acceso irrestricto a todos los datos personales.

## Decisión
Trotamundos recopilará y procesará datos de viajes, reservas, preferencias e interacciones con recomendaciones para analítica del producto y mejora del servicio.

El equipo de análisis podrá acceder a los datos individuales necesarios para sus tareas autorizadas, sujeto a controles de acceso. Cuando los datos agregados o desidentificados sean suficientes, se priorizarán para reducir la exposición de información personal.

La monetización se interpreta como explotación analítica para el negocio de Trotamundos; esta decisión no implica vender datos personales.

## Alternativas consideradas
- Utilizar exclusivamente datos agregados o desidentificados.
- Permitir acceso a datos individuales para tareas autorizadas y usar datos agregados o desidentificados cuando sean suficientes.
- Permitir acceso irrestricto a todos los datos individuales.

Se elige la segunda alternativa para habilitar análisis individuales cuando sean necesarios sin conceder acceso indiscriminado.

## Consecuencias
### Positivas
- Habilita el análisis de tendencias, destinos y cancelaciones.
- Aporta información para evaluar y mejorar las recomendaciones.
- Reconoce la necesidad de proteger datos personales y limitar el acceso.

### Costos y cuestiones pendientes
- Definir permisos, controles de acceso y trazabilidad.
- Proteger los datos personales almacenados y procesados.
- Definir políticas de conservación, desidentificación y acceso.

## Trazabilidad
- Requisito de analítica de datos de viajes.
- Requisito de seguridad y privacidad.
- Módulo avanzado de recomendación.
