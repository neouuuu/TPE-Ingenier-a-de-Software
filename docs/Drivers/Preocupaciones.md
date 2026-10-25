# Preocupaciones (concerns) — Trotamundos

Una **preocupación** es un tema relevante para los interesados que influye en el diseño aunque todavía no esté expresado como requisito medible. Varias salen de las **cuestiones pendientes** que ya dejaron los ADR del repo.

**Estado:** *Abierta* = hay que decidirla en el ADD; *Parcial* = ya hay una decisión pero falta detalle; *Supuesto* = se asume algo hasta confirmarlo.

| ID | Preocupación | Origen | Se vincula con | Estado |
|---|---|---|---|---|
| **CRN-01** | **Estructura general desde cero.** No hay arquitectura previa: la primera iteración debe definir la partición del sistema (estilo y módulos principales) que sostenga los drivers prioritarios. | Análisis inicial | Todos | Supuesto: sistema nuevo (*greenfield*) |
| **CRN-02** | **Calidad de la extracción y duplicados.** Los correos de viaje son heterogéneos (formatos, idiomas, proveedores). Una misma reserva puede llegar varias veces o por varios caminos. La regla de deduplicación está pendiente y un correo con datos insuficientes no debe generar una reserva incompleta. | CU-07 (alternativas) | RF-07, RF-08 · QA-S3, QA-I2 | Abierta |
| **CRN-04** | **Una única fuente de verdad.** Una reserva puede llegar por correo, por la API del proveedor o cargarse a mano. Hay que decidir qué fuente prevalece y qué pasa cuando el usuario edita una reserva que el proveedor luego actualiza. | RF-02/03, RF-08, RF-13; CU-10 | CU-01, CU-02, CU-03, CU-10 · QA-P1 | Abierta |
| **CRN-05** | **Condiciones de terceros.** Falta elegir el proveedor de correo y saber qué APIs reales de viajes se podrán usar en el prototipo. Cada proveedor impone cuotas, requisitos de verificación de aplicaciones y permisos de acceso al correo. | Resumen del sistema §4 | QA-I1, QA-I2, QA-SE1 · CON-T3 | Abierta |
| **CRN-06** | **Autorización de los enlaces compartidos.** Los destinatarios no tienen cuenta, así que hay que decidir cómo se verifica que son los designados, cuánto dura el enlace, cómo se revoca y qué permisos da. La publicación en redes depende de las políticas de cada plataforma, y su visibilidad no siempre la controla Trotamundos. | ADR-001, CU-15 | RF-23, RF-24 · QA-SE2, QA-I3 | Abierta |
| **CRN-07** | **Política de datos personales.** Faltan definir permisos, controles de acceso y trazabilidad para el equipo de análisis, los plazos de conservación, la desidentificación y el consentimiento del usuario para usar sus datos con fines analíticos. | ADR-003 | RF-16 · QA-SE3 | Parcial |
| **CRN-08** | **Normativa y ubicación de los datos.** Operar en varias regiones puede obligar a que los datos personales residan en la región del usuario, lo que complica la replicación, la disponibilidad global y las compartidas entre regiones. | Enunciado (multirregión) · CON-14 | QA-U3, QA-A1, QA-SE2 | Abierta |
| **CRN-09** | **Ciclo de vida del viaje.** Falta definir cuándo un viaje se considera completado (zonas horarias, viajes con varias etapas, reservas sueltas), quién lo archiva (usuario o proceso automático), qué se conserva y cuál es la política de eliminación de reservas. | CU-04, CU-06, RF-06 | CU-06 | Abierta |
| **CRN-10** | **Diseño del recomendador.** Falta definir qué datos necesita y cómo accede a ellos, qué interacciones se registran y por cuánto tiempo, cómo se refina el modelo (parámetros, análisis periódico o reentrenamiento), cómo evitar que las señales registradas degraden las recomendaciones y qué pasa con usuarios sin historial. | ADR-005, ADR-006 | RF-20 a RF-22 · QA-P5, QA-E3, QA-SE3 | Abierta |
| **CRN-11** | **Servicio de mapas.** Falta elegir el proveedor, conocer sus límites de uso y definir el comportamiento cuando no esté disponible. También hay que tratar con cuidado los datos de ubicación del usuario. | ADR-004 | QA-A4, QA-U1 | Abierta |
| **CRN-12** | **Costo de infraestructura.** Para una startup, sostener 2 M de usuarios activos con picos de 10× puede ser muy caro si no se ajusta la capacidad a la demanda. | Enunciado | QA-S1, QA-S2 | Abierta |
| **CRN-13** | **Observabilidad y operación.** Con un presupuesto de 5 min/mes de inactividad, hay que detectar fallas casi de inmediato: monitoreo, alertas y procedimientos de recuperación forman parte del diseño. | Enunciado | QA-A1, QA-A3 | Abierta |
| **CRN-14** | **Conectividad durante el viaje.** El usuario puede estar sin conexión o con roaming caro cuando más necesita su itinerario. | Enunciado (interfaz móvil) | QA-U1 | Supuesto: soporte sin conexión para el viaje en curso |
| **CRN-15** | **Alcance del prototipo.** Hay que decidir qué porción vertical se implementa para demostrar los drivers en el tiempo disponible, y dejar escrito qué queda fuera. Que funcione en una demostración acotada no demuestra la escala global ni la disponibilidad real. | Enunciado §2, §5 · Teoría ADD §9 | CON-06, CON-07 | Abierta |
| **CRN-16** | **Competencias y tiempo del equipo.** Las tecnologías y patrones elegidos deben poder implementarse dentro del cronograma. | Enunciado §2 | Todos | Abierta |

## Estimación de carga (orden de magnitud)

Sirve para justificar CRN-03 y los escenarios QA-S1, QA-S2 y QA-S3. **Todos los parámetros marcados con ⚠️ son supuestos** del equipo, no datos del enunciado.

| Parámetro | Valor | Resultado |
|---|---|---|
| Usuarios activos semanales | 2 M | |
| Sesiones por usuario activo por semana ⚠️ | 4 | 8 M sesiones por semana |
| Parte de las sesiones en los 4 días pico ⚠️ | 70 % | ≈ 1,4 M sesiones en un día pico |
| Parte del día en la hora pico ⚠️ | 15 % | ≈ 210 mil sesiones en esa hora ≈ **58 sesiones/s** |
| Solicitudes por sesión ⚠️ | 10 | ≈ **580 solicitudes/s** en pico habitual |
| Evento disruptivo ⚠️ | 10× | ≈ **5.800 solicitudes/s** |
| Cuentas con buzón conectado ⚠️ | 30 % de 15 M | 4,5 M buzones |
| Sondeo cada 2 minutos para cumplir los 5 minutos de QA-P1 ⚠️ | | ≈ **37.500 consultas/s** |

**Lectura:** el costo dominante no es consultar el itinerario, sino **escanear el correo**. Con sondeo puro serían decenas de miles de consultas por segundo solo para detectar correos nuevos, de ahí que QA-S3 se marque como ASR y que CRN-03 pida comparar consulta periódica y notificaciones de los proveedores.

**Disponibilidad:** un mes de 30 días tiene 43.200 minutos. 5 minutos equivalen a una disponibilidad objetivo de **≈ 99,988 %**. Un solo incidente con recuperación lenta puede consumir todo el presupuesto mensual, por lo que se necesita failover automático (QA-A1).
