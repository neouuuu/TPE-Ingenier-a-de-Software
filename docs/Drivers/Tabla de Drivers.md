# Tabla consolidada de drivers arquitectónicos — Trotamundos

Esta tabla identifica qué elementos condicionan decisiones de arquitectura. **Un requisito importante no es automáticamente un driver**: se selecciona como driver cuando cambia la estructura, los mecanismos o las alternativas de diseño. Los requisitos no incluidos aquí siguen vigentes y se implementan dentro de la arquitectura resultante.

**Prioridad:** Alta = condiciona estructura o riesgo significativo; Media = condiciona un subsistema o decisión local; Baja = efecto arquitectónico limitado. Las metas cuantitativas atribuidas al enunciado son requisitos; las estimaciones de carga o metas derivadas se marcan como supuestos.

Documentos: [Escenarios QA](Escenarios%20QA.md) · [Utility Tree](Utility%20Tree.md) · [Restricciones](Restricciones.md) · [Preocupaciones](Preocupaciones.md) · [Plan ADD](../ADD/00-Plan%20de%20iteraciones%20ADD.md).

## 1. Drivers funcionales seleccionados

| ID | Descripción | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|
| RF-01, RF-05; RN-01–RN-05 | Consultar viajes/reservas; permitir reserva sin asignar y asociarla a cero o un viaje. | Alta | Requerimientos y ADR-007 | Define modelo central, integridad y camino de lectura frecuente. | Reglas de dominio definidas; ciclo de vida del viaje sigue pendiente. |
| RF-07, RF-08, RF-09, RF-10, RF-17, RF-18 | Ingestar correos autorizados, filtrar y extraer reservas; permitir revocación. | Alta | Requerimientos | Trabajo externo lento, datos sensibles, deduplicación y procesamiento en segundo plano. | Preferir notificaciones/webhooks si existen; consulta periódica como alternativa. APIs reales pendientes. |
| RF-11–RF-14 | Consultar detalles, cambios y cancelaciones de reservas en proveedores turísticos. | Alta | Requerimientos | Exige adaptadores, modelo canónico, tolerancia a fallas y reconciliación. | Proveedores y contratos pendientes de etapa 5. |
| RF-15 | Integración técnica directa con agencia preferida para facilitar resolución de problemas. | Media/Alta | Requerimiento funcional | Introduce una integración externa distinta a proveedores de reserva y requiere adaptador. | API oficial no verificada; no declarar implementado hasta validar. |
| RF-16 | Consultas analíticas, incluso pesadas, sobre tendencias, destinos y cancelaciones. | Alta | Requerimiento funcional | Requiere aislar la carga analítica de las transacciones y controlar acceso a datos. | CU-12: actor es equipo de análisis. |
| RF-19 | Notificar al usuario cambios relevantes reflejados en sus reservas. | Media | Requerimiento funcional | Añade un canal de salida y debe ocurrir después de confirmar el cambio. | Canales y criterio de relevancia por definir. |
| RF-20–RF-22 | Recomendar alternativas personalizadas y usar interacciones para evaluar/mejorar resultados. | Alta | Módulo avanzado Opción A | Introduce datos/features, interfaz separada y ciclo de feedback. | Algoritmo, evaluación y frecuencia de actualización pendientes. |
| RF-23, RF-24 | Compartir por enlace seguro con destinatarios sin cuenta y publicar en red social elegida. | Media | Requerimientos y ADR-001 | Afecta autorización, exposición de datos y contratos externos. | Solo lectura; caducidad, revocación y verificación del destinatario pendientes. |

## 2. Escenarios de atributos de calidad seleccionados

