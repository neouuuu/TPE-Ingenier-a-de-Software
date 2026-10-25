# Tabla de Drivers Arquitectónicos — Trotamundos

Tabla consolidada de entrada para las iteraciones ADD. Usa los campos que pide la teoría de la cátedra (`Teoría ADD.md`, §4.4): **ID, Tipo, Descripción, Prioridad, Fuente, Justificación arquitectónica y Estado u observaciones.**

La tabla separa los **drivers seleccionados** (los que guían el diseño) de los **requisitos originales no seleccionados** (siguen vigentes, pero no condicionan la estructura). Así se distingue lo que el enunciado pide de lo que realmente conduce las decisiones.

**Documentos de apoyo:** [Escenarios QA](Escenarios%20QA.md) · [Utility Tree](Utility%20Tree.md) · [Restricciones](Restricciones.md) · [Preocupaciones](Preocupaciones.md)

**Prioridad:** Alta / Media / Baja, seguida de **(Importancia, Dificultad)** para los escenarios de calidad. Los valores marcados con ⚠️ son propuestos y deben validarse.

---

## 1. Drivers seleccionados

### 1.1 Funcionales

| ID | Tipo | Descripción | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|---|
| **RF-07, RF-08** (CU-07) | Funcional | Obtener y procesar los correos de las cuentas autorizadas para detectar los de viaje, extraer los datos y registrar las reservas, aunque no tengan viaje asignado. | Alta | Enunciado (Procesamiento de correo) · ADR-007 | Es el origen principal de datos y concentra la mayor carga de trabajo en segundo plano. Condiciona el estilo de procesamiento (asíncrono), los datos que se conservan y el límite con los proveedores de correo. | Mecanismo de obtención (consulta o notificación) por decidir (CRN-03). Falta la regla de deduplicación (CRN-02) y elegir proveedor de correo (CRN-05) |
| **RF-11 a RF-14** (CU-10) | Funcional | Integrarse con proveedores turísticos por APIs estándar para obtener detalles, actualizaciones y cancelaciones, y reflejarlos en las reservas. | Alta | Enunciado (Integración con terceros) | Exige un límite estable con terceros heterogéneos, un modelo interno común y tolerancia a sus fallas. Determina cómo entra el cambio al sistema y cómo se cumple la frescura. | APIs reales del prototipo sin definir (CRN-05) |
| **RF-01, RF-05** (CU-01) | Funcional | Consultar las reservas organizadas por viaje y ver el detalle; una reserva pertenece a cero o un viaje. | Alta | Enunciado (panel centrado en el viaje) · ADR-007 | Es la operación de lectura más frecuente y la que mide la mayoría de los escenarios de rendimiento. Define el modelo de datos central y la separación entre incorporar y organizar reservas. | Reglas RN-01 a RN-05 definidas en [Reglas de negocio](../Análisis%20del%20dominio/Reglas%20de%20negocio.md) |
| **RF-16** | Funcional | Recopilar y analizar datos de viajes (tendencias, destinos, cancelaciones) con consultas pesadas. | Alta | Enunciado (Analítica) · ADR-003 | Genera una carga analítica que no debe interferir con la operación. Condiciona el almacenamiento, el flujo de datos y el control de acceso. | CU-12 corregido: el actor es el equipo de análisis, como indican el enunciado y ADR-003 |
| **RF-20, RF-21, RF-22** (CU-13, CU-14) | Funcional | Generar recomendaciones personalizadas y permitir aceptarlas o ajustar parámetros, usando las interacciones para refinar el modelo (*human-in-the-loop*). | Alta (módulo avanzado obligatorio) | Enunciado (Opción A) · ADR-005, ADR-006 | Introduce un módulo con ciclo propio de datos y aprendizaje, con consumo de datos personales y un bucle de retroalimentación. | ADR-006 está en estado *Propuesto* (CRN-10) |
| **RF-23, RF-24** (CU-15, CU-16) | Funcional | Compartir itinerarios con destinatarios específicos por enlace seguro y publicarlos en una red social. | Media | Enunciado (compartir) · ADR-001 | Abre el sistema a personas sin cuenta y a servicios externos, lo que define el modelo de autorización. | Falta definir autorización, caducidad y revocación (CRN-06) |
| **RF-17, RF-18** (CU-17) | Funcional | Autorizar, consultar y revocar el acceso a la cuenta de correo del usuario. | Alta | Enunciado (seguridad del correo) · diagrama de contexto · QA-SE1 | Es requisito previo de RF-07 y concentra la gestión de credenciales sensibles y su revocación. | Requisito nuevo, agregado a la documentación. Mecanismo de autorización pendiente |
| **RF-19** (CU-18) | Funcional | Notificar al usuario los cambios relevantes de sus reservas. | Media | Diagrama de contexto · QA-P1 | Hace visible la frescura de los datos y agrega un canal de salida hacia los usuarios. | Requisito nuevo, agregado a la documentación. Canales y criterios de relevancia pendientes |

