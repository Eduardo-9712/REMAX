# Calle Miranda N.º 51 · 3 ideas de video (borrador para aprobar)

**Enfoque (Eduardo, 01-10):** comercial, inversión y redesarrollo, sin dejar de ser casa. El valor está en **el punto y los alrededores**.
**No se ha gastado ningún crédito.** Cada idea tiene su skill en `.claude/skills/`.
Datos: `material.md`. Precio **USD 120.000**. Nota de pie en todos: *"Superficies según ficha catastral del 17/08/2023.
Uso residencial y comercial, verificable con constancia de uso conforme. Todo proyecto sujeto a permisos y factibilidad."*
Tomas de los alrededores y fachada: **por llegar** (Eduardo las sube); los guiones las marcan con 🆕.

Para los 3: reel 9:16, música afrobeat/emotiva, negro con acentos azul y rojo. Higgsfield solo anima material **real**,
salvo la Idea 2, donde las imágenes son **recreaciones ilustrativas** y se rotulan así.

---

## Idea 1 · "El punto" (comercial e inversión) — skill `video-propiedad-punto`

**Para quién:** comerciantes, inversionistas locales y del exterior. **Duración:** 35–45 s.
**Mensaje:** en el casco central de Guatire, 420 m² de construcción en una esquina con movimiento. Tu negocio ya tiene ubicación.

| Tiempo | Imagen | Voz / texto |
|---|---|---|
| 0–3 | 🆕 Fachada de día | "¿Dónde pondrías tu negocio en el casco central de Guatire?" |
| 3–12 | 🆕 Recorrido en carro / caminando por los alrededores | "Esto es lo que rodea la propiedad." *(nombrar solo lo que se vea: comercios, vías, transporte)* |
| 12–20 | Terraza y salón (reales) | "419,86 m² de construcción sobre 295,41 m² de terreno." |
| 20–30 | Salón y escalera | "Uso residencial y comercial, verificable." |
| 30–38 | Eduardo a cámara frente a la fachada | "USD 120.000. Con Luis León, Consultor Jurídico, revisamos documentos y uso antes de que des el paso." |
| 38–45 | Texto | "Ven a verla. Escríbeme por WhatsApp." |

**Prompts Higgsfield (image-to-video, referencia real, 5 s):**
1. `Slow cinematic push-in on the building facade from street level, golden hour, subtle parallax, keep the exact architecture, signs and surroundings from the reference, no new objects or people.` *(con la foto de fachada 🆕)*
2. `Smooth forward glide along the street in front of the property, daylight, natural motion of the scene, keep everything identical to the reference.` *(con foto de la calle 🆕)*
3. `Slow dolly forward through the large hall with dark wooden coffered ceiling and sun rays on the tile floor, keep every element identical to the reference.` *(IMG_1769)*
4. `Slow push-in on the covered rooftop terrace with mountains and city in the background, golden hour, keep layout unchanged.` *(IMG_1753)*

---

## Idea 2 · "¿Qué harías con 420 m²?" (redesarrollo) — skill `video-propiedad-redesarrollo`

**Para quién:** inversionistas, emprendedores, constructores. **Duración:** 30–40 s.
**Mensaje:** la propiedad puede ser casa, oficina, local, restaurante… tú decides. Es el video que más usa la IA.
**Regla:** las imágenes de "después" son **ilustrativas** (rótulo "Recreación con IA, no es un proyecto aprobado"). Nunca presentarlas como obra existente ni como lo que "se puede" construir sin permisos.

| Tiempo | Imagen | Voz / texto |
|---|---|---|
| 0–3 | Salón real vacío (IMG_1768) | "Esto hoy es una casa." |
| 3–8 | Transición a una recreación: restaurante | "Mañana puede ser un restaurante…" |
| 8–13 | Transición: oficinas o consultorios | "…oficinas o consultorios…" |
| 13–18 | Transición: local comercial en planta baja | "…o un local con frente a la calle." |
| 18–25 | Terraza real con vista a la montaña | "Y esta terraza ya trae la vista." |
| 25–32 | Eduardo a cámara | "420 m² para reconvertir o redesarrollar. USD 120.000. Sujeto a permisos y factibilidad." |
| 32–38 | Texto | "Ven a verla y dime qué ves tú." |

**Prompts Higgsfield (primero imagen con `generate_image` desde la foto real, luego video):**
1. Restaurante: `Transform this exact empty hall into a modern restaurant interior: keep the dark wooden coffered ceiling, central column, windows and tile floor unchanged; add warm pendant lights, wooden tables, black chairs and a bar counter. Photorealistic, same camera angle.`
2. Oficinas: `Same room, same ceiling and windows, converted into a bright modern open office with black desks, glass partitions and plants. Photorealistic, same camera angle.`
3. Local comercial: `Same facade reference, ground floor converted into a modern retail storefront with large glass windows and an illuminated sign area, black and white palette. Keep the upper floors untouched.` *(con la fachada 🆕)*
4. Animar cada resultado: `Slow push-in, subtle light shimmer, keep the generated scene stable.`

---

## Idea 3 · "Ven a verla" (recorrido real e invitación) — skill `video-propiedad-recorrido`

**Para quién:** compradores y comerciantes de Guarenas/Guatire/Caracas. **Duración:** 45–60 s.
**Mensaje:** abierta, real, sin filtros: ven, camina el espacio y hablamos. Es el que más cierra visitas.
**Formato:** casi todo material real; Higgsfield solo para estabilizar y dar un toque de luz en 2 o 3 tomas.

| Tiempo | Imagen | Voz / texto |
|---|---|---|
| 0–4 | 🆕 Eduardo llegando a la fachada | "Te voy a enseñar una propiedad en el corazón de Guatire." |
| 4–15 | Planta baja (IMG_1764/1765, Cuarto 1) | "Entramos: salón amplio, techo de madera, mucha luz." |
| 15–25 | Escalera y cuartos (Escaleras terraza, Cuarto 2) | "Subimos: cuartos y corredor con vista." |
| 25–38 | Terraza (IMG_1753, 1755, copy_7183…) | "Y arriba, la terraza con vista a la montaña." |
| 38–48 | Eduardo a cámara | "420 m² de construcción, 295 m² de terreno, USD 120.000, uso residencial y comercial verificable." |
| 48–58 | Luis León (opcional) + texto | "Con el respaldo de RE/MAX y la experiencia de Luis León. Agenda tu visita por WhatsApp." |

**Prompts Higgsfield (opcionales, 5 s):**
1. `Gentle stabilization and slow forward motion, keep the exact interior from the reference, natural daylight.` *(IMG_1764)*
2. `Slow upward tilt along the staircase to the skylight, soft sun rays, keep the stairs and curtains identical.` *(IMG_1784)*
3. `Slow lateral slide on the rooftop terrace toward the mountains, golden hour, keep layout unchanged.` *(copy_7183…)*

---

## Qué necesito para cerrar las 3

1. Nuevo enlace (o confirmar que ya está subido) con fachada, calle y alrededores; las fotos que dices que adjuntaste no me llegaron.
2. ¿Qué hay alrededor? (comercios, vías, transporte, Plaza Bolívar): lo describo solo lo que se vea o me confirmes.
3. ¿Eduardo, Luis León o los dos a cámara? ¿Cuál grabamos primero?
4. ¿El precio de 120.000 va **visible** en el video o solo "consúltalo"?
5. Constancia de uso conforme (cuando la tengas) para decir "uso comercial" sin el "verificable".
