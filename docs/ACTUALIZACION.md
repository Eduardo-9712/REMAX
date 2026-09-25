# Actualización semanal (domingos, 9:00 p.m. hora de Venezuela)

Instrucciones para Claude. La base de datos viva está en la aplicación:
`https://claude.ai/artifact/PA1onp1SF72ZFpKKgjhyYY` (colecciones `inmuebles`, `clientes`, `meta`, `reportes`).
Se lee y se escribe con la herramienta `ArtifactData`.

## 1. Leer el estado actual
- `ArtifactData list` de `inmuebles` (limit 1000) con `out_dir` al scratchpad.
- Anotar, por inmueble: fuentes (código y URL), precio, estatus y `version` (para `if_version`).

## 2. Buscar publicaciones (SOLO RE/MAX Venezuela y MercadoLibre)
Por cada zona y tipo (venta y alquiler):
- Guatire, Guarenas, Costa Mirandina (Higuerote, Río Chico, Carenero, Tacarigua, Buche, Chirimena, Paparo).
- Residencial (apartamento, casa, townhouse), terreno, galpón, local.
- **Únicas fuentes permitidas:**
  - RE/MAX Venezuela: `www.remax.com.ve/inmuebles/...` (se busca con `allowed_domains: ["remax.com.ve"]`).
  - MercadoLibre: `apartamento.` / `casa.` / `inmueble.mercadolibre.com.ve/MLV-...` (se busca con `allowed_domains: ["mercadolibre.com.ve"]`).
- No se agrega nada de otros portales. Solo se aceptan otros enlaces cuando los envía Eduardo.
- El enlace guardado tiene que ser **la publicación individual**, nunca una página de búsqueda o de listado.
- Primero se prueba `WebFetch` en la publicación; si está bloqueada, se usa `WebSearch`.

## 3. Reglas
- **Exactitud antes que cantidad:** habitaciones, baños, puestos, m² y precio se anotan **solo si la
  publicación los dice explícitamente**. Si hay dudas, el campo queda vacío y se explica en la `nota`.
  Nunca se suma, redondea ni supone (por ejemplo, "4 habitaciones + estudio" son 4 habitaciones).
  Un precio que aparece en un resumen de varias publicaciones no se asigna a una publicación concreta.
- `verificado = true` solo cuando se leyó la página de la publicación (`WebFetch`) y los datos coinciden.
  Si los datos salieron del buscador, `verificado = false`.
- **Nuevos:** venta ≥ USD 20.000 (o sin precio visible) y alquileres sin mínimo, que no estén ya en la base
  (mismo código RE/MAX o MLV, o misma URL). ID con el prefijo de la zona (GTR/GRN/CST) y el siguiente número libre.
  `fecha_detectada` = hoy, estatus `por_verificar` y al historial "Nuevo en actualización semanal". Hay que calificar
  los 5 criterios (1-5) y escribir la `nota`: por qué la inversión es buena, media o baja, o qué dato falta.
- **Cambios de precio:** actualizar `precio` y agregar al historial "Cambio de precio (antes $X)".
- **Ya no aparece** (la publicación da 404 o dice finalizada o pausada): estatus `retirado` y al historial
  "Publicación no encontrada: posible venta". **Nunca marcar `vendido`**: eso lo confirma Eduardo.
- **Nunca tocar las captaciones de Eduardo** (`propia: true`, códigos `CAP-…`): ni datos, ni estatus, ni propietario.
  Sí cuentan como comparables.
- **No tocar** los inmuebles en `negociacion` o `vendido`, ni los que tengan `verificado = true`
  (salvo precio y estatus), ni la `nota` o `cal` que Eduardo haya editado.
- Escribir en lotes (`batch`, máximo 50) con `if_version`.
- Actualizar `ultima_verificacion` = hoy en los que se volvieron a encontrar.

## 4. Reporte
- `meta/estado`: `ultima_actualizacion` ("DD-MM-AAAA · Actualización semanal"), `resumen`
  (nuevos, bajas de precio, retirados y las 3 mejores oportunidades nuevas con su código) y `proxima`.
- `reportes/<AAAA-MM-DD>`: el mismo resumen con las listas de IDs.
- Exportar la base a `data/inmuebles.json` (lista con `id`) **sin `captacion.propietario`** (los datos de los propietarios no van al repositorio), hacer commit y push a la rama de trabajo.
- Terminar con un mensaje corto en español para Eduardo con el resumen y el enlace a la aplicación.
