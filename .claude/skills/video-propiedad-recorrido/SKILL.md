---
name: video-propiedad-recorrido
description: Idea "Puertas abiertas / Ven a verla" de una propiedad captada para provocar la visita. Genera 3 guiones (un solo plano, la terraza que no te esperas, padre e hijo abren la puerta), prompts de Higgsfield mínimos y lista de tomas. Úsalo cuando Eduardo pida recorrido, tour, invitación a visitar o el video emocional con Luis León.
---

# Idea 3 · "Puertas abiertas" (ven a verla)

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
Abrir la puerta: el espectador entra con Eduardo (y Luis León en la versión emotiva), sube y termina en la mejor vista. Es la visita comprimida y filmada como cine.
La transparencia (mostrar los acabados como están) genera confianza y filtra curiosos. La versión padre e hijo es la historia central de la marca: **legado y nueva generación**.

## Material que se necesita
Fachada y porche/entrada, recorrido interior en orden (planta baja, escalera, cuartos, balcón), terraza o mejor vista, y tomas por grabar: recorrido en una toma con gimbal, hora dorada en la mejor vista, Eduardo a cámara.
Vigilar la exposición en la transición interior oscuro → exterior claro (es la mejor escena).

## Los 3 guiones
- **A · "Un solo plano" (≈60 s):** esquina → fachada → entrada → salón → escalera → terraza con revelación → Eduardo con datos y precio → "agenda tu visita". Si no hay toma continua, cortes escondidos (puerta, pilar, columna).
- **B · "La terraza que no te esperas" (≈28 s):** empieza por la vista (gancho), rebobinado hasta la calle, recorrido rápido y vuelta a la vista en bucle.
- **C · "Legado: padre e hijo abren la puerta" (≈55 s):** Luis León abre la puerta ("más de cuarenta años abriendo puertas"), Eduardo muestra la nueva visión, terraza al atardecer, cierre con frase de marca (hay propuestas; no usar "Legado y visión" tal cual). Natural, no memorizado.

## Cinematografía
Gimbal, gran angular sin acercarse a los muros, luz natural, color con negro profundo y acentos azul/rojo; música creciente; silencio de 2–3 s en la revelación.

## Prompts de Higgsfield (mínimos; la IA solo pule lo real)
- Estabilizar/suavizar: `Gentle stabilization and slow forward motion, keep the exact interior, curtains and stairs from the reference, natural daylight, no new objects.`
- Vista con luz dorada: `Slow cinematic push-in on the terrace, warm golden hour light on the mountains, keep the layout, roof and background identical to the reference, no people.`
- Fachada final: `Slow gentle push-in on the facade at golden hour, keep the building, bars, cables and street identical to the reference.`
- `upscale_video` si hace falta (consultar costo). No generar espacios que no se grabaron.
