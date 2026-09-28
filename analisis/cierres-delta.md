# Cierres reales de RE/MAX Delta (2025 y 2026)

Fuente: el Excel interno de la oficina, *Productividad y Captaciones*, uno por año
(`datos/originales/delta-productividad-captaciones-<año>.xlsx`). El de 2026 llega hasta septiembre.
Los datos extraídos están en `datos/delta_cierres_<año>.json` y se recalculan con
`python3 analisis/scripts/delta_cierres.py`. Cuando llegue un Excel nuevo, se reemplaza el de su año y se
vuelve a correr.

Es **información interna** (agentes, comisiones, alianzas). Para contenido público solo se usan
cifras agregadas, nunca el detalle de una operación ni de un agente.

## Qué trae el Excel

| Hoja | Contenido |
|---|---|
| Captaciones del año y una hoja por mes | Cada inmueble captado: agente, códigos de oficina y NOVUS, tipo, urbanización, exclusiva, venta o alquiler, fecha y precio inicial |
| Reservas | Precio inicial, **precio final**, fecha de reserva y monto reservado |
| Ventas - Alquileres | Cada cierre con su **precio final** y fecha. En 2026 ya no dice si es venta o alquiler: se toma como alquiler lo que está por debajo de USD 3.000 |
| Puntas | Comisión de cada cierre y cómo se repartió entre las dos puntas |
| Captaciones por agentes y TOP | Ranking mensual de captadores y cerradores |

## Los dos años lado a lado

| | 2025 (año completo) | 2026 (enero–agosto) |
|---|---|---|
| Cierres | 55 (45 ventas, 9 alquileres y 1 dudoso) | **44** (33 ventas y 11 alquileres) |
| Cierres de enero a agosto | 34 | **44** |
| Monto vendido | USD 0,98 millones | **USD 1,30 millones** (1,02 sin el galpón de USD 280.000) |
| Venta típica (mediana) | USD 21.500 | **USD 29.000** |
| Apartamento típico | USD 20.000 (29 ventas) | USD 26.000 (19 ventas) |
| Rebaja sobre el precio publicado (mediana) | 3,5 % | **0 %** |
| Rebaja promedio | 4,9 % | 2,8 % |
| Vendidas sin rebaja | 18 de 44 | **15 de 26** (2 incluso por encima) |
| Días hasta la reserva (mediana) | 70 | **48** |
| Captaciones | 173 (62 % en exclusiva) | 102 hasta septiembre (**45 %** en exclusiva) |

## Lo que dicen los números

- **2026 va mejor que 2025:** en ocho meses ya se vendió más dinero que en todo 2025, y con más cierres
  en el mismo período.
- **Se vende más caro y más rápido.** La venta típica pasó de USD 21.500 a 29.000, y la reserva llega en
  unos 48 días en vez de 70. Ojo: puede ser porque la mezcla de inmuebles es distinta (más TH y casas). No
  hay que decir que "los precios subieron 35 %" sin comparar la misma zona y el mismo tipo.
- **Se negocia menos.** En 2026, más de la mitad de las ventas se cerró al precio publicado. Las rebajas
  grandes siguen siendo las que salieron con precio alto: una casa en La Esperanza (Castillejo) bajó
  de 120.000 a 100.000.
- **Las captaciones se frenaron:** 3 en julio, 6 en agosto y 8 en septiembre, frente a 19, 13 y 22 en esos
  meses de 2025. Y la exclusiva bajó del 62 % al 45 %. Es una oportunidad para Eduardo cuando llegue a Delta.
- **El nicho de Luis León aparece:** en marzo de 2026 se vendió un **galpón de USD 280.000** en el Centro
  Industrial Cloris. En 2026 se vendieron 2 terrenos, en Calle Zamora y en El Ingenio. Aun así, en las
  captaciones siguen siendo pocos: 3 terrenos y 3 galpones.
