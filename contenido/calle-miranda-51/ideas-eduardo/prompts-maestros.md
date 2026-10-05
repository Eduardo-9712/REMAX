# Prompts maestros (sirven para cualquier propiedad y cualquier video de transformación)

**Estado:** versión 1 (05-10-2026), con lo aprendido en la prueba del 04-10 y la **regla de obra con obreros** que pidió Eduardo.
**Higgsfield:** estos prompts **no se ejecutan** sin el «dale» de Eduardo. Costos reales: `higgsfield-calidad.md`. Skill que los usa: `video-propiedad-maestro`.

**Fórmula:** `[BLOQUE DE FIDELIDAD] + [instrucción específica] + [BLOQUE DE CALIDAD Y LUZ]`

---

## 1 · Bloques base

**Fidelidad (siempre al inicio):**
`Use the reference image as the exact source. Keep the building's structure identical: same number of floors, same frontage, same terrace roof, same window and door positions, same roof lines, same neighboring buildings and street. Do not add or remove floors, windows or structural elements. No readable text, no logos, no brand names, no license plates.`

**Calidad y luz (siempre al final):**
`Ultra-realistic, photographic, true-to-life colors, natural warm light, gentle film grain, cinematic but natural and human, 4K detail, no artificial glow, no plastic or CGI look.`

**Negativos útiles:** `no distortion of walls, no melting geometry, no smearing, no flicker, no extra windows, no changed roof, no fantasy elements, no oversaturation.`

---

## 2 · REGLA MAESTRA DE REMODELACIÓN (decidida por Eduardo el 05-10-2026)

> **Toda remodelación se genera LARGA, con OBREROS trabajando, y se ACELERA a 2× en la edición.** Así se ve rápida y corta, pero con vida y realismo.

| Regla | Qué significa |
|---|---|
| **1. Generar largo, publicar a 2×** | **Fachada: generar 10 s → publica 5 s.** **Interiores: generar 5 s → publica 2,5 s.** (Más dramático: 1,5×.) La velocidad se aplica en CapCut con flujo óptico o mezcla de cuadros y algo de desenfoque de movimiento. |
| **2. Obreros visibles** | **3–4 obreros en la fachada y 2 por interior**, con **casco, chaleco reflectivo y overol**, en plano medio o general, **de espaldas o de perfil, sin rostros nítidos**, sin logos ni texto. Trabajan de verdad: **pintan, instalan vidrios y puertas, sueldan (chispas), arman andamio, cargan materiales, colocan plantas**. |
| **3. Secuencia de obra** | (a) **desmontan lo anterior** (letrero, vitrinas, mobiliario, rejas); (b) sube un **andamio con malla verde de seguridad**; (c) **trabajos** a la vista; (d) **retiran la malla**; (e) **remates** (plantas, luces); (f) **reveal** con barrido de luz. |
| **4. Estructura intacta** | La obra **no cambia el volumen** ni la distribución: solo acabados, vidrio, mobiliario, luz y función. La terraza de techo verde no se cubre con tablas. |
| **5. Cámara** | **Trípode fijo** (sin movimiento) para que el inicio y el final calcen; un leve empuje solo si se pide. |
| **6. Sonido (en edición)** | Martillo, taladro, soldadura, mezcladora, radio de obra suave y, al revelar, un *whoosh* + acorde. La obra suena muy bien (ASMR). |
| **7. Rótulo** | Siempre **"Recreación con IA · No es un proyecto aprobado"**. |
| **8. Los obreros son ficción de IA** | Personajes genéricos, no personas reales ni identificables. |

### Costos con la regla (Kling v3.0 pro, sin sonido; consultados el 05-10)
| Pieza | Generar | Créditos | Publica |
|---|---|---|---|
| **Fachada** | 10 s | **17,5** | 5 s (2×) |
| **Interior** | 5 s | **8,75** | 2,5 s (2×) |
| Opcional más largo | 8 s = 14 · 15 s = 26,25 | | |

---

## 3 · Prompt maestro: transición de **FACHADA** con obreros (10 s)
Imagen inicial = foto real o render del rubro anterior · Imagen final = render del siguiente rubro · Kling v3.0 pro · 9:16 · sin sonido.

