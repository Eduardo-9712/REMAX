# Estudio de Mercado · Este de Miranda

Estudio de mercado y análisis comparativo privado de **Eduardo León (RE/MAX)** para
**Guatire**, **Guarenas** y la **Costa Mirandina**, dividido en residencial, terrenos,
galpones y locales, en venta y en alquiler.

**Fuentes: solo RE/MAX Venezuela y MercadoLibre** (más los enlaces que envíe Eduardo). Cada inmueble
guarda el enlace directo a su publicación.

- **Aplicación (privada):** https://claude.ai/artifact/PA1onp1SF72ZFpKKgjhyYY
- **Código de la aplicación:** `app/index.html`
- **Copia de los datos:** `data/inmuebles.json` (la base de datos viva está en la aplicación)
- **Levantamiento piloto:** `scripts/semilla.py`
- **Procedimiento de la actualización semanal:** `docs/ACTUALIZACION.md`

## Qué tiene la aplicación

| Pestaña | Para qué sirve |
|---|---|
| Panel general | Inventario activo, nuevos de la semana, salidas del mercado, mapa zona × tipo con la mediana de $/m² y el top 10 de oportunidades |
| Guatire / Guarenas / Costa Mirandina | Sub-pestañas Residencial · Terrenos · Galpones · Locales, con filtros, orden y KPIs |
| Clientes e inversionistas | Perfil de cada cliente → inmuebles que le sirven, ordenados según su perfil, y ficha lista para enviar por WhatsApp |

En la ficha de cada inmueble se cambia el estatus con un botón (Disponible · En negociación ·
Vendido/Alquilado · Retirado · Por verificar), se edita cualquier dato y se guarda el historial de
precios y estatus. **Exportar a Excel** genera un libro con una hoja por zona más un resumen.

## Calificación de inversión (0-100)

| Criterio | Peso general |
|---|---|
| Precio por m² vs. la mediana de sus comparables | 35% |
| Ubicación y demanda | 20% |
| Estado y servicios (agua, luz, planta) | 15% |
| Rentabilidad por alquiler | 10% |
| Liquidez | 10% |
| Documentación y riesgo | 10% |

- **Precio:** 40% por debajo de la mediana da 100 puntos, igual a la mediana da 50 y 40% por encima da 0.
  Los comparables son del mismo tipo y zona (en residencial, casas con casas y apartamentos con
  apartamentos). Si hay 3 o más en el mismo sector, se compara solo con el sector.
- Los demás criterios los califica el asesor de 1 a 5.
- **Excelente**: 75 o más · **Media**: de 50 a 74 · **Baja**: menos de 50.
- Los perfiles de cliente (renta, plusvalía, reventa, uso propio, desarrollo) cambian los pesos.

## Reglas del estudio

- Habitaciones, baños, m² y precio se anotan solo si la publicación los dice. La marca **Confirmado**
  indica que los datos se revisaron contra la página del anuncio.
- Solo se incluyen ventas desde **USD 20.000**, sin tope. Los alquileres se incluyen como referencia de renta.
- Un anuncio que desaparece pasa a **Retirado**, nunca a **Vendido**: eso lo confirma Eduardo.
- La actualización corre cada **domingo a las 9:00 p.m.** (hora de Venezuela).