| ID | Escenario/meta | Prioridad | Fuente | Justificación arquitectónica | Estado / observaciones |
|---|---|---|---|---|---|
| QA-A1 | Máximo 5 minutos de indisponibilidad no planificada por mes (≈99,988 % en un mes de 30 días). | Alta | Enunciado | Condiciona redundancia, recuperación, monitoreo y despliegue. | Meta exigente; debe validarse con pruebas. RTO/RPO pendientes. |
| QA-P1 | Mostrar cambios dentro de 5 minutos desde que la fuente externa los genera. | Alta | Enunciado | Condiciona ingesta, frecuencia de sincronización, colas y alertas de atraso. | Depende de que la fuente exponga el cambio oportunamente. |
| QA-P2 | Respuesta web objetivo de 800 ms. | Alta | Enunciado | Condiciona camino de consulta, datos y aislamiento de operaciones lentas. | Definir percentil y condiciones de carga en la validación. |
| QA-P3 | FCP móvil menor a 1,4 s. | Media | Enunciado | Condiciona entrega de contenido, recursos y cliente móvil. | Verificar con prototipo y dispositivos representativos. |
| QA-P4 | Consultas analíticas pesadas no degradan operaciones de usuario. | Alta | Requerimiento de analítica | Requiere aislamiento de cargas y posiblemente almacenamiento separado. | Meta cualitativa; definir métricas de interferencia. |
| QA-P5 | Recomendaciones no bloquean el acceso al itinerario; respuesta objetivo de 3 s. | Media | Meta propuesta derivada | Favorece interfaz separada y fallback. | **3 s es supuesto propuesto, no meta explícita del enunciado.** |
| QA-S1, QA-S2 | 15 M de cuentas, 2 M de usuarios activos semanales y picos de demanda. | Alta | Enunciado | Condiciona particionado, escalado, caché, capacidad y costos. | Carga pico exacta no está fijada; escenarios 10× son supuestos. |
| QA-S3 | Ingesta de correo debe escalar sin generar una tasa insostenible de consultas. | Alta | Derivado de RF-07 y QA-P1 | El sondeo masivo puede dominar el costo/carga; favorece notificaciones cuando existan. | Estimaciones de buzones/frecuencia deben marcarse como supuestos. |
| QA-I1, QA-I2 | Integración con correo y proveedores turísticos mediante APIs disponibles. | Alta | Enunciado | Exige puertos, adaptadores, contratos y tolerancia a cambios. | Capacidad real por proveedor pendiente. |
| QA-I3 | Publicar en una red social seleccionada por el usuario. | Media | Requerimiento funcional | Integración puntual, condicionada por permisos y políticas sociales. | No asumir que la API permite publicar cualquier contenido. |
| QA-SE1 | Acceso al correo con autorización mínima, cifrado y revocación. | Alta | Enunciado / privacidad | Define identidad, almacenamiento de tokens, scopes y auditoría. | Proveedor de correo y permisos pendientes. |
| QA-SE2 | Solo destinatarios designados pueden visualizar un itinerario compartido. | Alta | Enunciado / ADR-001 | Requiere autorización segura aun sin cuenta local. | Definir cómo se verifica al destinatario; el enlace por sí solo puede reenviarse. |
| QA-SE3 | Datos analíticos y de recomendación accesibles solo a roles/tareas autorizadas. | Alta | ADR-003 y privacidad | Condiciona acceso, auditoría, minimización y desidentificación. | Retención y consentimiento por definir. |
| QA-SE4 | No conservar correos que no sean de viaje más allá de lo necesario para filtrarlos. | Media | Privacidad / flujo de correo | Reduce exposición y volumen de datos personales. | Política exacta de retención pendiente. |
| QA-E1 | Agregar nuevos medios de transporte/proveedores sin modificar el núcleo. | Alta | Enunciado | Favorece modelo canónico y adaptadores. | Contratos deben probarse. |
| QA-E2 | Mantener trazabilidad requisito → ADR → vista → especificación → código. | Media | Enunciado / spec-driven | Condiciona estructura documental y control de cambios. | Aplicar en todas las iteraciones. |
| QA-E3 | Sustituir/evolucionar recomendador sin modificar el núcleo y registrar feedback. | Media | ADR-005/006 | Favorece puerto estable y modelo de interacción separado. | No implica reentrenamiento inmediato. |
| QA-U1 | Interfaz móvil contextual con GPS y acceso práctico al itinerario. | Media | Enunciado | Condiciona cliente móvil y permisos de ubicación. | Modo sin conexión es supuesto hasta confirmarlo. |
| QA-U2 | Incorporar idiomas externalizando textos y formatos. | Media | Enunciado | Evita codificar textos en componentes. | Idiomas objetivo pendientes. |
| QA-U3 | Operar globalmente y en múltiples regiones. | Alta | Enunciado | Condiciona residencia de datos, latencia, replicación y recuperación. | Topología depende de requisitos legales/costo. |

## 3. Restricciones que condicionan la arquitectura

| ID | Restricción | Prioridad | Fuente | Efecto |
|---|---|---|---|---|
| CON-06/07 | Prototipo trazable y alcance acotado por cronograma. | Alta | Enunciado | No implementar todos los objetivos globales; demostrar un corte vertical. |
| CON-09 | Clientes web y móvil. | Alta | Enunciado | Backend/API compartidos y contratos de cliente. |
| CON-10/12 | APIs estándar de proveedores, correo y redes sociales. | Alta | Enunciado | Integrar solo capacidades ofrecidas por terceros. |
| CON-11 | Preparación multirregión. | Alta | Enunciado | No implica topología final elegida todavía. |
| CON-13 | Módulo avanzado: recomendación (Opción A). | Alta | Enunciado/ADR-005 | Debe formar parte del alcance arquitectónico. |
| CON-14/15 | Protección de datos y autorización expresa del correo. | Alta | Restricción implícita | Mínimo privilegio, control de acceso y auditoría. |

