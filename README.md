# Trotamundos — Diseño de Arquitectura de Software

Trotamundos es una plataforma web y móvil para centralizar reservas de viaje, organizarlas en itinerarios y mantenerlas actualizadas a partir de fuentes externas. El trabajo práctico documenta el diseño de su arquitectura mediante **Attribute-Driven Design (ADD)**.

## Alcance del sistema

- Gestionar viajes y reservas, incluidas reservas importadas desde correo y reservas sin asignar a un viaje.
- Sincronizar información con proveedores turísticos mediante integraciones desacopladas.
- Compartir itinerarios por correo con enlaces de solo lectura y publicar itinerarios en redes sociales compatibles.
- Ofrecer analítica protegida y un módulo avanzado de recomendaciones personalizadas.
- Preparar el diseño para requisitos de rendimiento, disponibilidad, seguridad, escalabilidad, evolución e internacionalización.

Las integraciones externas concretas siguen pendientes de validación: el diseño no presupone que una agencia, proveedor de correo, empresa turística o red social ofrezca una API con todas las capacidades requeridas.

## Método de diseño

Se utiliza **ADD (Attribute-Driven Design)**. Cada iteración identifica drivers arquitectónicos, selecciona elementos para refinar, evalúa alternativas, registra decisiones mediante ADR y produce vistas que describen la arquitectura resultante.

Las cuatro iteraciones son el proceso de diseño arquitectónico. La etapa 5 es una validación previa al prototipo para comprobar APIs, permisos, cuotas, costos y contratos reales; no sustituye una iteración ADD.

## Documentación

### Análisis del dominio

- [Resumen del sistema](docs/An%C3%A1lisis%20del%20dominio/Resumen%20Sistema.md)
- [Requerimientos funcionales](docs/An%C3%A1lisis%20del%20dominio/Requerimientos%20funcionales.md)
- [Reglas de negocio](docs/An%C3%A1lisis%20del%20dominio/Reglas%20de%20negocio.md)
- [Diagrama de contexto](docs/An%C3%A1lisis%20del%20dominio/Diagrama%20de%20Contexto.md)
- [Diagrama y descriptores de casos de uso](docs/An%C3%A1lisis%20del%20dominio/Descriptores%20Casos%20de%20Uso.md)
- [Índice de ADR del análisis del dominio](docs/An%C3%A1lisis%20del%20dominio/Architecture%20Decision%20Records/README.md)

### Drivers arquitectónicos

- [Tabla consolidada de drivers](docs/Drivers/Tabla%20de%20Drivers.md)
- [Escenarios de atributos de calidad](docs/Drivers/Escenarios%20QA.md)
- [Árbol de utilidad](docs/Drivers/Utility%20Tree.md)
- [Restricciones](docs/Drivers/Restricciones.md)
- [Preocupaciones abiertas](docs/Drivers/Preocupaciones.md)

### Iteraciones ADD

- [Plan y secuencia de las iteraciones](docs/ADD/00-Plan%20de%20iteraciones%20ADD.md)
- [ADD-1 — Arquitectura de alto nivel](docs/ADD/01-Iteracion-1/Iteracion-1.md)
- [ADD-2 — Componentes funcionales centrales](docs/ADD/02-Iteracion-2/Iteracion-2.md)
- [ADD-3 — Disponibilidad, seguridad y resiliencia](docs/ADD/03-Iteracion-3/Iteracion-3.md)
- [ADD-4 — Rendimiento, analítica y recomendaciones](docs/ADD/04-Iteracion-4/Iteracion-4.md)
- [Etapa 5 — Validación de integraciones antes del prototipo](docs/ADD/05-Integraciones-pendientes.md)

Cada iteración incluye sus vistas arquitectónicas y ADR propios. Los diagramas describen decisiones propuestas; no constituyen evidencia de que las metas de calidad ya se hayan alcanzado.

## Estructura del repositorio

```text
/
├── README.md
└── docs/
    ├── Análisis del dominio/
    │   ├── Resumen Sistema.md
    │   ├── Requerimientos funcionales.md
    │   ├── Reglas de negocio.md
    │   ├── Diagrama de Contexto.md
    │   ├── Descriptores Casos de Uso.md
    │   └── Architecture Decision Records/
    │       ├── README.md
    │       ├── Surgidas en Analisis Inicial/       # ADR-001 a ADR-006
    │       └── Surgidas en Captura de Requerimientos/ # ADR-007
    ├── Drivers/
    │   ├── Tabla de Drivers.md
    │   ├── Escenarios QA.md
    │   ├── Utility Tree.md
    │   ├── Restricciones.md
    │   └── Preocupaciones.md
    └── ADD/
        ├── 00-Plan de iteraciones ADD.md
        ├── 01-Iteracion-1/  # Diseño de alto nivel, vistas y ADR-008/009
        ├── 02-Iteracion-2/  # Componentes funcionales, vistas y ADR-010/011
        ├── 03-Iteracion-3/  # Resiliencia/seguridad, vistas y ADR-012/013
        ├── 04-Iteracion-4/  # Analítica/recomendaciones, vistas y ADR-014/015
        └── 05-Integraciones-pendientes.md
```

## Estado actual

La documentación define una arquitectura lógica, sus decisiones y los asuntos que siguen abiertos. Antes del prototipo deben verificarse las APIs de terceros, cerrar la política de acceso a enlaces compartidos, definir precedencia en conflictos entre fuentes y confirmar el alcance de despliegue, operación y pruebas de carga.