### 1.2 Atributos de calidad (escenarios)

| ID | Tipo | Descripción | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|---|
| **QA-A1** | Calidad: disponibilidad | Máximo 5 min/mes de inactividad no planificada (≈ 99,988 %). | Alta (A,A) | Enunciado | Obliga a eliminar puntos únicos de falla y automatizar la recuperación. Es el atributo más exigente y atraviesa el despliegue. | RTO y RPO ⚠️ |
| **QA-S2** | Calidad: escalabilidad | Pico de 10× por evento disruptivo masivo, manteniendo las funciones críticas. | Alta (A,A) | Enunciado | Exige elasticidad, priorización y degradación controlada de lo no crítico. Define la separación de cargas. | Factor 10× y medidas durante el pico ⚠️ |
| **QA-S3** | Calidad: escalabilidad | Procesar millones de buzones sin acumular backlog ni duplicar reservas. | Alta (A,A) | Enunciado · derivado | Es el cuello de botella dominante (ver estimación). Define el modelo de procesamiento, las colas y el paralelismo. | Estimación ⚠️ (CRN-03) |
| **QA-P1** | Calidad: rendimiento | Una actualización externa se ve en la app dentro de 5 min. | Alta (A,A) | Enunciado | Fija el presupuesto de latencia de punta a punta (detección, procesamiento y presentación) y condiciona sondeo frente a notificación. | Percentil ⚠️ |
| **QA-P4** | Calidad: rendimiento | Las consultas analíticas pesadas no degradan la operación. | Alta (A,A) | Enunciado · ADR-003 | Obliga a separar el almacenamiento y los recursos analíticos de los operativos. | Variación permitida ⚠️ |
| **QA-U3** | Calidad: usabilidad / i18n | Operación multirregión: tráfico a la región más cercana y datos en la región que corresponde. | Alta (A,A) | Enunciado | Condiciona el despliegue, la replicación y el modelo de datos. Entra en tensión con QA-A1 y QA-SE2. | Regiones concretas sin definir (CRN-08) |
| **QA-P2** | Calidad: rendimiento | Web: tiempo de respuesta de 800 ms en pico. | Alta (A,M) | Enunciado | Condiciona las lecturas del itinerario (modelo de consulta, caché, ubicación de los datos). | Percentil y tramo medido ⚠️ |
| **QA-A2** | Calidad: disponibilidad | Si cae un proveedor de viajes o de correo, la app sigue sirviendo y se resincroniza al volver. | Alta (A,M) | Enunciado · derivado | Exige aislar fallas de terceros e impide que su caída se propague. | Tiempos ⚠️ |
| **QA-S1** | Calidad: escalabilidad | 2 M de usuarios activos semanales sobre 15 M de cuentas, con picos semanales. | Alta (A,M) | Enunciado | Define el dimensionamiento base y la estrategia de escalado. | |
| **QA-I1** | Calidad: interoperabilidad | Las APIs estándar de proveedores se traducen a un modelo interno, de forma idempotente. | Alta (A,M) | Enunciado | Define el modelo canónico de reservas y la capa de adaptación. | |
| **QA-I2** | Calidad: interoperabilidad | Agregar un proveedor de correo sin tocar el procesamiento. | Alta (A,M) | Enunciado | Define la abstracción sobre el acceso a correo. | Proveedor del prototipo pendiente (CRN-05) |
| **QA-SE1** | Calidad: seguridad | Acceso al correo con permisos mínimos, credenciales cifradas y revocación inmediata. | Alta (A,M) | Enunciado | Condiciona dónde y cómo se guardan credenciales y cómo se detiene el acceso. | |
| **QA-SE2** | Calidad: seguridad | Solo los destinatarios designados ven el itinerario compartido. | Alta (A,M) | Enunciado · ADR-001 | Define el modelo de autorización para personas sin cuenta. | Mecanismo pendiente (CRN-06) |
| **QA-SE3** | Calidad: seguridad | Acceso por rol, auditado y con desidentificación por defecto para analítica y recomendación. | Alta (A,M) | Enunciado · ADR-003 | Condiciona la separación de datos, los roles y la auditoría. | Políticas pendientes (CRN-07) |
| **QA-E1** | Calidad: evolucionabilidad | Nuevo medio de transporte sin modificar los existentes. | Alta (A,M) | Enunciado | Define los puntos de extensión del modelo de reservas y de las integraciones. | Trenes y buses fuera del prototipo ⚠️ |
| **QA-P5** | Calidad: rendimiento | Las recomendaciones no afectan al núcleo y responden en 3 s. | Media (M,M) ⚠️ | Derivado de ADR-005 | Define el aislamiento y el modo de invocación del recomendador. | Se aborda al diseñar el módulo avanzado |
| **QA-E3** | Calidad: evolucionabilidad | Cambiar el modelo de recomendación sin tocar el núcleo y registrar las interacciones. | Media (M,M) ⚠️ | Derivado de ADR-005, ADR-006 | Define la interfaz estable del recomendador y el registro de eventos. | Se aborda al diseñar el módulo avanzado |

