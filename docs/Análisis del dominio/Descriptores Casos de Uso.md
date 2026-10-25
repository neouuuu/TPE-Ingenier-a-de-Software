
@startuml
left to right direction

actor Usuario
actor "Servicio de correo" as Mail
actor "Proveedor turístico" as Provider
actor "Agencia preferida" as Agency
actor "Red social" as Social
actor "Equipo de análisis de datos" as Analytics

rectangle "Sistema de gestión de viajes" {
  usecase "CU-01\nConsultar viajes y reservas" as CU01
  usecase "CU-02\nRegistrar reserva manual" as CU02
  usecase "CU-03\nActualizar reserva manual" as CU03
  usecase "CU-04\nEliminar reserva manual" as CU04
  usecase "CU-05\nOrganizar reservas e itinerarios" as CU05
  usecase "CU-06\nArchivar viajes completados" as CU06
  usecase "CU-07\nProcesar correos e importar reservas" as CU07
  usecase "CU-08\nConfigurar filtros de correo" as CU08
  usecase "CU-09\nGestionar remitentes seguros" as CU09
  usecase "CU-10\nSincronizar información de reservas" as CU10
  usecase "CU-11\nContactar agencia preferida" as CU11
  usecase "CU-12\nConsultar analítica de viajes" as CU12
  usecase "CU-13\nObtener recomendaciones" as CU13
  usecase "CU-14\nAjustar recomendaciones" as CU14
  usecase "CU-15\nCompartir itinerario por correo" as CU15
  usecase "CU-16\nPublicar itinerario en red social" as CU16
  usecase "CU-17\nGestionar acceso a la cuenta de correo" as CU17
  usecase "CU-18\nNotificar cambios en reservas" as CU18
}

Usuario -- CU01
Usuario -- CU02
Usuario -- CU03
Usuario -- CU04
Usuario -- CU05
Usuario -- CU06
Usuario -- CU08
Usuario -- CU09
Usuario -- CU11
Usuario -- CU13
Usuario -- CU14
Usuario -- CU15
Usuario -- CU16
Usuario -- CU17
CU18 -- Usuario

Mail -- CU07
Provider -- CU10
Agency -- CU11
Mail -- CU15
Mail -- CU17
Analytics -- CU12
Social -- CU16

@enduml


CU-01 — Consultar viajes y reservas
- Actor principal: Usuario.
- RF asociados: RF-01, RF-05.
- Precondición: el usuario tiene acceso a sus datos.
- Flujo principal:
  1. El usuario solicita consultar sus viajes.
  2. El sistema presenta los viajes disponibles.
  3. El usuario selecciona un viaje.
  4. El sistema muestra sus reservas y elementos del itinerario.
  5. El usuario puede consultar los detalles de una reserva.
- Alternativas: si no existen viajes, reservas o elementos del itinerario, el sistema informa que no hay resultados.
- Postcondición: la información se muestra sin modificarla.

CU-02 — Registrar reserva manual
- Actor principal: Usuario.
- RF asociado: RF-02.
- Precondición: el usuario tiene acceso al sistema.
- Flujo principal:
  1. El usuario solicita registrar una reserva.
  2. El sistema presenta los campos necesarios.
  3. El usuario introduce los datos.
  4. Opcionalmente, selecciona un viaje existente.
  5. El sistema valida los datos y la asociación, si existe.
  6. El sistema guarda la reserva y confirma el resultado.
- Alternativas: ante datos inválidos, el sistema solicita corregirlos. Si no se selecciona un viaje, la reserva queda sin asignar.
- Postcondición: la reserva queda registrada y asociada a cero o un viaje (RN-01, RN-03).

CU-03 — Actualizar reserva manual
- Actor principal: Usuario.
- RF asociado: RF-03.
- Precondición: existe una reserva que el usuario puede modificar.
- Flujo principal:
  1. El usuario selecciona una reserva.
  2. El sistema muestra sus datos actuales.
  3. El usuario modifica los campos deseados.
  4. Si corresponde, cambia su asociación con un viaje o la elimina.
  5. El sistema valida y guarda los cambios.
  6. El sistema confirma la actualización.
- Alternativas: si la reserva no existe o los datos son inválidos, no se completa la operación.
- Postcondición: la reserva queda actualizada sin violar la regla de asignación única (RN-01).