- **Costas Mirandinas:** hubo 3 ventas en 2026 (Jardín de Higuerote, Villas de Fuente Mar y Los Jobos en
  Río Chico), entre USD 17.000 y 46.000.
- **Alianzas:** 16 cierres en 2025 y 5 en 2026, incluidas alianzas con Century 21.
- **Comisión mínima:** en ventas casi nunca se cobra menos de **USD 1.000**, aunque el 5 % dé menos. Eso
  **no aparece en los contratos**, así que conviene confirmarlo con Luis León y ponerlo por escrito.
- **Comisión de alquiler:** el contrato dice un mes de canon que paga el propietario, pero en muchos
  alquileres la comisión registrada es de **dos cánones**, seguramente uno por cada parte. *Por confirmar.*

## Datos para revisar con Alejandra

**2025**

- **Reservas con fecha anterior a la captación:** La Laguna (Nueva Casarapa), Los Altos II
  (Castillejo), Parque Alto y Canaima IV. Seguramente es un error de año o de mes.
- **La Sabana (obra gris):** en *Ventas* dice USD 1.000, pero en *Reservas* y *Puntas* dice 16.500.
- **Frigorífico Super Carne (Guarenas):** se reservó en 37.000, pero el precio final y la comisión
  aparecen como 5.450. Hay que confirmar el precio real.
- **Galpón de 1.710 m² en Las Flores:** alquilado por USD 9.563. Hay que confirmar si es el canon mensual.

**2026**

- **Tres cierres de marzo con fecha de 2025:** C.C. Vista Place, Los Cardenales (El Marqués) y el galpón
  del Centro Industrial Cloris. *Eduardo: si está en el Excel de 2026, es de 2026 (corregido en la base).*
- **Precios distintos entre la reserva y la venta:**
  - Canaima II: reservado en 28.000, vendido en 27.000.
  - Terreno de Calle Zamora: reservado en 46.000, vendido en 50.000.
  - Los dos apartamentos de Ciudad Casarapa (parcela 6): los precios están cruzados entre las dos hojas.
  - Local del C.C. Compro: 1.600 en *Ventas*, 800 en *Puntas*.
- **Parque Habitat B:** aparece como casa en *Reservas* y como TH en *Ventas*.
- **Galpón de El Desvío:** el agente figura como "Enrique Castillejo". *Eduardo: es Enrique Oliveri (corregido).*
- **Jardines de Pacairigua:** la reserva quedó con fecha un día antes de la captación.
- **Reservas sin cierre en el Excel:** según Eduardo, la casa de La Esperanza (Castillejo, USD 100.000) y la de
  El Torreón (USD 65.000, en alianza con Luis León) ya se cerraron. Falta la fecha exacta. El apartamento de
  La Sabana (USD 42.000) sigue por confirmar.

## Para qué lo vamos a usar

1. **Cargados en la base maestra (29-09-2026):** 101 cierres en la colección `cierres` (pestaña Cierres), con
   `python3 analisis/scripts/cierres_a_base.py`, que genera los lotes en `datos/cierres_base/`. Se aplicaron
   las correcciones de Eduardo:
   - Si un cierre está en el Excel de 2026, es de 2026.
   - Enrique Castillejo es Enrique Oliveri.
   - La Esperanza (USD 100.000) y El Torreón (USD 65.000) están cerradas.
   - La Sabana (USD 42.000) sigue por confirmar.
   Contando solo ventas cerradas y cruzadas con su reserva, la base da: rebaja mediana de 4,6 % en 2025 y de
   0 % en 2026, y 75 y 57 días desde la captación hasta el cierre. Los números de arriba salen de la hoja
   *Reservas*, que incluye reservas que no llegaron a cierre.
2. **Reel del sobreprecio** (`contenido/reels.md`): *"Este año, más de la mitad de las ventas de nuestra
   oficina se cerró al precio publicado… cuando el precio es el correcto."*
3. **Captación:** mostrarle al propietario cuánto se tarda en vender y cuánto se negocia en su zona.
