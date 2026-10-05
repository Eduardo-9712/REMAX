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
| **1. Generar largo, publicar a 2×** | **Fachada: generar 10 s → publica 5 s (10 obreros).** **Interiores: generar 5 s → publica 2,5 s (5 obreros).** (Más dramático: 1,5×.) La velocidad se aplica en CapCut con flujo óptico o mezcla de cuadros y algo de desenfoque de movimiento. |
| **2. Obreros visibles** | **10 obreros en cada fachada y 5 por interior** (confirmado por Eduardo, 05-10), con **casco, chaleco reflectivo y overol**, en plano medio o general, **de espaldas o de perfil, sin rostros nítidos**, sin logos ni texto. Trabajan de verdad: **pintan, instalan vidrios y puertas, sueldan (chispas), arman andamio, cargan materiales, colocan plantas**. |
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

`Locked-off camera, identical framing. A realistic interior renovation time-lapse of this exact room, from the start image to the end image. Five workers in hard hats, high-visibility vests and overalls, seen from behind or in profile, faces not visible, work: two remove the previous [mobiliario/equipos], one paints the walls, two install [el nuevo mobiliario/equipos]; light dust, ladders, drop cloths and tools. The walls, ceiling, windows, doors, stairs, columns and floor pattern never change. Ends exactly on the end image with the lights switched on. No smearing, no melting, no flicker, no text, no logos, no readable faces.`

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

---

# AÑADIDOS DEL 05-10-2026 (decisiones de Eduardo sobre la lista "para un video espectacular")

**Decisiones de Eduardo:** (1) **10 obreros** en las remodelaciones de **fachada**; (2) **camión de materiales y hormigonera solo en la PRIMERA fachada** (restaurante); en los otros rubros solo están los obreros remodelando hacia el siguiente rubro; (3) **reveal con "inauguración"** (luces y siluetas lejanas de gente) **al menos en el restaurante y el concesionario**; (4) **plano animado con el croquis real**: SÍ; (5) **sonido por rubro / obra como ASMR**: SÍ; (6) **4 mini-reels** además del video maestro: SÍ; (7) **letrero en blanco** y el nombre del rubro lo pone Eduardo en edición.
**Confirmado (05-10): afuera, en cada transformación de rubro, son 10 obreros; adentro son 5. El camión de materiales y la hormigonera solo salen en la PRIMERA transformación de la fachada (restaurante).** **Precio: SÍ en el cierre.** **Final en 4 paneles: SÍ.** **Maqueta isométrica: SÍ.** **Subtítulos: en español (no en inglés).** **Kit gráfico: NO.**

## 10 · Bloque de obra con 10 obreros (fachada, todas)
Se **agrega a la transición de fachada** (sección 3). Reemplaza "three to four workers":
`A crew of ten construction workers in hard hats, high-visibility vests and work overalls, seen from behind or in profile at medium and wide distance, faces not visible, working in coordinated groups: two on the scaffolding installing glass panels, two carrying wooden panels and planters, two painting walls with rollers from ladders, one using an angle grinder with sparks, one operating a small cement mixer, two removing the previous fit-out. Light dust and warm work lights; every worker is busy and distinct, no faces visible, no text on clothing.`

## 11 · Bloque de camión y materiales (SOLO la primera fachada: restaurante)
`At the start, a flatbed truck arrives and parks at the curb with building materials (large glass panels, wooden panels, planters, paint buckets, bags of cement); workers unload with hand trolleys. The truck has no text, no logo and no readable license plate. By the end of the sequence the truck has left.`
*(En las fachadas siguientes no hay camión: solo los obreros desmontando y montando.)*

## 12 · Bloque de letrero en blanco (todas las fachadas)
`A large blank sign band above the entrance is installed with a crane-free hand lift by two workers; the sign is plain, dark, softly lit and completely blank: no text, no letters, no logo.`
**En edición:** Eduardo escribe el **nombre del rubro** con el texto exacto (tipografía y color de la marca).

## 13 · Bloque de reveal "inauguración" (restaurante y concesionario)
Se usa como **imagen final** de la transición o como un **clip corto de 5 s** posterior (+8,75 créditos):
`The finished building at blue-hour dusk, all lights on, a warm opening-night atmosphere: about ten distant silhouettes of people (guests and visitors) arriving and walking near the entrance, far from the camera, backlit and blurred, no faces visible, no readable text, no logos. [Restaurante: a soft glow from inside, guests at the tables behind the glass.] [Concesionario: generic unbranded motorcycles lit on display, a few visitors looking at them.] Locked-off camera, slow subtle push-in.`
*(Siluetas lejanas y borrosas, sin rostros; se rotula como recreación con IA.)*

## 14 · Chispas, pintura con pistola y polvo (todas)
`Occasional welding or grinder sparks, a worker spraying paint with a spray gun in a soft cloud, light dust drifting in the work lights; satisfying, realistic, never covering the structure.`