CU-04 — Eliminar reserva manual
- Actor principal: Usuario.
- RF asociado: RF-04.
- Precondición: existe una reserva que el usuario puede eliminar.
- Flujo principal:
  1. El usuario selecciona una reserva.
  2. El sistema presenta la opción de eliminarla.
  3. El usuario confirma la operación, si se requiere confirmación.
  4. El sistema elimina la reserva.
  5. El sistema informa el resultado.
- Alternativas: si la reserva no existe, el sistema informa que no puede eliminarla.
- Postcondición: la reserva deja de formar parte de los registros activos según la política de eliminación definida.

CU-05 — Organizar reservas e itinerarios
- Actor principal: Usuario.
- RF asociado: RF-05.
- Precondición: existe una reserva registrada y el usuario puede gestionar viajes.
- Flujo principal:
  1. El usuario selecciona una reserva pendiente o un viaje.
  2. El sistema muestra los viajes disponibles.
  3. El usuario elige un viaje existente o, si está permitido, inicia la creación de uno nuevo.
  4. El sistema valida la asociación.
  5. El sistema vincula la reserva al viaje seleccionado.
  6. El sistema actualiza la vista del viaje y confirma la operación.
- Alternativas: si el usuario cancela, no se modifica la asociación. Si el viaje ya no existe, se solicita elegir otro. Si la reserva pertenece a otro viaje, el sistema permite cambiar su asignación únicamente si la operación está admitida.
- Postcondición: la reserva pertenece a un único viaje como máximo (RN-01, RN-05).

CU-06 — Archivar viajes completados
- Actor principal: Usuario o proceso automático del sistema, según las reglas del enunciado.
- RF asociado: RF-06.
- Precondición: un viaje cumple las condiciones para considerarse completado.
- Flujo principal:
  1. El sistema identifica el viaje completado.
  2. Determina qué elementos deben archivarse o retirarse de la vista principal.
  3. Actualiza su estado o visibilidad.
  4. Conserva los datos necesarios para su consulta posterior.
- Alternativas: si el viaje no cumple las condiciones de finalización, no se archiva.
- Postcondición: el viaje deja de aparecer en la vista principal conforme a la política de archivo.

CU-07 — Procesar correos e importar reservas
- Actor principal: proceso automático del sistema.
- Actor secundario: Servicio de correo.
- RF asociados: RF-07, RF-08.
- Precondición: el usuario autorizó el acceso a su cuenta de correo (CU-17) y no lo revocó.
- Flujo principal:
  1. El sistema obtiene los correos que debe procesar (por consulta periódica o por notificación del proveedor, según se defina en el diseño).
  2. Identifica aquellos relacionados con viajes mediante los criterios configurados.
  3. Extrae la información de las reservas reconocidas.
  4. Valida los datos extraídos.
  5. Registra las reservas identificadas.
  6. Deja sin asignar las reservas que no tienen un viaje determinado de forma válida.
  7. Registra el resultado del procesamiento.
- Alternativas: si el usuario revocó el acceso, no se procesan sus correos. Si el servicio no está disponible, se registra el fallo. Si un correo no contiene información suficiente, no se crea una reserva incompleta como si fuera válida. Los duplicados deben tratarse conforme a una regla de deduplicación.
- Postcondición: las reservas reconocidas quedan registradas sin asignaciones automáticas no justificadas (RN-03, RN-04). Si las reservas se agregaron o cambiaron, se notifica al usuario (CU-18).

CU-08 — Configurar filtros de correo
- Actor principal: Usuario.
- RF asociado: RF-09.
- Precondición: el usuario puede acceder a la configuración.
- Flujo principal:
  1. El usuario solicita configurar filtros.
  2. El sistema presenta los criterios disponibles.
  3. El usuario establece o modifica los criterios.
  4. El sistema valida y guarda la configuración.
  5. El sistema confirma los cambios.
- Alternativas: si los criterios son inválidos, se solicita su corrección.
- Postcondición: los filtros quedan configurados para los procesos de correo posteriores.

