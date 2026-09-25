# Actualización semanal (domingos, 9:00 p.m. hora de Venezuela)

Instrucciones para Claude. La base de datos viva está en la aplicación:
`https://claude.ai/artifact/PA1onp1SF72ZFpKKgjhyYY` (colecciones `inmuebles`, `clientes`, `meta`, `reportes`).
Se lee y se escribe con la herramienta `ArtifactData`.

## 1. Leer el estado actual
- `ArtifactData list` de `inmuebles` (limit 1000) con `out_dir` al scratchpad.
- Anotar, por inmueble: fuentes (código y URL), precio, estatus y `version` (para `if_version`).

## 2. Buscar publicaciones
Por cada zona y tipo (venta y alquiler):
- Guatire, Guarenas, Costa Mirandina (Higuerote, Río Chico, Carenero, Tacarigua, Buche, Chirimena, Paparo).
- Residencial (apartamento, casa, townhouse), terreno, galpón, local.
- Fuentes: Rent-A-House (`site:rentahouse.com.ve`, títulos "RAH … Precio Referencial"), RE/MAX
  (`remax.com.ve`), MercadoLibre, Tu Inmueble, Conlallave, Century 21, Inmobiliaria.com, BienesOnline, ZonaVen.
- Primero se prueba `WebFetch` directo; si el portal está bloqueado, se usa `WebSearch`.

## 3. Reglas
- **Nuevos:** venta ≥ USD 20.000 (alquiler sin mínimo) que no estén ya en la base (mismo código o URL,
  o mismo sector + precio + m²). ID con el prefijo de la zona (GTR/GRN/CST) y el siguiente número libre.
  `fecha_detectada` = hoy. Historial: "Nuevo en actualización semanal". Hay que calificar los 5 criterios (1-5)
  y escribir la `nota` explicando por qué la inversión es buena, media o baja.
  Estatus `disponible` si la publicación es reciente; si no, `por_verificar`.
- **Cambios de precio:** actualizar `precio` y agregar al historial "Cambio de precio (antes $X)".
- **Ya no aparece** (la URL da 404 o el anuncio dice vendido o pausado): estatus `retirado` y al historial
  "Publicación no encontrada: posible venta". **Nunca marcar `vendido`**: eso lo confirma Eduardo.
- **No tocar** los inmuebles en `negociacion` o `vendido`, ni la `nota` o `cal` que Eduardo haya editado.
- Escribir en lotes (`batch`, máximo 50) con `if_version`.
- Actualizar `ultima_verificacion` = hoy en los que se volvieron a encontrar.

## 4. Reporte
- `meta/estado`: `ultima_actualizacion` ("DD-MM-AAAA · Actualización semanal"), `resumen`
  (nuevos, bajas de precio, retirados y las 3 mejores oportunidades nuevas con su código) y `proxima`.
- `reportes/<AAAA-MM-DD>`: el mismo resumen con las listas de IDs.
- Exportar la base a `data/inmuebles.json` (lista con `id`), hacer commit y push a la rama de trabajo.
- Terminar con un mensaje corto en español para Eduardo con el resumen y el enlace a la aplicación.
