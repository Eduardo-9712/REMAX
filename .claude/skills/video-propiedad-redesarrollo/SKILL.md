---
name: video-propiedad-redesarrollo
description: Idea "¿Qué harías con estos m²?" de una propiedad captada: reconversión y redesarrollo con recreaciones de IA rotuladas. Genera 3 guiones (tres negocios, tres caminos del inversionista con Luis León, comenta 1-2-3), prompts de Higgsfield y lista de tomas. Úsalo cuando Eduardo pida el video de potencial, reconversión, redesarrollo o antes/después con IA.
---

# Idea 2 · "¿Qué harías con estos m²?" (reconversión y redesarrollo)

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
La propiedad como **pregunta**: foto real "hoy" → recreaciones con IA "mañana" (local, restaurante, oficinas, mixto) → terraza/vista real → precio y llamado.
Transformaciones antes/después con IA: gancho natural, comentarios, guardados. Educativo: reconvertir depende de **permisos, uso conforme y estudio estructural**.

## Reglas especiales (este video sí inventa imágenes)
1. Cada imagen generada lleva el rótulo permanente **"Recreación con IA · No es un proyecto aprobado"** (o "Concepto ilustrativo").
2. Decir "podría", nunca "se puede"; siempre "sujeto a permisos, uso conforme y estudio estructural".
3. Conservar estructura, techo, ventanas y proporciones reales en el prompt; solo cambia mobiliario, luz y función.
4. Abrir y cerrar con material real. Sin marcas legibles ni personas en los renders.
5. Los usos son ideas; nada de promesas de rentabilidad ni de demanda.

## Los 3 guiones
- **A · "Una propiedad, tres negocios" (≈35 s):** fachada real (HOY) → barrido de luz → local → restaurante → oficinas → terraza real → Eduardo con precio → "ven a verla y dime qué ves tú".
- **B · "Los 3 caminos del inversionista" (≈50 s, con Luis León):** reutilizar, transformar, redesarrollar (los 3 caminos de la ficha técnica), cada uno con imágenes reales o renders rotulados; cierre: primero se revisan uso, permisos y estructura.
- **C · "Comenta 1, 2 o 3" (≈25 s):** tres renders de 5 s numerados, terraza real y llamado: "comenta 1, 2 o 3 y te mando la ficha".

## Cinematografía
Transición "barrido de luz"; "hoy" frío y apagado, "después" cálido y saturado; música con build-up que estalla en la toma real final.

## Proceso con Higgsfield
1. Elegir 2–3 fotos reales con buen ángulo (fachada recta, salón, cuarto, terraza).
2. `generate_image` con la foto de referencia y el patrón: `Edit this exact photo: keep the structure, proportions, ceiling, windows and street unchanged; convert only <espacio> into <uso> with <materiales, luz>; photorealistic, same camera angle, no people, no readable brand names.`
3. Mostrar los prompts y **esperar el "dale"** antes de generar; revisar que no invente elementos.
4. Animar cada render aprobado: `Slow cinematic push-in, subtle light shimmer, keep the generated scene stable, no new objects.`
Usos de ejemplo: local con apartamentos arriba, restaurante, oficinas/consultorios, terraza como lounge, y un concepto de obra nueva (rotulado "Concepto ilustrativo").