CU-09 — Gestionar remitentes seguros
- Actor principal: Usuario.
- RF asociado: RF-10.
- Precondición: el usuario tiene acceso a la configuración de remitentes.
- Flujo principal:
  1. El usuario consulta la lista actual.
  2. Selecciona agregar, modificar o quitar un remitente.
  3. Introduce o modifica los datos.
  4. El sistema valida la entrada.
  5. El sistema actualiza la lista.
  6. El sistema confirma la operación.
- Alternativas: si el remitente es inválido o ya está registrado, el sistema informa la situación y evita inconsistencias.
- Postcondición: la lista queda actualizada.

CU-10 — Sincronizar información de reservas
- Actor principal: proceso del sistema.
- Actor secundario: Proveedor turístico.
- RF asociados: RF-11, RF-12, RF-13, RF-14.
- Precondición: el proveedor dispone de una interfaz compatible y existe una reserva que puede consultarse.
- Flujo principal:
  1. El sistema solicita información al proveedor.
  2. El proveedor devuelve los detalles y el estado de la reserva.
  3. El sistema valida la respuesta.
  4. Actualiza los datos de la reserva.
  5. Si se informa una cancelación, actualiza el estado correspondiente.
  6. Registra el resultado de la sincronización.
- Alternativas: si la interfaz no está disponible o devuelve información inválida, el sistema registra el fallo y evita sobrescribir los datos con información inconsistente.
- Postcondición: la información local queda actualizada con los datos válidos recibidos. Si hay cambios relevantes, se notifica al usuario (CU-18).

CU-11 — Contactar agencia preferida
- Actor principal: Usuario.
- Actor secundario: Agencia preferida.
- RF asociado: RF-15.
- Precondición: el usuario tiene configurada una agencia y existe una integración compatible.
- Flujo principal:
  1. El usuario solicita ayuda con un problema de viaje.
  2. El sistema identifica la agencia configurada.
  3. El sistema prepara la información necesaria.
  4. Envía la solicitud o inicia el mecanismo de contacto disponible.
  5. Informa al usuario del resultado.
- Alternativas: si no hay agencia configurada o la integración falla, el sistema informa que no pudo iniciar el contacto.
- Postcondición: la solicitud queda iniciada cuando la integración lo permite; no se presupone que el problema esté resuelto automáticamente.

CU-12 — Consultar analítica de viajes
- Actor principal: Equipo de análisis de datos.
- RF asociado: RF-16.
- Precondición: la persona del equipo tiene autorización para los datos que necesita (ADR-003) y existen datos de viajes disponibles para analizar.
- Flujo principal:
  1. La persona del equipo solicita un análisis (tendencias, destinos o cancelaciones).
  2. El sistema verifica que esté autorizada para los datos solicitados.
  3. El sistema obtiene los datos, usando datos agregados o desidentificados cuando son suficientes.
  4. El sistema ejecuta la consulta analítica.
  5. El sistema entrega los resultados.
  6. El sistema registra el acceso.
- Alternativas: si no está autorizada, el sistema rechaza la solicitud. Si no hay datos suficientes, el sistema informa la limitación.
- Postcondición: los resultados se entregan sin modificar los registros originales y el acceso queda registrado.
- Nota de cambio: antes el actor principal era el Usuario. Se cambió para alinear el caso de uso con el enunciado (datos analíticos para el equipo de datos) y con el ADR-003.

CU-13 — Obtener recomendaciones
- Actor principal: Usuario.
- RF asociados: RF-20, RF-21.
- Precondición: existe información suficiente del historial o las preferencias del usuario para generar recomendaciones.
- Flujo principal:
  1. El usuario solicita recomendaciones.
  2. El sistema obtiene el historial y las preferencias disponibles.
  3. Analiza la información pertinente.
  4. Genera alternativas de alojamiento, transporte y rutas.
  5. Presenta las recomendaciones al usuario.
- Alternativas: si no hay información suficiente o no se generan resultados, el sistema informa la situación.
- Postcondición: el usuario puede consultar las recomendaciones generadas.

CU-14 — Ajustar recomendaciones
- Actor principal: Usuario.
- RF asociado: RF-22.
- Precondición: el usuario dispone de recomendaciones o puede iniciar una consulta de recomendaciones.
- Flujo principal:
  1. El sistema presenta recomendaciones.
  2. El usuario acepta una sugerencia o modifica los parámetros disponibles.
  3. El sistema actualiza los criterios de la consulta.
  4. Genera y presenta los resultados ajustados.
  5. El sistema registra las interacciones pertinentes para refinar progresivamente el modelo de recomendación.
