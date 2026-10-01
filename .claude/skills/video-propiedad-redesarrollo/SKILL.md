---
name: video-propiedad-redesarrollo
description: Reel "¿Qué harías con estos m²?" de una propiedad captada: muestra con IA cómo podría reconvertirse o redesarrollarse (restaurante, oficinas, local). Úsalo cuando Eduardo pida el video de reconversión, redesarrollo o potencial de una propiedad.
---

# Video "¿Qué harías con estos m²?" (redesarrollo)

Responde en español, tono de amigo, a Eduardo. Reglas del CLAUDE.md: no inventar datos (todo lo no confirmado va como "por confirmar"), no gastar créditos de Higgsfield sin el visto bueno de Eduardo (antes: `balance` y `models_explore`, proponer el costo total y esperar el "dale"), y no mostrar nunca nombre ni documentos de la propietaria. Primero lee `contenido/<propiedad>/material.md` y, si es una propiedad nueva, usa el skill `video-propiedad` para leer la carpeta de Drive.

## Qué es
Reel 9:16 de 30–40 s que enseña el **potencial**: foto real "hoy" → recreaciones con IA "mañana" → terraza/vista real → precio y llamado.
Ejemplo ya armado: `contenido/calle-miranda-51/ideas-video.md`, Idea 2.

## Reglas especiales (este video sí inventa imágenes, por eso)
- Toda imagen generada lleva el rótulo visible **"Recreación con IA, no es un proyecto aprobado"**.
- Nunca presentarlas como obra existente, como proyecto aprobado ni como algo que "se puede" hacer sin permisos.
- Los usos mostrados deben tener sentido para la zona; si hay duda sobre el uso permitido, decir "sujeto a permisos y factibilidad" y no afirmar.
- La estructura, ventanas, techo y proporciones de la foto real se **conservan** en el prompt; solo cambia el mobiliario, la iluminación y la función.

## Pasos
1. Elegir 2 o 3 fotos reales con buen ángulo (salón, fachada, planta).
2. Para cada uso (restaurante, oficinas, local, otro que pida Eduardo): prompt de `generate_image` en inglés que parta de la foto, con "keep the ceiling, columns, windows and floor unchanged; same camera angle; photorealistic". Mostrar los prompts y esperar el "dale" antes de generar.
3. Animar cada imagen con un movimiento corto (push-in, brillo de luz) en un segundo paso de video.
4. Guion (tabla tiempo | imagen | voz): hoy → mañana (x3) → terraza real → datos (m², precio, uso verificable) → "ven a verla y dime qué ves tú".
5. Nota de pie con la fuente de las superficies y la advertencia de permisos.
6. Guardar en `contenido/<propiedad>/`.
