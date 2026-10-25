# Escenarios de atributos de calidad — Trotamundos

Escenarios en el formato de seis partes de la cátedra (ver `Teoría Escenarios.md`): **Fuente, Estímulo, Entorno, Artefacto, Respuesta y Medida de respuesta**.

## Convenciones

| Símbolo | Significado |
|---|---|
| **Imp.** | Importancia para el negocio: **A**lta / **M**edia / **B**aja |
| **Dif.** | Dificultad o riesgo técnico de lograrlo: **A**lta / **M**edia / **B**aja |
| ⚠️ | Valor **propuesto por el equipo**, no figura en el enunciado ni en el repo. Hay que validarlo |
| Sin marca | Valor tomado del enunciado |

**Atributos:** se usan los nombres del enunciado. Equivalencias con la teoría: *Interoperabilidad* ≈ *Integrabilidad*; *Evolucionabilidad* ≈ *Modificabilidad*; *Despliegue sin downtime* ≈ *Desplegabilidad*.

## Índice

| Atributo | Escenarios |
|---|---|
| [Rendimiento y latencia](#1-rendimiento-y-latencia) | QA-P1, QA-P2, QA-P3, QA-P4, QA-P5 |
| [Disponibilidad](#2-disponibilidad) | QA-A1, QA-A2, QA-A3, QA-A4 |
| [Escalabilidad](#3-escalabilidad) | QA-S1, QA-S2, QA-S3 |
| [Interoperabilidad](#4-interoperabilidad) | QA-I1, QA-I2, QA-I3 |
| [Seguridad y privacidad](#5-seguridad-y-privacidad) | QA-SE1, QA-SE2, QA-SE3, QA-SE4 |
| [Evolucionabilidad](#6-evolucionabilidad-y-mantenibilidad) | QA-E1, QA-E2, QA-E3 |
| [Usabilidad e internacionalización](#7-usabilidad-e-internacionalización) | QA-U1, QA-U2, QA-U3 |

---

## 1. Rendimiento y latencia

### QA-P1 — Frescura de las actualizaciones de viaje

**Imp./Dif.:** A / A · **Trazabilidad:** RF-07, RF-08, RF-12, RF-13, RF-14, RF-19 · CU-07, CU-10, CU-18

| Parte | Escenario |
|---|---|
| Fuente | Proveedor turístico o proveedor de correo del usuario. |
| Estímulo | Genera un cambio en una reserva (cambio de horario, cancelación) o llega un correo con una reserva nueva. |
| Entorno | Operación normal y también en picos de carga. |
| Artefacto | Flujo de ingesta y sincronización de reservas y vista del itinerario. |
| Respuesta | El sistema detecta el cambio, valida los datos, actualiza la reserva y la refleja en el itinerario del usuario. |
| Medida de respuesta | La actualización se muestra en la aplicación **dentro de los 5 minutos** posteriores a su generación en la fuente, para el **99 %** ⚠️ de las actualizaciones. El tiempo de detección (polling, webhook o notificación) cuenta dentro de esos 5 minutos. |

### QA-P2 — Tiempo de respuesta en web

**Imp./Dif.:** A / M · **Trazabilidad:** RF-01, RF-05 · CU-01

| Parte | Escenario |
|---|---|
| Fuente | Usuario autenticado desde un navegador web. |
| Estímulo | Solicita consultar sus viajes y reservas. |
| Entorno | Carga de pico (domingo-lunes y jueves-viernes) con la base de 2 millones de usuarios activos semanales. |
| Artefacto | Servicio de consulta de viajes y reservas y su capa de acceso a datos. |
| Respuesta | El sistema recupera el itinerario y lo devuelve. |
| Medida de respuesta | Tiempo de respuesta de **800 ms** en el **percentil 95** ⚠️. El enunciado no aclara el percentil ni qué tramo se mide (backend o página completa). |

### QA-P3 — Primer despliegue de contenido en móvil

**Imp./Dif.:** M / M · **Trazabilidad:** CU-01

| Parte | Escenario |
|---|---|
| Fuente | Usuario autenticado desde un dispositivo móvil. |
| Estímulo | Abre la aplicación para consultar sus viajes. |
| Entorno | Red móvil 4G ⚠️, operación normal y pico. |
| Artefacto | Cliente móvil y los servicios que le entregan el contenido inicial. |
| Respuesta | La aplicación presenta el primer contenido útil (viaje activo o próximas reservas). |
| Medida de respuesta | **First Contentful Paint inferior a 1,4 segundos** en el **percentil 75** ⚠️. |

### QA-P4 — Aislamiento de la carga analítica

**Imp./Dif.:** A / A · **Trazabilidad:** RF-16 · CU-12 · ADR-003

| Parte | Escenario |
|---|---|
| Fuente | Equipo de análisis de datos. |
| Estímulo | Ejecuta consultas analíticas pesadas sobre el histórico (tendencias, destinos, cancelaciones). |
| Entorno | Horario de pico operativo. |
| Artefacto | Subsistema analítico y su almacenamiento de datos. |
| Respuesta | Las consultas se ejecutan sobre recursos aislados de los que atienden las operaciones de los usuarios. |
| Medida de respuesta | Se siguen cumpliendo **QA-P1 y QA-P2**; el p95 de las operaciones de usuario varía **a lo sumo 5 %** ⚠️ mientras corren las consultas. |

### QA-P5 — Recomendaciones sin afectar al núcleo

**Imp./Dif.:** M / M ⚠️ · **Trazabilidad:** RF-20, RF-21, RF-22 · CU-13, CU-14 · ADR-005

| Parte | Escenario |
|---|---|
| Fuente | Usuario autenticado. |
| Estímulo | Solicita recomendaciones o ajusta los parámetros de una recomendación. |
| Entorno | Carga de pico. |
| Artefacto | Módulo de recomendación. |
| Respuesta | El módulo genera y presenta las alternativas sin competir por los recursos del núcleo de consulta de viajes. |
| Medida de respuesta | Las recomendaciones se presentan en **3 segundos** o menos en el p95 ⚠️ (o se entregan de forma asíncrona si el cálculo lo requiere) y **QA-P2 no se degrada**. |

---

## 2. Disponibilidad

### QA-A1 — Falla de infraestructura

**Imp./Dif.:** A / A · **Trazabilidad:** todo el sistema

| Parte | Escenario |
|---|---|
| Fuente | Infraestructura que aloja el sistema. |
| Estímulo | Falla un nodo, una zona de disponibilidad o una región completa. |
| Entorno | Operación normal, con uso global las 24 horas. |
| Artefacto | Plataforma completa (cómputo, datos y mensajería). |
| Respuesta | El sistema detecta la falla y redirige el tráfico a recursos sanos con failover automático, sin intervención manual y sin perder datos confirmados. |
| Medida de respuesta | **Máximo 5 minutos de inactividad no planificada por mes** (≈ 99,988 % de disponibilidad). **RTO ≤ 60 s** y **RPO ≤ 1 min** ⚠️ por incidente. |

### QA-A2 — Falla de un proveedor externo de viajes o de correo

**Imp./Dif.:** A / M · **Trazabilidad:** RF-11 a RF-14 · CU-07, CU-10

| Parte | Escenario |
|---|---|
| Fuente | Proveedor turístico o proveedor de correo. |
| Estímulo | Deja de responder, devuelve errores o limita las solicitudes. |
| Entorno | Operación normal. |
| Artefacto | Módulos de integración con proveedores. |
| Respuesta | El sistema registra el fallo, reintenta con espera creciente y no sobrescribe datos válidos con información inconsistente. El itinerario sigue mostrando los últimos datos conocidos, indicando que pueden estar desactualizados. Al recuperarse el proveedor, se resincroniza. |
| Medida de respuesta | **100 %** de las consultas de usuario siguen funcionando; **0 actualizaciones perdidas**; resincronización completa en **5 minutos** ⚠️ luego de la recuperación. |

### QA-A3 — Despliegue sin interrupción

**Imp./Dif.:** M / M · **Trazabilidad:** todo el sistema

| Parte | Escenario |
|---|---|
| Fuente | Pipeline de despliegue del equipo. |
| Estímulo | Se publica una nueva versión de un servicio. |
| Entorno | Producción, con usuarios activos. |
| Artefacto | Servicio afectado y su proceso de despliegue. |
| Respuesta | El sistema despliega de forma gradual, verifica la nueva versión y revierte automáticamente si falla. |
| Medida de respuesta | **0 minutos** de interrupción perceptible; reversión automática en **2 minutos** o menos ⚠️ cuando falla la verificación. |

### QA-A4 — Falla del servicio de mapas

**Imp./Dif.:** M / B · **Trazabilidad:** ADR-004

| Parte | Escenario |
|---|---|
| Fuente | Servicio externo de mapas y navegación. |
| Estímulo | No está disponible, excede el tiempo de espera o se superan los límites de uso. |
| Entorno | Usuario consultando un viaje desde el móvil. |
| Artefacto | Integración con el servicio de mapas. |
| Respuesta | Las funciones que no dependen de mapas siguen operando; la información geográfica se reemplaza por datos textuales o por la ubicación del GPS, con un aviso al usuario. |
| Medida de respuesta | **100 %** de las funciones no geográficas siguen operando; el reemplazo se presenta dentro de **2 segundos** ⚠️ del tiempo de espera. |

---

## 3. Escalabilidad

### QA-S1 — Carga base sostenida

**Imp./Dif.:** A / M · **Trazabilidad:** todo el sistema

| Parte | Escenario |
|---|---|
| Fuente | Usuarios de la plataforma. |
| Estímulo | 2 millones de usuarios activos por semana, de una base de 15 millones de cuentas, con picos domingo-lunes y jueves-viernes. |
| Entorno | Operación normal con picos semanales previsibles. |
| Artefacto | Sistema completo. |
| Respuesta | El sistema absorbe la carga ajustando sus recursos sin intervención manual. |
| Medida de respuesta | Se cumplen **QA-P1, QA-P2 y QA-P3** durante los picos; el crecimiento de la base de cuentas no degrada los tiempos de respuesta. |

### QA-S2 — Pico por evento disruptivo masivo

**Imp./Dif.:** A / A · **Trazabilidad:** todo el sistema

| Parte | Escenario |
|---|---|
| Fuente | Evento disruptivo masivo (por ejemplo, clima o cierre de espacio aéreo). |
| Estímulo | Aumento brusco de consultas de usuarios (**10 veces el pico habitual en menos de 10 minutos** ⚠️) junto con una avalancha de actualizaciones de proveedores. |
| Entorno | Ya en un pico semanal. |
| Artefacto | Sistema completo: consulta, ingesta y notificaciones. |
| Respuesta | El sistema escala horizontalmente, prioriza las funciones críticas (consultar el itinerario y recibir cambios) y degrada de forma controlada las no críticas (analítica, recomendaciones). |
| Medida de respuesta | Se mantiene **QA-P2 (800 ms)** o se relaja hasta **1,5 s** ⚠️; **QA-P1** se cumple para al menos el **95 %** ⚠️ de las actualizaciones; **0 datos perdidos**; capacidad ampliada en **5 minutos** o menos ⚠️. |

### QA-S3 — Ingesta de correo a escala

**Imp./Dif.:** A / A · **Trazabilidad:** RF-07, RF-08 · CU-07

| Parte | Escenario |
|---|---|
| Fuente | Proveedores de correo y planificador de procesamiento. |
| Estímulo | Millones de buzones conectados deben procesarse dentro de la ventana de frescura, con ráfagas de correos de viaje (estimación en `Preocupaciones.md`, CRN-03). |
| Entorno | Operación normal y pico. |
| Artefacto | Flujo de procesamiento de correo. |
| Respuesta | El procesamiento se reparte en paralelo con colas y control de contrapresión; los workers escalan según la demanda; el procesamiento es idempotente. |
| Medida de respuesta | Antigüedad del backlog de **2 minutos** o menos en el p99 ⚠️; **0 correos perdidos**; **0 reservas duplicadas** por reprocesamiento. |

---

## 4. Interoperabilidad

### QA-I1 — Integración con proveedores turísticos

**Imp./Dif.:** A / M · **Trazabilidad:** RF-11, RF-12, RF-13, RF-14 · CU-10

| Parte | Escenario |
|---|---|
| Fuente | Proveedor turístico (aerolínea, hotel, rentadora, etc.). |
| Estímulo | Entrega detalles, actualizaciones o cancelaciones de una reserva mediante su API estándar. |
| Entorno | Operación normal; el proveedor cumple su contrato. |
| Artefacto | Adaptador del proveedor y modelo interno de reservas. |
| Respuesta | El adaptador valida la respuesta, la traduce al modelo interno y actualiza la reserva. Los mensajes inválidos se descartan sin sobrescribir datos y quedan registrados. |
| Medida de respuesta | **100 %** de los casos válidos de la batería de integración se traducen correctamente; **100 %** de los inválidos se rechazan según el contrato; procesamiento idempotente. |

### QA-I2 — Proveedores de correo

**Imp./Dif.:** A / M · **Trazabilidad:** RF-07, RF-08, RF-17 · CU-07, CU-17

| Parte | Escenario |
|---|---|
| Fuente | Proveedor de correo y usuario que conecta su cuenta. |
| Estímulo | El usuario autoriza el acceso a su correo y el proveedor entrega o notifica mensajes nuevos. |
| Entorno | Operación normal. |
| Artefacto | Módulo de acceso a correo. |
| Respuesta | El acceso se realiza mediante una interfaz común sobre protocolos o APIs estándar; el procesamiento posterior no depende del proveedor concreto. |
| Medida de respuesta | Agregar un proveedor de correo **no exige modificar** el flujo de extracción y registro de reservas; **al menos 1** proveedor real en el prototipo ⚠️ (pendiente de selección). |

### QA-I3 — Publicación en redes sociales

**Imp./Dif.:** M / B · **Trazabilidad:** RF-24 · CU-16 · ADR-001

| Parte | Escenario |
|---|---|
| Fuente | Usuario autenticado. |
| Estímulo | Confirma la publicación de un itinerario en una red social elegida (una por publicación). |
| Entorno | Operación normal, con la integración autorizada. |
| Artefacto | Módulo de compartición en redes sociales. |
| Respuesta | El sistema prepara la publicación solo con el contenido seleccionado y la envía a la red. |
| Medida de respuesta | La publicación se considera realizada **únicamente si la red la confirma**; **0 datos no seleccionados** incluidos; **al menos 1** red en el prototipo ⚠️. |

---

## 5. Seguridad y privacidad

### QA-SE1 — Acceso seguro y autorizado al correo

**Imp./Dif.:** A / M · **Trazabilidad:** RF-17, RF-18 · CU-17

| Parte | Escenario |
|---|---|
| Fuente | Usuario propietario del buzón o un atacante. |
| Estímulo | El usuario autoriza el acceso a su correo y luego lo revoca; un atacante intenta obtener las credenciales almacenadas. |
| Entorno | Operación normal. |
| Artefacto | Gestión de autorizaciones y credenciales de acceso al correo. |
| Respuesta | El sistema usa autorización delegada con permisos mínimos de solo lectura, almacena las credenciales cifradas, registra cada acceso y deja de acceder al buzón cuando se revoca. |
| Medida de respuesta | **0 accesos** al buzón luego de la revocación (propagación en **1 minuto** o menos ⚠️); **100 %** de las credenciales cifradas en reposo; **100 %** de los accesos registrados. |

### QA-SE2 — Acceso restringido a itinerarios compartidos

**Imp./Dif.:** A / M · **Trazabilidad:** RF-23 · CU-15 · ADR-001

| Parte | Escenario |
|---|---|
| Fuente | Destinatario designado o persona no designada que obtiene el enlace. |
| Estímulo | Intenta acceder al itinerario mediante el enlace seguro recibido por correo. |
| Entorno | Operación normal; los destinatarios no necesitan cuenta de Trotamundos y no pueden editar. |
| Artefacto | Servicio de compartición y autorización de enlaces. |
| Respuesta | El sistema verifica que quien accede es un destinatario designado y que el enlace sigue vigente; permite solo lectura; deniega y registra cualquier otro intento. |
| Medida de respuesta | **100 %** de los accesos no autorizados se deniegan y registran; los enlaces no son predecibles ni adivinables; revocación efectiva en **1 minuto** o menos ⚠️; caducidad por defecto de **30 días** ⚠️. El mecanismo concreto de autorización queda **pendiente** (ADR-001). |

### QA-SE3 — Control de acceso a datos para analítica y recomendación

**Imp./Dif.:** A / M · **Trazabilidad:** RF-16, RF-20 a RF-22 · ADR-003, ADR-006

| Parte | Escenario |
|---|---|
| Fuente | Integrante del equipo de análisis o proceso del módulo de recomendación. |
| Estímulo | Accede a datos de viajes, reservas, preferencias e interacciones. |
| Entorno | Operación normal. |
| Artefacto | Plataforma de datos y almacenamiento de información personal. |
| Respuesta | Por defecto se entregan datos agregados o desidentificados; el acceso a datos individuales solo se concede por rol y para tareas autorizadas, queda registrado, y las recomendaciones de un usuario no exponen datos de otros. |
| Medida de respuesta | **100 %** de los accesos a datos individuales tienen autorización por rol y quedan auditados; **0 datos identificables** en los conjuntos analíticos estándar ⚠️; **0 exposición de datos entre usuarios** en las pruebas del recomendador. |

### QA-SE4 — Minimización de datos del correo

**Imp./Dif.:** M / B · **Trazabilidad:** RF-07, RF-09, RF-10 · CU-07, CU-08, CU-09

| Parte | Escenario |
|---|---|
| Fuente | Flujo de procesamiento de correo. |
| Estímulo | Llegan correos que no son de viaje o que no cumplen los filtros y whitelists del usuario. |
| Entorno | Operación normal. |
| Artefacto | Filtro de ingesta. |
| Respuesta | Los correos descartados no se conservan; de los correos de viaje solo se guardan los datos de la reserva. |
| Medida de respuesta | **0 correos** no relacionados con viajes se conservan; los cambios en filtros y whitelists se aplican en **1 minuto** o menos ⚠️. |

---

## 6. Evolucionabilidad y mantenibilidad

### QA-E1 — Incorporación de un nuevo medio de transporte

**Imp./Dif.:** A / M · **Trazabilidad:** RF-01, RF-11

| Parte | Escenario |
|---|---|
| Fuente | Equipo de desarrollo. |
| Estímulo | Se solicita soportar un nuevo medio de transporte (por ejemplo, trenes o autobuses). |
| Entorno | El sistema está en producción y debe conservar sus integraciones actuales. |
| Artefacto | Modelo de reservas, integraciones e interfaz de usuario. |
| Respuesta | El equipo agrega el nuevo tipo de reserva mediante un punto de extensión (adaptador, esquema y vista), sin cambiar la lógica de los tipos existentes. |
| Medida de respuesta | Se completa en **10 días-persona** o menos ⚠️; **0 modificaciones** en los componentes de los tipos existentes, salvo su registro; la regresión de los tipos existentes pasa. |

### QA-E2 — Trazabilidad y contratos (Spec-driven)

**Imp./Dif.:** M / B · **Trazabilidad:** CON-05, CON-06

| Parte | Escenario |
|---|---|
| Fuente | Equipo de desarrollo o evaluador. |
| Estímulo | Cambia un requisito o se revisa una decisión de diseño. |
| Entorno | Diseño y desarrollo del prototipo. |
| Artefacto | ADRs, vistas, especificaciones y código. |
| Respuesta | Se identifica el impacto siguiendo la cadena requisito → driver → ADR → vista → especificación → código. |
| Medida de respuesta | **100 %** de los ADRs referencian al menos un driver; **100 %** de las interfaces del prototipo tienen una especificación verificada por pruebas de contrato; el impacto de un cambio se identifica en **30 minutos** o menos ⚠️. |

### QA-E3 — Evolución del modelo de recomendación

**Imp./Dif.:** M / M ⚠️ · **Trazabilidad:** RF-22 · CU-14 · ADR-005, ADR-006

| Parte | Escenario |
|---|---|
| Fuente | Equipo de datos o de desarrollo. |
| Estímulo | Se necesita actualizar o reemplazar el modelo de recomendación, o incorporar nuevas señales de interacción. |
| Entorno | Sistema en producción. |
| Artefacto | Módulo de recomendación y su interfaz con el resto del sistema. |
| Respuesta | Se cambia el modelo detrás de una interfaz estable. Las interacciones del usuario (aceptar o ajustar) quedan registradas y disponibles para refinarlo. |
| Medida de respuesta | **0 cambios** en componentes fuera del módulo de recomendación; el cambio se aplica **sin interrupción**; **100 %** de las interacciones de aceptar o ajustar se registran ⚠️. |

---

## 7. Usabilidad e internacionalización

### QA-U1 — Experiencia móvil con GPS

**Imp./Dif.:** M / M · **Trazabilidad:** ADR-004

| Parte | Escenario |
|---|---|
| Fuente | Usuario en un dispositivo móvil, de viaje. |
| Estímulo | Abre su viaje en curso. |
| Entorno | Conectividad variable; GPS disponible o no. |
| Artefacto | Aplicación móvil. |
| Respuesta | La aplicación muestra información contextual (próxima reserva, cómo llegar) usando la ubicación del dispositivo con permiso del usuario. Sin GPS o sin conexión sigue mostrando los datos del viaje en curso. |
| Medida de respuesta | La ubicación se usa **solo con permiso explícito**; la próxima reserva se alcanza en **2 toques** o menos ⚠️; los datos del viaje en curso están disponibles sin conexión ⚠️. |

### QA-U2 — Internacionalización y localización

**Imp./Dif.:** M / M

| Parte | Escenario |
|---|---|
| Fuente | Usuario de otro país o idioma. |
| Estímulo | Usa la aplicación con una configuración regional distinta. |
| Entorno | Operación normal. |
| Artefacto | Interfaces web y móvil y servicios que entregan fechas, horas y montos. |
| Respuesta | Textos, fechas, monedas y zonas horarias se presentan localizados; la hora de cada reserva se muestra en la zona horaria del lugar. |
| Medida de respuesta | Agregar un idioma requiere **solo archivos de recursos** (0 cambios de código); **100 %** de los textos están externalizados. |

### QA-U3 — Operación multirregión

**Imp./Dif.:** A / A

| Parte | Escenario |
|---|---|
| Fuente | Usuarios en distintas regiones del mundo. |
| Estímulo | Acceden al sistema desde sus regiones. |
| Entorno | Operación normal y pico. |
| Artefacto | Despliegue del sistema y estrategia de ubicación de datos. |
| Respuesta | El tráfico se atiende desde la región más cercana, los datos personales residen en la región que corresponde y se puede sumar una región nueva sin cambios de código. |
| Medida de respuesta | **QA-P2 y QA-P3** se cumplen en todas las regiones soportadas; **0 datos personales** fuera de su región asignada sin consentimiento ⚠️. |

> ⚠️ **Tensión a resolver en ADD:** QA-U3 (ubicación de los datos) frente a QA-A1 (disponibilidad global) y QA-SE2 (itinerarios compartidos con destinatarios de otras regiones).
