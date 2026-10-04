# Higgsfield: cómo conseguir "lo mejor posible" sin cambiar la casa

**Estado:** plan para aprobar. **No se ha generado nada ni se han gastado créditos.** Saldo al 03-10-2026: **801 créditos** (plan Plus). El costo de cada generación lo consulto **antes** de ejecutarla y espero tu "dale".

## La regla de Eduardo
La IA puede **mejorar el grado** (luz, color, calidad, movimiento), pero **no cambia la esencia ni la estructura de la casa**: mismos niveles, mismo frente angosto, misma terraza con techo verde, mismas ventanas y rejas, mismo porche, mismos vecinos. En las transformaciones (idea 2) cambian **acabados, fachada comercial, mobiliario y función**, nunca el volumen del edificio.

## Qué modelo usar para qué, y cuánto cuesta (costos reales consultados el 03-10-2026, **sin gastar nada**)

El costo se consultó con la opción de "cotizar sin enviar" de Higgsfield. **Saldo: 801 créditos (plan Plus).**

| Trabajo | Modelo recomendado | Costo por pieza | Plan B |
|---|---|---|---|
| **Renders del "después"** (fachada e interiores) | **Nano Banana Pro**, 4K (calidad máxima, usa fotos de referencia) | **4 créditos** (2K: 2) | FLUX 3 Image 2K: 3 · GPT Image 2.5 |
| **Transiciones** (foto real → render, con la obra en medio; y rubro → rubro) | **Kling v3.0 modo pro**, imagen inicial y final, 5 s, sin sonido | **8,75 créditos** (modo estándar: 7,5) | Seedance 2.5: 720p 4 s = 28 · 1080p 5 s = 60 · **borrador 480p 4–5 s = 12–15** |
| **Tomas "héroe" de cine** (caída, paneo, elevación final, apertura con dron) | **Veo 3.1 ultra**, 8 s | **120 créditos** | **Veo 3.1 rápido, 8 s = 32** · Kling v3.0 4K, 5 s = 30 |
| **Mejorar la nitidez** de los clips reales | `upscale_video` | se cotiza antes | — |

**Cómo gastar bien:** las transiciones y los interiores se hacen con **Kling pro** (baratísimo). Las tomas héroe se **prueban primero con Veo 3.1 rápido (32)** y solo se **repiten en ultra (120)** las 2 o 3 que de verdad lo merecen. Seedance queda como plan B y para los **borradores a 480p**.

### Primera prueba recomendada (cuando Eduardo diga «dale»): la **prueba mínima de fidelidad**
Antes de gastar en serio, se hace **una sola cosa** que responde a la duda más importante: **¿la IA respeta la estructura de la casa y la obra se ve bien?**
1. **1 render** de la fachada real (IMG_1881) convertida en el **restaurante gastronómico** (Nano Banana Pro 4K): **4 créditos**.
2. **1 transición** de la fachada real al render, con la obra en timelapse (Kling v3.0 pro, 5 s): **8,75 créditos**.
**Total: ≈ 13 créditos.** Te muestro el resultado y comparamos con la foto real. Si respeta los 3 niveles, la terraza de techo verde, el porche con sus dos puertas y los vecinos, seguimos con la apertura (Etapa 0) y la cadena. Si no, ajustamos el prompt antes de gastar más.

### Plan de créditos (aproximado, con ≈30 % de margen para repetir tomas)

| Etapa | Qué se genera | Créditos |
|---|---|---|
| **0 · Prueba mínima de fidelidad** | 1 render + 1 transición (restaurante) | **≈ 13** |
| **0b · Apertura Google Earth + paneo 360** (la misma para las ideas 1 y 2) | caída y paneo con Veo 3.1 rápido (probar) | **≈ 64** |
| **A · Cadena completa del restaurante** (idea 2) | 6 renders (4K) + 6 transiciones (Kling pro) | **≈ 77** (+ margen ≈ 100) |
| **B · Concesionario, coworking y spa** | 18 renders + 18 transiciones | **≈ 230** (+ margen ≈ 300) |
| **C · Apertura y paneo** (idea 2 y 1) | 2 tomas héroe: pruebas en Veo rápido (64) + 2 finales en ultra (240) | **≈ 64 a 304** |
| **D · Idea 1** (calle → atardecer final) | porche "dron" (Kling 8,75) + elevación final (Veo ultra 120) + reutiliza el paneo | **≈ 150** |
| **E · Idea 3** (interactivo) | fachada al atardecer (Veo rápido 32) + 4 micro-movimientos (Kling estándar 30) | **≈ 70** |
| **F · Idea 4 versión B** | 1 motorizado de ficción (4) + 3 clips (Kling pro 26) + reutiliza renders de la idea 2 | **≈ 40** |
| **Total aproximado** | | **≈ 560 a 800** (cabe en los 801 créditos, **ajustado**) |

**Cómo no pasarnos:** se hace **por etapas**; antes de cada una te digo el costo exacto y espero tu «dale». Si hace falta, se baja el número de tomas por rubro (de 5 a 4) o se usa Veo rápido también en las finales.

## Reglas de prompt (para todas las ideas)

**Bloque de fidelidad (siempre al inicio):**
`Use the reference image as the exact source. Keep the building's structure identical: same number of floors, same narrow frontage, same green terrace roof, same window and door positions, same bars pattern, same porch roof, same neighboring buildings and street. Do not add or remove floors, windows or structural elements. No people, no readable text, no logos, no brand names, no license plates.`

**Bloque de calidad y luz (siempre al final):**
`Ultra-realistic, photographic, true-to-life colors, natural warm golden-hour light with soft long shadows, gentle film grain, subtle lens realism, cinematic but natural and human, 4K detail, no artificial glow, no plastic or CGI look.`

**Negativos útiles:** `no distortion of walls, no melting geometry, no extra windows, no changed roof, no fantasy elements, no oversaturation, no text.`

## Quitar los carros de las fotos de la fachada
- **Ya hay una foto sin carros: IMG_1881** (la maestra para los renders).
- Para tomas frontales (IMG_3339, 3335, 3336…): edición de imagen con **Nano Banana Pro** o **FLUX 3**: `Remove the parked cars from the street in front of the building and restore the pavement and the lower wall exactly as they would continue; do not change anything else.` Se compara con IMG_1881 y se descarta si **inventa** puertas, rejas o paredes. (Los videos 1876–1879 llevan el carro adelante: no se limpian; se usan solo como referencia.)

## Caída del cielo: coordenadas reales
Coordenadas: **10,468938; −66,541720** (Guatire). Si Google Earth Studio no abre, la caída se genera con IA y **termina en la foto real de la calle** (3350) o la fachada (1881); no cambia el guion.

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
