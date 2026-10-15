# Trotamundos — Diseño de Arquitectura de Software

## ¿De qué trata el trabajo?

El trabajo práctico consiste en diseñar la arquitectura de **Trotamundos**, una plataforma que centraliza las reservas de viaje en un solo lugar y las organiza por viaje.

## ¿Qué hace el sistema?

Trotamundos permite consultar y administrar reservas, incorporarlas a partir de correos electrónicos, integrarse con servicios externos y gestionar la información de cada viaje desde la web o dispositivos móviles.

## ¿Qué método utilizamos?

Utilizamos **ADD (Attribute-Driven Design)**, un método iterativo de diseño de arquitectura que toma como guía los requerimientos y, especialmente, los atributos de calidad del sistema. En cada iteración se definen objetivos de diseño, se toman y documentan decisiones arquitectónicas y se evalúa la solución.

También se documentarán las decisiones mediante **ADR** y se desarrollará un prototipo para demostrar la viabilidad de la arquitectura propuesta.

## Estructura del repositorio

```text
/
├── README.md
├── docs/
│   ├── analysis/             # Requerimientos y contexto del sistema
│   ├── quality-attributes/   # Escenarios de atributos de calidad
│   ├── add-iterations/       # Iteraciones del método ADD
│   ├── adr/                  # Decisiones arquitectónicas
│   ├── architecture-views/   # Vistas y diagramas de arquitectura
│   └── specifications/       # Especificaciones y contratos
├── prototype/                # Prototipo de la solución
├── tests/                    # Pruebas del prototipo
└── wiki/                     # Documentación de apoyo (opcional)
```

La estructura es una propuesta inicial y puede ajustarse según las necesidades del equipo. Si utilizamos la Wiki de GitHub como documentación principal, no es necesario duplicar su contenido en la carpeta `wiki/`.