- Alternativas: si los parámetros son inválidos, solicita corregirlos. Si el usuario no desea continuar, conserva el estado anterior.
- Postcondición: se muestran las recomendaciones ajustadas y se registra la interacción conforme a las reglas del sistema.

CU-15 — Compartir itinerario por correo
- Actor principal: Usuario.
- Actor secundario: Servicio de correo.
- RF asociado: RF-23.
- Precondición: existe un itinerario que el usuario puede compartir.
- Flujo principal:
  1. El usuario selecciona un itinerario.
  2. Introduce los destinatarios.
  3. El sistema genera un enlace seguro con los permisos previstos.
  4. El usuario confirma el envío.
  5. El sistema envía el enlace por correo.
  6. El sistema informa el resultado.
- Alternativas: si los destinatarios son inválidos o el envío falla, el sistema informa el error. Si se cancela antes de confirmar, no envía el correo.
- Postcondición: el enlace se envía si la operación tiene éxito.
- Pendiente de definición: expiración, revocación y permisos del enlace compartido.

CU-16 — Publicar itinerario en red social
- Actor principal: Usuario.
- Actor secundario: Red social seleccionada.
- RF asociado: RF-24.
- Precondición: existe un itinerario que puede publicarse y la integración dispone de los permisos necesarios.
- Flujo principal:
  1. El usuario selecciona un itinerario.
  2. Selecciona una red social compatible.
  3. El sistema prepara la publicación.
  4. El usuario confirma.
  5. El sistema envía la publicación a la red social.
  6. El sistema informa el resultado.
- Alternativas: si no hay autorización o la plataforma rechaza la publicación, informa que la operación no se completó.
- Postcondición: la publicación queda realizada únicamente si la red social confirma su aceptación.

CU-17 — Gestionar acceso a la cuenta de correo
- Actor principal: Usuario.
- Actor secundario: Servicio de correo.
- RF asociados: RF-17, RF-18.
- Precondición: el usuario tiene acceso al sistema.
- Flujo principal (conectar):
  1. El usuario solicita conectar una cuenta de correo.
  2. El sistema presenta los proveedores de correo compatibles.
  3. El usuario elige uno.
  4. El sistema lo dirige al mecanismo de autorización del proveedor, indicando qué acceso se solicita.
  5. El usuario autoriza el acceso.
  6. El sistema registra la autorización y habilita el procesamiento de los correos de esa cuenta (CU-07).
  7. El sistema confirma el resultado.
- Flujo alternativo (revocar):
  1. El usuario consulta las cuentas de correo conectadas.
  2. Selecciona una y solicita revocar el acceso.
  3. El sistema deja de acceder a esa cuenta y descarta las credenciales almacenadas.
  4. El sistema confirma el resultado.
- Alternativas: si el usuario rechaza la autorización, la cuenta no se conecta. Si el proveedor no está disponible, el sistema informa que no pudo completar la operación. Si la cuenta ya está conectada, el sistema lo informa.
- Postcondición: el sistema accede al correo solo mientras exista una autorización vigente del usuario. Tras revocarla, no vuelve a acceder.
- Pendiente de definición: mecanismo concreto de autorización, permisos mínimos solicitados y qué ocurre con las reservas ya importadas al revocar.

CU-18 — Notificar cambios en reservas
- Actor principal: proceso automático del sistema.
- Beneficiario: Usuario.
- RF asociado: RF-19.
- Precondición: un cambio proveniente de una fuente externa (correo o proveedor turístico) se reflejó en una reserva del usuario (CU-07, CU-10).
- Flujo principal:
  1. El sistema determina si el cambio es relevante para el usuario.
  2. El sistema genera la notificación.
  3. El sistema la entrega por el canal disponible.
  4. El sistema registra el resultado de la entrega.
- Alternativas: si el cambio no es relevante, no se notifica. Si la entrega falla, el sistema registra el fallo y lo reintenta; el cambio sigue visible en el itinerario.
- Postcondición: el usuario fue informado del cambio relevante, o el fallo quedó registrado.
- Pendiente de definición: canales de notificación y criterios de relevancia.
