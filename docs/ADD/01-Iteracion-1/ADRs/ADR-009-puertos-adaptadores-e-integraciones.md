# ADR-009: Aislar proveedores mediante puertos y adaptadores

- **Estado:** Aceptado como diseño
- **Fecha:** 2026-10-28
- **Iteración:** ADD-1

## Contexto

Correo, proveedores turísticos, agencia preferida, mapas y redes sociales exponen contratos, autenticación, límites y disponibilidad diferentes. El dominio no debe depender de esos detalles.

## Drivers

RF-07–RF-15, RF-24; QA-I1/I2/I3, QA-SE1, QA-E1; CON-10/12/15; CRN-05/06/11.

## Alternativas

- Invocar SDKs y modelos externos directamente desde el dominio.
- Definir puertos internos y adaptadores por proveedor.
- Depender de un único proveedor aunque no cubra todas las capacidades.

## Decisión

Adoptar Ports and Adapters (hexagonal). Dominio y servicios de aplicación dependen de interfaces internas; los adaptadores traducen protocolos, autenticación, formatos y errores. Cada integración tendrá pruebas de contrato.

RF-15 se diseña como integración técnica directa con la agencia preferida, condicionada a verificar una API oficial compatible en la etapa 5. Si no existe, se documentará la limitación y se consultará el impacto en el alcance; no se fingirá una integración.

## Consecuencias

Reduce el acoplamiento y permite reemplazar proveedores, pero agrega interfaces, mapeos y pruebas. No elimina cuotas, costos, permisos ni cambios de APIs.

## Trazabilidad

ADD-1/2; vistas de módulos y C&C; etapa 5.