## 4. Preocupaciones que requieren resolución

| ID | Preocupación | Drivers relacionados | Estado |
|---|---|---|---|
| CRN-02 | Extracción heterogénea y deduplicación. | RF-07/RF-08, QA-P1, QA-I2 | Abierta |
| CRN-03 | Notificaciones del proveedor vs. consulta periódica. | RF-07/RF-13, QA-P1, QA-S3 | Preferir notificaciones cuando existan; fallback según API. |
| CRN-04 | Fuente de verdad y conflicto entre correo, API y edición manual. | RF-02/RF-03/RF-13 | Abierta; no asumir “último dato gana”. |
| CRN-05 | Cuotas, permisos y disponibilidad de APIs externas. | RF-11–RF-15, QA-I1/I2 | Etapa 5. |
| CRN-06 | Verificación, caducidad y revocación de enlaces. | RF-23, QA-SE2 | Abierta; solo lectura ya decidido. |
| CRN-07/08 | Retención, consentimiento, normativa y residencia regional. | RF-16, QA-SE3, QA-U3 | Abierta. |
| CRN-10 | Datos y ciclo de mejora del recomendador. | RF-20–RF-22, QA-E3 | Abierta. |
| CRN-11 | Proveedor de mapas y fallback. | QA-U1 | Abierta. |
| CRN-12/13 | Costo, observabilidad y recuperación. | QA-A1, QA-S1/S2 | Abierta. |
| CRN-15/16 | Corte vertical del prototipo y competencias del equipo. | CON-06/07 | Abierta. |

## 5. Asignación de drivers a las iteraciones

| Iteración | Objetivo | Drivers principales |
|---|---|---|
| ADD-1 | Partición de alto nivel. | RF-01/05, RF-07/08, RF-11–RF-16; QA-A1, QA-P1/P2, QA-S1/S2, QA-I1/I2, QA-E1. |
| ADD-2 | Componentes funcionales centrales. | RF-01–RF-15, RF-17–RF-19; RN-01–RN-05; QA-P1, QA-I1/I2, QA-SE1. |
| ADD-3 | Resiliencia, seguridad y escala. | QA-A1, QA-P1, QA-S1/S2/S3, QA-SE1/SE2/SE3, QA-I1/I2; CRN-05/06/07/08/12/13. |
| ADD-4 | Lecturas, analítica, recomendaciones y UX. | QA-P2/P3/P4/P5, QA-E3, QA-U1/U2/U3, RF-16, RF-20–RF-24. |

Los requisitos funcionales no listados como drivers siguen vigentes. La priorización no autoriza a descartarlos.


## 6. Escenarios complementarios y requisitos vigentes no seleccionados como drivers independientes

Estos elementos siguen siendo obligatorios. Se resuelven dentro de las estructuras y mecanismos anteriores o requieren decisiones locales, sin constituir un objetivo arquitectónico independiente en el estado actual.

| ID | Descripción | Tratamiento |
|---|---|---|
| QA-A2 | Si falla un proveedor de viajes/correo, la aplicación continúa sirviendo y resincroniza cuando se recupera. | Se aborda junto con QA-A1 mediante aislamiento de fallas, timeouts, colas y reintentos; ver ADD-3/ADR-012. |
| QA-A3 | Despliegues sin interrupción. | Se evalúa como táctica operativa ligada a disponibilidad; el mecanismo de despliegue queda pendiente de infraestructura. |
| QA-A4 | La falla del servicio de mapas no impide consultar el itinerario. | Fallback y aislamiento del adaptador de mapas; proveedor pendiente en etapa 5. |
| RF-02/RF-03/RF-04 | Registrar, actualizar y eliminar reservas manualmente. | Se implementan dentro del servicio de reservas definido en ADD-2; política de eliminación pendiente. |
| RF-06 | Archivar o retirar de la vista principal los viajes completados. | Se implementa en el servicio de viajes; definición de “completado” pendiente. |
| RF-09/RF-10 | Configurar filtros y remitentes confiables. | Se resuelve dentro del flujo de ingesta y la configuración por usuario. |
| QA-SE4 | No conservar correos irrelevantes más allá de lo necesario. | Regla de minimización/retención en el procesamiento de correo; plazo concreto pendiente. |
| QA-U1/U2 | GPS, experiencia móvil e internacionalización. | Se contemplan en ADD-4; modo offline e idiomas objetivo requieren validación. |

La ausencia de un requisito en la tabla de drivers seleccionados **no significa que pueda omitirse del análisis o del prototipo**. La selección solo identifica qué necesidades guían decisiones de arquitectura.
