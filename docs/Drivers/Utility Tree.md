# Utility Tree — Trotamundos

El árbol organiza los atributos de calidad en tres niveles: **atributo → preocupación de calidad → escenario**. Cada escenario está definido en [Escenarios QA](Escenarios%20QA.md) y lleva dos valores: **(Importancia, Dificultad)**, donde A = alta, M = media, B = baja.

Los escenarios **(A,A)** son los candidatos a ASR (requisitos arquitectónicamente significativos) y marcan por dónde empezar. Los valores son una propuesta del equipo y deben revisarse.

## Árbol

```text
Utilidad de Trotamundos
│
├── Rendimiento y latencia
│   ├── Frescura de los datos
│   │   └── QA-P1   Actualización visible en ≤ 5 min                          (A,A) ★
│   ├── Latencia de consulta
│   │   ├── QA-P2   Web: 800 ms en pico                                       (A,M)
│   │   └── QA-P3   Móvil: FCP < 1,4 s                                        (M,M)
│   └── Aislamiento de cargas
│       ├── QA-P4   Analítica pesada sin degradar la operación                (A,A) ★
│       └── QA-P5   Recomendaciones sin afectar al núcleo                     (M,M)
│
├── Disponibilidad
│   ├── Fallas de infraestructura
│   │   └── QA-A1   ≤ 5 min/mes de inactividad no planificada                 (A,A) ★
│   ├── Fallas de servicios externos
│   │   ├── QA-A2   Degradación controlada si cae un proveedor                (A,M)
│   │   └── QA-A4   Degradación controlada si cae el servicio de mapas        (M,B)
│   └── Operación
│       └── QA-A3   Despliegues sin interrupción                              (M,M)
│
├── Escalabilidad
│   ├── Carga sostenida
│   │   └── QA-S1   2 M usuarios activos semanales / 15 M cuentas             (A,M)
│   ├── Picos extremos
│   │   └── QA-S2   Pico de 10× por evento disruptivo masivo                  (A,A) ★
│   └── Volumen de ingesta
│       └── QA-S3   Procesar millones de buzones sin acumular backlog         (A,A) ★
│
├── Interoperabilidad
│   ├── Proveedores turísticos
│   │   └── QA-I1   APIs estándar traducidas al modelo interno                (A,M)
│   ├── Proveedores de correo
│   │   └── QA-I2   Nuevo proveedor de correo sin tocar el procesamiento      (A,M)
│   └── Redes sociales
│       └── QA-I3   Publicar solo lo que el usuario eligió                    (M,B)
│
├── Seguridad y privacidad
│   ├── Acceso al correo
│   │   ├── QA-SE1  Autorización mínima, credenciales cifradas, revocación    (A,M)
│   │   └── QA-SE4  No conservar correos que no son de viaje                  (M,B)
│   ├── Compartición
│   │   └── QA-SE2  Solo los destinatarios designados ven el itinerario       (A,M)
│   └── Datos personales
│       └── QA-SE3  Acceso por rol y desidentificación en analítica           (A,M)
│
├── Evolucionabilidad y mantenibilidad
│   ├── Extensibilidad
│   │   ├── QA-E1   Nuevo medio de transporte sin tocar lo existente          (A,M)
│   │   └── QA-E3   Cambiar el modelo de recomendación sin tocar el núcleo    (M,M)
│   └── Trazabilidad
│       └── QA-E2   Requisito → ADR → vista → especificación → código         (M,B)
│
└── Usabilidad e internacionalización
    ├── Experiencia móvil
    │   └── QA-U1   Contexto GPS y datos del viaje sin conexión               (M,M)
    ├── Internacionalización
    │   └── QA-U2   Nuevo idioma solo con archivos de recursos                (M,M)
    └── Multirregión
        └── QA-U3   Región más cercana y ubicación de los datos               (A,A) ★
```

★ = candidato a ASR.

## Tabla de prioridades

Orden de atención: primero los escenarios (A,A), después los (A,M) y por último los de importancia media o baja.

| Prioridad | Escenarios | Qué significa para el diseño |
|---|---|---|
| **1 — (A,A)** | QA-P1, QA-P4, QA-A1, QA-S2, QA-S3, QA-U3 | Condicionan la estructura general. Se resuelven primero |
| **2 — (A,M)** | QA-P2, QA-A2, QA-S1, QA-I1, QA-I2, QA-SE1, QA-SE2, QA-SE3, QA-E1 | Se resuelven con patrones y tácticas conocidas, apoyándose en la estructura de la primera etapa |
| **3 — (M,\*)** | QA-P3, QA-P5, QA-A3, QA-A4, QA-I3, QA-SE4, QA-E2, QA-E3, QA-U1, QA-U2 | Se tienen en cuenta y se verifican; rara vez cambian la estructura. QA-P5 y QA-E3 se abordan cuando se diseñe el módulo de recomendación |

## Cómo se obtuvo la prioridad

- **Importancia:** alta si el enunciado fija una medida explícita (800 ms, 5 min, 5 min/mes, 2 M / 15 M) o si afecta directamente la propuesta de valor de Trotamundos (un único punto de verdad, actualizado y seguro). Media si apoya funciones secundarias. Baja si es de alcance acotado.
- **Dificultad:** alta si exige combinar varias decisiones estructurales (datos, comunicación y despliegue a la vez), si depende de terceros que no controlamos o si no hay una solución estándar simple.
- Los valores de QA-P5 y QA-E3 son **supuestos**: el enunciado no fija medidas para el módulo de recomendación.