### 1.3 Restricciones

| ID | Tipo | Descripción | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|---|
| **CON-06, CON-07** | Restricción | El prototipo debe demostrar la arquitectura, ser trazable y tener alcance acotado por el cronograma. | Alta | Enunciado §1, §2, §5 | Limita qué porción se implementa y exige especificaciones verificables. | Alcance por definir (CRN-15) |
| **CON-09** | Restricción | Web y móvil. | Alta | Enunciado | Condiciona los clientes y la API que los sirve. | Tecnología móvil sin definir |
| **CON-10, CON-12** | Restricción | Integración mediante APIs estándar con proveedores, correo y redes sociales. | Alta | Enunciado | Limita las opciones de integración a lo que los terceros exponen. | |
| **CON-11** | Restricción | Sistema global y multirregión. | Alta | Enunciado | Origen de QA-U3. | |
| **CON-13 / DEC-05** | Restricción | Módulo avanzado: Opción A (recomendación). | Alta | Enunciado · ADR-005 | Define el alcance del módulo avanzado. | |
| **CON-14, CON-15** | Restricción (implícita) | Normativa de datos personales y autorización expresa para el correo. | Alta | Implícita | Condiciona la ubicación y el tratamiento de los datos. | Confirmar con la cátedra |
| **DEC-01, DEC-04, DEC-07** | Decisión previa | Compartición sin cuenta y sin edición; servicio de mapas externo; reserva con cero o un viaje. | Media | ADR-001, ADR-004, ADR-007 | Acotan el modelo de acceso, las dependencias externas y el modelo de dominio. | Ver [Restricciones](Restricciones.md) |

### 1.4 Preocupaciones

| ID | Tipo | Descripción | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|---|
| **CRN-01** | Preocupación | Definir la estructura general del sistema. | Alta | Análisis inicial | Es el primer problema de diseño. | Supuesto: sistema nuevo |
| **CRN-03** | Preocupación | Consulta periódica o notificación del proveedor en la ingesta de correo. | Alta | RF-07, RF-13 · diagrama de contexto | Cambia por completo el modelo de ingesta y su costo. | Abierta: se decide en el ADD |
| **CRN-04** | Preocupación | Fuente de verdad y reconciliación entre correo, API y carga manual. | Alta | RF-02/03, RF-08, RF-13 | Define el modelo de datos y las reglas de actualización. | Abierta |
| **CRN-02, CRN-05** | Preocupación | Extracción, duplicados y condiciones de terceros. | Media | CU-07, resumen del sistema | Afectan la robustez y el alcance del prototipo. | Abierta |
| **CRN-06, CRN-07, CRN-08** | Preocupación | Autorización de enlaces, política de datos y normativa por región. | Alta | ADR-001, ADR-003 | Condicionan seguridad, datos y despliegue. | Abierta |
| **CRN-10** | Preocupación | Diseño del recomendador y su ciclo de refinamiento. | Media | ADR-005, ADR-006 | Define datos, eventos y estrategia de actualización del módulo. | Abierta |
| **CRN-12, CRN-13** | Preocupación | Costo de infraestructura y observabilidad. | Media | Enunciado | Limitan la elasticidad y exigen monitoreo desde el diseño. | Abierta |
| **CRN-15** | Preocupación | Alcance vertical del prototipo. | Alta | Enunciado §2, §5 | Decide qué drivers se demuestran. | Abierta |

