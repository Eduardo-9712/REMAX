# Cierres reales de RE/MAX Delta (2025)

Fuente: el Excel interno de la oficina, *Productividad y Captaciones Año 2025*
(`datos/originales/delta-productividad-captaciones-2025.xlsx`). Los datos extraídos están en
`datos/delta_cierres_2025.json` y se recalculan con `python3 analisis/scripts/delta_cierres.py`.

Es **información interna** (agentes, comisiones, alianzas). Para contenido público solo se usan
cifras agregadas, nunca el detalle de una operación ni de un agente.

## Qué trae el Excel

| Hoja | Contenido |
|---|---|
| Captaciones 2024 / 2025 y una hoja por mes | Cada inmueble captado: agente, código de oficina y NOVUS, tipo, urbanización, exclusiva, venta o alquiler, fecha y precio inicial |
| Reservas | Precio inicial, **precio final**, fecha de reserva y monto reservado |
| Ventas - Alquileres | Cada cierre con su **precio final** y fecha |
| Puntas | Comisión de cada cierre y cómo se repartió entre las dos puntas |
| Captaciones por agentes y TOP | Ranking mensual de captadores y cerradores |

## Lo que dicen los números

- **56 cierres en 2025:** 45 ventas y 9 alquileres. Hay 2 registros con precio dudoso (ver abajo).
- **Precio de venta típico:** mediana de **USD 21.500**, con un rango de USD 6.000 a 52.500.
  - Apartamentos: 28 ventas, mediana USD 20.000.
  - Casas: 9 ventas, mediana USD 23.000.
  - Town houses: 6 ventas, mediana USD 27.000.
- **La rebaja real (el sobreprecio):** se comparan 44 ventas con precio inicial y precio final.
  - Mediana: **3,5 % menos** que el precio publicado. Promedio: **4,9 %** menos.
  - 18 de las 44 se vendieron **sin rebaja**.
  - Las que más bajaron, entre 13 % y 23 %, salieron con precio alto. Es el argumento para
    captar a precio de mercado desde el día uno.
- **Tiempo hasta la reserva:** mediana de **70 días** desde que se publica. La vigencia de la
  autorización es de 90 días, así que la mitad se reserva dentro del primer contrato.
- **Alianzas:** 16 de los 56 cierres se hicieron compartiendo con otro agente u oficina,
  incluso Century 21.
- **Captaciones 2025:** unas 173, frente a 98 en 2024. El 62 % fue en exclusiva y el 86 % para venta.
  Predominan apartamentos, casas y locales comerciales, pero solo hay 5 terrenos y 4 galpones.
- **Comisión mínima:** en la práctica casi nunca se cobra menos de **USD 1.000** en ventas, aunque el 5 %
  dé menos. La única excepción fue una casa de USD 6.000 en Caja de Agua, con USD 500. Eso **no aparece en los contratos**, así que conviene confirmarlo con Luis León y ponerlo por escrito.

## Datos para revisar con Alejandra

- **Fechas de reserva anteriores a la captación:** La Laguna (Nueva Casarapa), Los Altos II
  (Castillejo), Parque Alto y Canaima IV. Seguramente es un error de año o de mes.
- **La Sabana (obra gris):** en *Ventas* dice USD 1.000, pero en *Reservas* y *Puntas* dice 16.500.
- **Frigorífico Super Carne (Guarenas):** se reservó en 37.000, pero el precio final y la comisión
  aparecen como 5.450. Hay que confirmar el precio real.
- **Galpón de 1.710 m² en Las Flores:** alquilado por USD 9.563. Hay que confirmar si es el canon mensual.

## Para qué lo vamos a usar

1. **Cargar los cierres en la base maestra**, en la parte de *cierres reales*, para tener precios
   finales y no solo precios de publicación. *Pendiente: con el visto bueno de Eduardo.*
2. **Reel del sobreprecio** (`contenido/reels.md`): *"En nuestra oficina, la mitad de las ventas
   se cerró a menos de 4 % del precio publicado… cuando el precio es el correcto."*
3. **Captación:** mostrarle al propietario cuánto se tarda en vender y cuánto se negocia en su zona.
