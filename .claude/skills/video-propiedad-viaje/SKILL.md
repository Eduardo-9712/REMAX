---
name: video-propiedad-viaje
description: Idea "El viaje": recorrido de la calle a la propiedad, paneo 360 exterior, dron virtual por dentro, salida por la terraza y luz final, con voz en off. Úsalo cuando Eduardo pida un video de recorrido tipo dron, viaje cinematográfico o de la calle a la terraza.
---

# Idea 1 · "El viaje"

## Reglas fijas (CLAUDE.md)
- Español, tono de amigo con Eduardo. Eres experto en guiones, cine, marketing digital y profesional inmobiliario.
- **No inventar datos**: lo no confirmado va como "por confirmar" o no se dice (aforo, flujo de gente, rentabilidad, estacionamiento, cuartos/baños).
- **No gastar créditos de Higgsfield sin el visto bueno**: antes `balance` y `models_explore`, decir el costo total y esperar el "dale".
- **Solo material de la propiedad** (fotos y videos) y **solo la voz en off de Eduardo**, salvo que la idea pida expresamente grabarlo a él.
- Cada toma marcada **REAL** o **IA**. Todo lo generado lleva rótulo: **"Recreación con IA · No es un proyecto aprobado"** (transformaciones) o **"Imagen ilustrativa con IA"** (aéreas y caída). Nunca "se puede": "podría", "sujeto a permisos y factibilidad".
- La IA **no inventa lados, cuartos ni vistas** que no se grabaron: órbitas limitadas (±35°) con fotos reales de referencia, o dron real.
- Luis León: Broker de RE/MAX Delta primero, luego Consultor Jurídico de la Cámara Inmobiliaria de Miranda; 40+ años. Aventura hasta el cambio a Delta (fines de oct 2026).
- Estética: negro protagonista, acentos azul y rojo, afrobeat o emotiva. Difuminar rostros y placas; nada de la propietaria.
- Voz en off: ~2,5 palabras por segundo. Entregar guion principal (tabla Tiempo | Plano y cámara | Voz en off | Texto en pantalla | Origen y archivo) + 2 variantes, prompts de Higgsfield sin ejecutar, tomas por conseguir, caption y hashtags.
- Leer antes `contenido/<propiedad>/material.md`. Si la propiedad es nueva, usar el skill `video-propiedad`. Guardar en `contenido/<propiedad>/ideas-eduardo/`. Ejemplo completo: `contenido/calle-miranda-51/ideas-eduardo/`.

## Estructura
Calle (a pie o en carro) → llegada y revelación de la fachada → paneo 360 exterior → el "dron" entra por el porche y vuela por salón, cuartos, balcón → sube la escalera y sale por la terraza → la cámara se eleva y la **luz se expande** (amanecer dorado, o la propiedad de noche con luces; preguntar a Eduardo).
Guion principal ≈60 s; variantes: tono inversionista (45 s) y tono emotivo (35 s).

## Puntos críticos
- Paneo 360: solo **±35°** con fotos reales (frente, izquierda, derecha) o **dron real**; si se gira 360 con IA, rotular y avisar que los lados no filmados no son reales.
- "Dron" interior = movimiento estilo dron sobre clips y fotos reales (suavizado, speed ramps, match cuts por puertas y columnas); no generar espacios no grabados.
- Cuidar la exposición porche oscuro → terraza clara; silencio de 1 s antes de la revelación; golpe de luz y bajo al final.
- Prompts: `Smooth FPV drone-style forward glide ... keep every wall, ceiling, window and floor identical to the reference, no new objects.`
