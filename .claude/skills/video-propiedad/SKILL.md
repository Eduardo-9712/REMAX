---
name: video-propiedad
description: Convierte una propiedad captada (carpeta de Drive con fotos, videos y ficha) en guion de reel, prompts de Higgsfield y lista de lo que falta. Úsalo cuando Eduardo pase el enlace de una propiedad nueva o pida un video/guion de una propiedad.
---

# Video de una propiedad captada

Responde en español, tono de amigo, a Eduardo. Sigue las reglas del CLAUDE.md: **no inventar datos** (precio, metros,
cuartos, usos → "por confirmar"), y **no gastar créditos de Higgsfield sin el visto bueno**.

## 1. Leer la carpeta de Drive

- Los conectores de Drive pueden fallar con "Insufficient scope". Si la carpeta es pública, funciona esto:
  1. `curl -L "https://drive.google.com/drive/folders/<ID>"` y sacar de la tabla HTML (`<tr data-selectable data-id="...">`) el id, nombre y tamaño.
  2. Descargar con `https://drive.google.com/uc?export=download&id=<ID>`. Los archivos grandes devuelven una página de
     aviso: leer su `action` y campos ocultos (`id`, `confirm`, `uuid`) y pedir `drive.usercontent.google.com/download?...`.
  3. Las fotos son HEIC: `pip install pillow-heif` (ImageMagick no las abre). Videos: `ffmpeg` para sacar un fotograma central.
  4. Armar hojas de contacto y **mirar todo** antes de escribir.
- Trabajar en el directorio temporal (scratchpad), **no** meter fotos ni videos en el repositorio.
- **Privacidad:** no descargar ni abrir cédulas, documentos de identidad ni escrituras. Si se ven en la carpeta
  compartida, avisar a Eduardo que los saque (el enlace es público). Nunca usar el nombre de la propietaria.

## 2. Datos

Leer la ficha técnica (.docx: `unzip` y sacar `word/document.xml`). Tabla con: dirección, terreno, construcción
(indicar fuente y fecha del catastro), uso, precio, cuartos/baños, enlace del anuncio. Lo que no esté → **por confirmar**.
Anotar lo que **falta verificar** (uso comercial, registro, estacionamiento, etc.).

## 3. Revisar el material

Listar qué muestra cada archivo (salón, terraza, vistas…), cuáles son las mejores tomas y **qué falta** (casi siempre:
fachada, calle, entorno, precio, permiso de la propietaria).

## 4. Guion

Reel vertical 9:16 de 35–45 s con tabla: tiempo | imagen (archivo) | voz/texto. Estructura: gancho (la mejor toma) →
dato fuerte → recorrido → posibilidades → respaldo (Luis León: broker + Consultor Jurídico de la Cámara Inmobiliaria
de Miranda) → llamado a WhatsApp. Estética negra con acentos azul y rojo RE/MAX, música afrobeat/emotiva.
Incluir "no decir hasta confirmar" y la nota de pie con la fuente de las superficies.
Oficina en los logos: Aventura hasta el cambio a Delta (fines de octubre de 2026).

## 5. Prompts de Higgsfield

Un prompt en inglés por toma, **image-to-video** con la foto real de referencia: movimiento de cámara suave y luz, y
la frase "keep the exact architecture from the reference, no new objects". La IA anima lo real; no inventa
acabados, cuartos ni vistas. Textos y datos se ponen en edición.
Antes de generar: `balance` y `models_explore` para el costo; proponer el total y esperar el "dale".

## 6. Entregables

Guardar en `contenido/<propiedad>/`: `material.md` (datos, lo que se ve, lo que falta, privacidad) y
`ideas-video.md` (3 ideas, cada una con su skill: `video-propiedad-punto`, `video-propiedad-redesarrollo`, `video-propiedad-recorrido`). Commit claro en español. Cerrar con las preguntas que Eduardo debe responder.
