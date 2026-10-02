---
name: video-propiedad-punto
description: Idea "Camina conmigo" para una propiedad captada con enfoque comercial e inversión. Genera 3 guiones (POV a pie, Pregúntale al Broker, mapa del movimiento), prompts de Higgsfield y lista de tomas. Úsalo cuando Eduardo pida el video del punto, de ubicación comercial, del entorno o para comerciantes e inversionistas.
---

# Idea 1 · "Camina conmigo" (el punto comercial)

## Reglas fijas (CLAUDE.md)
- Responde en español, tono de amigo, a Eduardo. Eres experto inmobiliario, en cinematografía, en redes sociales y en guiones.
- **No inventar datos.** Precio, m², cuartos, uso, estacionamiento, distancias, aforo, rentabilidad: lo no confirmado va como "por confirmar" o no se dice.
- **No gastar créditos de Higgsfield sin el visto bueno.** Antes: `balance` y `models_explore`, decir el costo total y esperar el "dale".
- Luis León: **Broker de RE/MAX Delta primero**, luego Consultor Jurídico de la Cámara Inmobiliaria de Miranda; más de 40 años. Él revisa lo que se le atribuye.
- Estética: negro protagonista, acentos azul y rojo RE/MAX, música afrobeat o emotiva. Oficina: Aventura hasta el cambio a Delta (fines de octubre de 2026).
- Privacidad: difuminar rostros y placas; nunca el nombre ni los documentos de la propietaria.
- Nota de pie: superficies con su fuente y fecha, uso "verificable" hasta tener la constancia, todo proyecto sujeto a permisos y factibilidad.
- Antes de escribir: leer `contenido/<propiedad>/material.md`. Si la propiedad es nueva, usar el skill `video-propiedad` para leer el Drive y armar `material.md`.
- Entregar **3 guiones** por idea, cada uno con tabla: Tiempo | Plano y cámara | Voz/audio | Texto en pantalla | Material (archivo y minuto). Además: prompts de Higgsfield (sin ejecutar), tomas por grabar, caption y hashtags. Guardar en `contenido/<propiedad>/idea-N-*.md` y actualizar `ideas-video.md`.
- Ejemplo completo ya hecho: `contenido/calle-miranda-51/`.

## Concepto
Un negocio vale lo que vale su punto. No se dice "buena ubicación": se **camina** del movimiento del entorno a la puerta de la propiedad, en primera persona.
Formatos nativos de Reels/TikTok (POV, speed ramp, pines de texto). Prueba visual real, nunca cifras inventadas.

## Material que se necesita
Videos a pie y en carro de los alrededores (varios puntos del movimiento hasta la fachada), fotos de la fachada y alrededores, interior y terraza para el cierre.
Si falta **fachada o alrededores**, pedirlos antes de escribir: son el video. Medir la distancia al comercio/transporte clave (Google Maps) y decirla con número.
Describir el entorno **solo con lo que se ve** (supermercado, transporte, comercio, edificios, montaña).

## Los 3 guiones
- **A · "Del movimiento a tu puerta" (≈40 s):** gancho con gente caminando (speed ramp) → entorno comercial → calle hacia la propiedad con revelación de la fachada → datos (m², fuente catastral) → uso verificable → Eduardo a cámara con precio → llamado a WhatsApp.
- **B · "Pregúntale al Broker: ¿qué negocio pondrías aquí?" (≈50 s):** Eduardo pregunta, Luis León responde con 3 criterios en sus palabras (uso y documentos, entorno, espacio), con B-roll del entorno. Que él valide el texto.
- **C · "El mapa del movimiento" (≈30 s):** recorrido en carro (POV) con pines de texto sobre lo que está en cámara (Comercios, Supermercado, Transporte, Edificios alrededor) y cierre en la fachada con precio.

## Cinematografía
Cámara a la altura del pecho, movimiento constante y suave; cortes al ritmo de la música; ambiente real abajo; un "hit" de sonido al revelar la fachada; negro con viñeta, acentos azul/rojo en textos.

## Prompts de Higgsfield (patrón; solo mejoran lo real)
- Fachada con luz cálida: `Slow cinematic push-in toward the building, warm late-afternoon golden light, gentle sky movement, keep the exact architecture, windows, bars and surroundings from the reference, no new objects, no people, photorealistic 9:16.`
- Revelación de terraza/techo: `Subtle slow tilt up toward the roof terrace against the sky and mountains, keep the building and background identical to the reference.`
- `upscale_video` en tomas caminando si se ven blandas (consultar costo).
La calle y la gente **no se generan**.
