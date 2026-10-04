# Prueba mínima de fidelidad · Restaurante gastronómico (04-10-2026)

**Autorizada por Eduardo (04-10).** Objetivo: ver si la IA respeta la estructura de la casa y si la "obra" se ve de calidad.

## Qué se hizo y cuánto costó
| Paso | Modelo y ajustes | Créditos |
|---|---|---|
| 2 renders de la fachada convertida en restaurante (A y B) | Nano Banana Pro, 4K, 9:16, con 2 fotos de referencia (IMG_3339 recortada a 9:16 y IMG_1881 para entender el porche sin carro) | 8 |
| Transición, intento 1 | Kling v3.0 pro, 5 s, sin sonido, imagen inicial = foto real, final = render A | 8,75 |
| Transición, intento 2 (mejorado) | Igual, con prompt afinado (malla verde de seguridad, terraza visible) | 8,75 |
| **Total** | | **25,5** (saldo: 801 → 775,5) |

## Resultado
- **Estructura:** se conservan los **3 niveles**, la **terraza con techo verde y baranda**, la posición de las **ventanas del segundo nivel**, las **tejas**, la línea del techo del porche y el **vecino de la derecha**. **Se quitó el carro.** Cambian solo la planta baja (restaurante), pintura y luz.
- **Render A (elegido):** se ve claramente un restaurante (mesas, sillas, luz cálida), hora azul, terraza con luces. **Render B (reserva):** conserva las rejas de las ventanas del 2.º nivel; más sobrio.
- **Transición (intento 2, la elegida):** se va el carro, sube la obra con **malla verde de seguridad sobre andamio** (muy de Venezuela), cae la malla y aparece el restaurante al atardecer, igual al render. Sin franjas ni derretidos. Intento 1 tenía una franja borrosa a 1,4 s.
- **Detalles a pulir:** (1) al principio de la obra el andamio también tapa la terraza unos 2 s (es pasajero); (2) la IA quitó los cables aéreos; (3) el render agrega una banqueta delante.

## Lo que aprendimos (para las demás cadenas)
1. **Recortar la foto a 9:16** antes de subirla (la IMG_3339 es 3:4) da un clip vertical completo, sin deformar.
2. Con **dos fotos de referencia** (la composición y una vista despejada del porche) la IA entiende mejor la estructura.
3. En el video, **describir la obra paso a paso** y pedir **"sin tablas, sin derretidos, sin parpadeos"** mejora mucho.
4. La transición sale a 1080×1920 y 24 fps, 5 s.

## Archivos
`render-restaurante-A.jpg` · `render-restaurante-B-reserva.jpg` · `antes-despues-restaurante.jpg` · `tablero-transicion.jpg` · `transicion-restaurante.mp4`
*(Todo lo generado lleva el rótulo "Recreación con IA · No es un proyecto aprobado" al publicar.)*