---

## 2. Requisitos originales no seleccionados como drivers

Siguen vigentes y se implementan o verifican, pero **no condicionan** la estructura general; se resuelven dentro de la estructura que fijen los drivers anteriores.

| ID | Tipo | Descripción | Prioridad | Motivo por el que no es driver | Observaciones |
|---|---|---|---|---|---|
| RF-02, RF-03, RF-04 (CU-02, 03, 04) | Funcional | Registrar, actualizar y eliminar reservas manualmente. | Alta (A,B) | Operaciones de gestión estándar; el impacto en la arquitectura está cubierto por RF-01, RF-05 y la preocupación CRN-04. | Falta política de eliminación (CRN-09) |
| RF-06 (CU-06) | Funcional | Archivar viajes completados. | Media | Proceso programado sencillo sobre el modelo de viajes. | Definir «viaje completado» (CRN-09) |
| RF-09, RF-10 (CU-08, 09) | Funcional | Filtros y whitelists de remitentes. | Media | Configuración por usuario que se aplica dentro del flujo de correo. | Semántica de la whitelist por aclarar |
| RF-15 (CU-11) | Funcional | Contacto con la agencia de viajes preferida. | Baja | Derivación indirecta, sin integración técnica (ADR-002). | Revisar si se exige integración directa |
| QA-P3 | Calidad | Móvil: FCP < 1,4 s. | Media (M,M) | Se logra con decisiones de cliente y entrega de contenido, apoyadas en la estructura de lectura de QA-P2. | Verificar en el prototipo |
| QA-A3 | Calidad | Despliegues sin interrupción. | Media (M,M) | Lo resuelven las decisiones de despliegue de QA-A1. | |
| QA-A4 | Calidad | Falla del servicio de mapas. | Media (M,B) | Caso particular de aislamiento de terceros (QA-A2). | Proveedor pendiente (CRN-11) |
| QA-I3 | Calidad | Publicación en redes sociales. | Media (M,B) | Integración puntual con poca incidencia estructural. | |
| QA-SE4 | Calidad | No conservar correos que no son de viaje. | Media (M,B) | Se resuelve como regla del flujo de procesamiento. | |
| QA-E2 | Calidad | Trazabilidad y contratos. | Media (M,B) | Atraviesa todo el trabajo y es parte del proceso (CON-05). | |
| QA-U1 | Calidad | Experiencia móvil con GPS. | Media (M,M) | Decisión del cliente móvil. | Sin conexión: CRN-14 |
| QA-U2 | Calidad | Internacionalización. | Media (M,M) | Se resuelve con externalización de textos y formatos. | |

---

## 3. Propuesta de objetivos por iteración ⚠️

Sugerencia para ordenar los drivers seleccionados. Se debe ajustar al plan que el equipo defina para las iteraciones.

| Iter. | Objetivo | Drivers principales |
|---|---|---|
| **1** | Definir la estructura general del sistema. | RF-01/05, RF-07/08, RF-11 a RF-14, RF-16 · QA-A1, QA-S1, QA-S2, QA-P4, QA-E1 · CRN-01 |
| **2** | Resolver la ingesta de correo y las integraciones con proveedores. | RF-07/08, RF-11 a RF-14, RF-17, RF-18 · QA-P1, QA-S3, QA-A2, QA-I1, QA-I2, QA-SE1 · CRN-02, CRN-03, CRN-04, CRN-05 |
| **3** | Resolver la compartición, la seguridad de los datos y la multirregión. | RF-23, RF-24, RF-16 · QA-SE2, QA-SE3, QA-U3, QA-A1 · CRN-06, CRN-07, CRN-08 |
| **4** | Diseñar el módulo de recomendación y optimizar la lectura. | RF-20 a RF-22, RF-01 · QA-P2, QA-P5, QA-E3, QA-SE3 · CRN-10 |
