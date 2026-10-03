# Higgsfield: cómo conseguir "lo mejor posible" sin cambiar la casa

**Estado:** plan para aprobar. **No se ha generado nada ni se han gastado créditos.** Saldo al 03-10-2026: **801 créditos** (plan Plus). El costo de cada generación lo consulto **antes** de ejecutarla y espero tu "dale".

## La regla de Eduardo
La IA puede **mejorar el grado** (luz, color, calidad, movimiento), pero **no cambia la esencia ni la estructura de la casa**: mismos niveles, mismo frente angosto, misma terraza con techo verde, mismas ventanas y rejas, mismo porche, mismos vecinos. En las transformaciones (idea 2) cambian **acabados, fachada comercial, mobiliario y función**, nunca el volumen del edificio.

## Qué modelo usar para qué (según el catálogo de Higgsfield; sin probar todavía)

| Trabajo | Modelo recomendado | Por qué | Plan B |
|---|---|---|---|
| **Renders del "después"** (fachada e interiores) a partir de las fotos reales | **Nano Banana Pro** (calidad máxima, hasta 4K, fotorrealista, usa imágenes de referencia) | Es el de "ultimate quality" y soporta referencias | **FLUX 3 Image** (edición con hasta 10 referencias, 4K) · **GPT Image 2.5** calidad alta |
| **Tomas "héroe" de cine** (atardecer, órbita exterior, "dron" entrando, caída final) | **Veo 3.1** en calidad **ultra** (ultrarrealista, cinematográfico, imagen inicial, 9:16, 4–8 s por clip) | Es el más realista del catálogo | **Kling v3.0** modo **4K** (imagen inicial y final, multi-plano) |
| **Transformaciones** (foto real → render, con la obra en medio) | **Seedance 2.5** (imagen inicial **y final**, referencias, 1080p, hasta 30 s) o **Kling v3.0** (imagen inicial y final) | Puedes fijar **cómo empieza (real) y cómo termina (render)**, y la IA "rellena" la obra | Veo 3.1 con dos clips |
| **Mejorar la nitidez** de los clips reales | `upscale_video` | No inventa, solo sube resolución | — |

**Ahorro de créditos:** Seedance 2.5 permite hacer **borrador a 480p** y luego **finalizar a 1080p** el que gusta. Se prueba el movimiento barato y solo se paga la versión final de las tomas aprobadas.

## Reglas de prompt (para todas las ideas)

**Bloque de fidelidad (siempre al inicio):**
`Use the reference image as the exact source. Keep the building's structure identical: same number of floors, same narrow frontage, same green terrace roof, same window and door positions, same bars pattern, same porch roof, same neighboring buildings and street. Do not add or remove floors, windows or structural elements. No people, no readable text, no logos, no brand names, no license plates.`

**Bloque de calidad y luz (siempre al final):**
`Ultra-realistic, photographic, true-to-life colors, natural warm golden-hour light with soft long shadows, gentle film grain, subtle lens realism, cinematic but natural and human, 4K detail, no artificial glow, no plastic or CGI look.`

**Negativos útiles:** `no distortion of walls, no melting geometry, no extra windows, no changed roof, no fantasy elements, no oversaturation, no text.`

## Control de calidad (antes de aprobar cualquier toma)

Se compara **lado a lado con la foto real**. Se rechaza si cambia **algo** de esta lista:
1. Niveles del edificio (3) y terraza con techo verde.
2. Frente angosto, porche con techo de tejas, rejas.
3. Posición y número de ventanas.
4. Edificios vecinos y forma de la calle.
5. Aparecen letras, logos, placas o personas reconocibles.
6. Las paredes "se derriten" o la geometría se curva.
Se regenera con el mismo prompt reforzando lo que falló, o se baja el movimiento de cámara.

## Cómo trabajamos la "versión de dron" ahora y la real después
1. **Ahora:** IA lo mejor posible, con las fotos reales de referencia, rotulada **"Imagen ilustrativa con IA"** en tomas aéreas y de caída.
2. **Cuando Eduardo compre el dron:** se **regraban** las mismas tomas con las mismas indicaciones de cámara (órbita, avance al porche, subida sobre la terraza, caída final). Los guiones y la voz en off **no cambian**, solo se reemplazan los clips de IA por los reales y se quita el rótulo en esas tomas.
3. **Etalonaje (color) real:** la luz cálida de atardecer de los clips reales se logra también **en edición** (grado de color), no solo con IA, para que lo real y lo generado se vean de la misma película.

## Orden de producción propuesto (cuando des el visto bueno)
1. **Idea 2** (la más compleja): renders → transiciones → caída → paneo.
2. **Idea 1:** paneo atardecer + tomas héroe (reutiliza el paneo de la idea 2).
3. **Idea 3:** casi todo real; solo micro-movimientos y el teaser.
4. **Idea 4:** renders de la idea 2 y, si se hace la versión B, el motorizado de ficción.
Cada paso: 1 prueba corta → te la muestro → apruebas → se genera el resto.