## 15 · Plano animado con el croquis real (se hace en CapCut/Canva, **0 créditos**)
1. **Base:** redibujar limpio el **croquis** (planta baja y segundo piso) sobre fondo **negro**, líneas blancas y azules, **sin medidas** (no inventar). Rótulo: **"Plano ilustrativo, no a escala"**.
2. **Línea de recorrido** en **rojo** que sigue **la ruta real**: estacionamiento y porche → sala → comedor → pasillo → cocina → gran salón → patio → fondo → escalera → segundo piso → terraza.
3. **Se detiene en cada espacio** y **se ilumina la zona del rubro** con su color: restaurante (cocina, gran salón, patio, terraza), concesionario (estacionamiento, porche, sala, fondo), coworking + estudio (salas, gran salón, cuartos, balcón-salón), spa (cuartos, baños, patio, terraza).
4. **Texto en pantalla:** nombre del espacio y del rubro. **Voz:** "Aquí iría…".
5. **Versión opcional con IA:** una **maqueta isométrica en corte** hecha desde el croquis (Nano Banana Pro, 4 créditos) para un plano "wow"; se rotula **"Ilustración conceptual"** y se revisa que no invente habitaciones.
**Usos:** 1) escena de 6–8 s dentro del video maestro; 2) **reel propio de 20 s** "La casa por dentro".

## 16 · Cifras reales en pantalla (0 créditos)
**419,86 m² de construcción · 295,41 m² de terreno · 6 cuartos · 4 baños · 2 estacionamientos.** *(Eduardo no incluyó el precio en esta lista; se mantiene **USD 120.000** en el cierre, según su decisión anterior, salvo que él diga lo contrario.)* Las cifras entran con un golpe de música, en la tipografía de la marca.

## 17 · Sonido por rubro y de obra (0 créditos)
| Momento | Sonido |
|---|---|
| **Obra (todas)** | martillo, taladro, amoladora con chispas, mezcladora, andamio, radio de obra suave: **ASMR** |
| **Restaurante** | cuchillos, sartenes, copas, murmullo suave |
| **Concesionario** | motor encendiendo, aceleración corta, llave y tubo de escape |
| **Coworking + estudio** | teclado, obturador de cámara, flash |
| **Spa** | agua, campanillas, respiración |
| **Reveal (todos)** | silencio de 0,5 s → *whoosh* → acorde (la misma "firma sonora" en los 4) |

## 18 · Los 4 mini-reels (20–25 s cada uno), con el mismo material de la cadena
**Estructura:** gancho (2 s) → fachada con obra (5 s a 2×) → 3 tomas interiores (7,5 s) → reveal (5 s) → cierre con cifras y "Escribe CASA" (3 s).
| Reel | Voz en off (borrador) |
|---|---|
| **1 · Restaurante gastronómico** | "¿Y si esta casa fuera un restaurante gastronómico? Mira cómo cambia. Una cocina de alto nivel, un gran salón para el servicio, un patio para cenar al aire libre… y arriba, la terraza con la cordillera. Calle Miranda 51, Guatire. USD 120.000. Escribe CASA." |
| **2 · Concesionario de motos** | "¿Y si fuera un concesionario de motos? En esta zona las motos se ven por todas partes. Vitrina a la calle, exhibición adentro, un patio para entregas y un taller al fondo. Calle Miranda 51, Guatire. USD 120.000. Escribe CASA." |
| **3 · Coworking + estudio** | "¿Y si fuera un coworking con estudio de fotografía y video? Recepción, un gran salón para el set… y arriba, un cuarto con un secreto: abres la puerta y aparece un salón de techo de madera. Calle Miranda 51, Guatire. USD 120.000. Escribe CASA." |
| **4 · Spa** | "¿Y si fuera un spa? Cabinas para desconectar, baños de relajación, un patio convertido en jardín y una terraza para ver el atardecer. Calle Miranda 51, Guatire. USD 120.000. Escribe CASA." |
*(Todas llevan: "Recreación con IA · No es un proyecto aprobado" y la nota de pie: uso residencial y comercial verificable, sujeto a permisos y factibilidad.)*


## 19 · Final en 4 paneles (APROBADO por Eduardo, 05-10) — edición, 0 créditos
1. La pantalla se divide en **4 paneles**: los 4 rubros terminados (restaurante, concesionario, coworking + estudio, spa), cada uno con sus luces del reveal.
2. Los paneles **se funden de nuevo a la foto real de hoy** (la fachada tal como está).
3. Texto grande: **"1 propiedad · 4 posibilidades · 1 decisión · Escribe CASA"** y el precio **USD 120.000**.
4. Cierra con la firma sonora y la voz: "Tú decides cuál. Ven a verla."

## 20 · Subtítulos en español (decisión de Eduardo, 05-10)
**Los videos llevan subtítulos en español** (la misma voz en off de Eduardo, texto grande y legible, para que se entienda sin sonido). **No se hacen subtítulos en inglés.**

## 21 · Maqueta isométrica del croquis (APROBADA por Eduardo, 05-10)
**Qué es:** un dibujo en 3D de la casa "cortada" y vista desde arriba en diagonal, como una **casa de muñecas**: se ven los cuartos, la cocina, el patio y la terraza. Se hace a partir del croquis real, con los 4 rubros pintados en colores. Se usa dentro del plano animado.
**Cómo se hace:** 1 imagen con Nano Banana Pro a partir del croquis (≈ **4 créditos**) y, si se quiere, una animación corta (≈ **8,75**). Se rotula **"Ilustración conceptual, no a escala"** y se revisa que **no invente habitaciones** ni medidas.
`Isometric cutaway illustration of a three-level house with a long courtyard, based exactly on the reference floor plan sketch: same rooms in the same order from the street to the back, parking and porch at the front, stairs, kitchen, great hall, courtyard, service rooms at the back, second-floor rooms and balconies, rooftop terrace with a green roof; dark elegant style on a black background with thin white and blue lines; the rooms are softly colored in four groups; no text, no numbers, no measurements; clean, premium, conceptual.`