`Locked-off tripod camera, no camera movement, identical framing throughout. A realistic architectural renovation time-lapse of this exact building, starting exactly from the start image and ending exactly on the end image. A small crew of three to four construction workers in hard hats, high-visibility vests and work overalls, seen from behind or in profile at medium and wide distance, faces not visible, work continuously: one removes the old [elementos anteriores: signage, glass front, iron bars] with an angle grinder (sparks), two install the new [vidrios, puertas, vitrina] , one paints the walls with a roller from a ladder, one carries materials and large planters with a wheelbarrow. First the previous fit-out is dismantled, then a light metal scaffolding with translucent green safety netting rises only in front of the work area, light dust, a small cement mixer, tools and materials on the sidewalk; then the new fit-out is built step by step; finally the scaffolding and netting are removed, plants and lights are placed, and the scene ends exactly on the end image. [Si la hora cambia: the sky shifts smoothly from daylight to blue-hour dusk.] The building volume, window positions, terrace roof, roof lines and neighboring buildings never change shape. No wooden planks covering the facade, no smearing, no melting, no flicker. No text, no logos, no license plates, no readable faces. Premium architectural time-lapse, natural light, true-to-life colors.`

## 4 · Prompt maestro: transición de **INTERIOR** con obreros (5 s)
Imagen inicial = espacio real o render del rubro anterior · final = render del rubro nuevo · Kling v3.0 pro · 9:16.

`Locked-off camera, identical framing. A realistic interior renovation time-lapse of this exact room, from the start image to the end image. Two workers in hard hats, high-visibility vests and overalls, seen from behind or in profile, faces not visible, work: one removes the previous [mobiliario/equipos], one paints the walls and installs [el nuevo mobiliario/equipos]; light dust, ladders, drop cloths and tools. The walls, ceiling, windows, doors, stairs, columns and floor pattern never change. Ends exactly on the end image with the lights switched on. No smearing, no melting, no flicker, no text, no logos, no readable faces.`

## 5 · Prompt maestro: render del "después" (imagen)
Nano Banana Pro · 4K · 9:16 · **2 referencias**: (1) la foto real **recortada a 9:16** (composición) y (2) una vista despejada del mismo espacio (para entender la estructura).

`[BLOQUE DE FIDELIDAD] Edit the FIRST reference image and keep its exact composition, camera angle and framing. The SECOND reference shows the same space unobstructed: use it only to understand the structure. KEEP IDENTICAL: [lista de lo que no cambia]. CHANGE ONLY: [lista de lo que cambia: planta baja, acabados, mobiliario, luz]. Remove [carro/obstáculo]. Mood: [hora y ambiente]. [BLOQUE DE CALIDAD Y LUZ]`
*(Creatividad permitida por Eduardo: estacionamiento, plantas, luces, detalles de lujo… siempre acorde a la estructura real.)*

## 6 · Apertura y tomas héroe
- **Caída tipo Google Earth (referencia final: foto de la calle):** `Google Earth style zoom from outer space: stars, the curvature of the Earth turning from night to day, clouds, the Caribbean coast of Venezuela, the coastal mountain range, a valley and a town, then a rapid descent searching for one specific narrow street and landing at street level on the exact reference street; smooth continuous camera, a small location pin appears near the end, no text, no labels; vertical 9:16.` *(Nombres y pin: en edición.)* Modelo: Veo 3.1 rápido para probar (32), ultra para la final (120).
- **Paneo 360 al atardecer:** `Slow cinematic drone orbit starting at the front and rotating up to 35 degrees each side while rising slightly, warm golden-hour light, keep the exact facade, terrace, neighbors and street from the references; do not invent unseen sides.`
- **"Dron" entrando / vuelo interior / elevación final:** ver `idea-1-el-viaje.md`.

## 7 · Preparación de las fotos
1. Convertir HEIC a JPG de alta calidad. 2. **Recortar a 9:16** centrado en lo importante (una foto 3:4 pierde un 25 % de ancho; revisar que no se corte nada clave). 3. Subir la foto principal y **una referencia despejada**. 4. Nunca subir documentos ni datos personales.

## 8 · Lo aprendido en la prueba del 04-10
- Con **dos referencias** la IA entiende mejor la estructura.
- **Describir la obra paso a paso** y pedir "sin tablas, sin derretidos, sin parpadeos" evita fallos.
- La **malla verde de seguridad** da un look muy natural (Venezuela).
- La IA quitó los **cables aéreos** y agregó **banqueta**: avisar siempre.
- **Cada intento cuesta**: probar con una variante y repetir solo si hace falta.

## 9 · Control de calidad antes de aprobar
Comparar **lado a lado** con la foto real. Rechazar si cambia: niveles, terraza/techo, posición de ventanas y puertas, vecinos, forma de la calle; si hay letras, logos, placas o **rostros nítidos**; si algo "se derrite" o parpadea.
