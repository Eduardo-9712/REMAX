---
name: video-propiedad-caida
description: Idea "Caída y transformación": caída desde el espacio hasta la propiedad, paneo 360 al atardecer y antes/después con obra visible en 4 rubros (restaurante gastronómico, concesionario de motos, coworking + estudio de fotografía y video, spa), fachada y luego interior de cada rubro, con voz en off. Úsalo cuando Eduardo pida un video viral de potencial, caída del cielo o transformaciones con IA.
---

# Idea 2 · "Caída del cielo y transformación"

## Reglas fijas (CLAUDE.md)
- Español, tono de amigo con Eduardo. Eres experto en guiones, cine, marketing digital y profesional inmobiliario.
- **No inventar datos**: lo no confirmado va como "por confirmar" o no se dice (aforo, flujo de gente, rentabilidad, estacionamiento, cuartos/baños, distribución de los niveles).
- **No gastar créditos de Higgsfield sin el visto bueno**: antes `balance` y `models_explore`, decir el costo total y esperar el "dale". Usar `ideas-eduardo/higgsfield-calidad.md` (modelos, bloques de fidelidad y calidad, control de calidad).
- **IA ahora, dron real después**: los guiones y la voz en off no cambian; solo se reemplazan los clips de IA por los reales.
- **La IA mejora el grado, pero NO cambia la esencia ni la estructura de la casa** (niveles, frente angosto, terraza con techo verde, ventanas, rejas, porche, vecinos). En transformaciones cambian acabados, fachada comercial, mobiliario y función.
- Solo **material de la propiedad** y **solo la voz en off de Eduardo**, salvo la idea del delivery (que él graba). Eduardo graba la voz; entregar textos listos para leer, ~2,5 palabras por segundo.
- Cada toma marcada **REAL** o **IA**. Rótulos: **"Recreación con IA · No es un proyecto aprobado"** (transformaciones) o **"Imagen ilustrativa con IA"** (aéreas y caída). "Podría", nunca "se puede"; "sujeto a permisos y factibilidad".
- Precio **USD 120.000 visible** (decisión de Eduardo). Luis León: Broker de RE/MAX Delta primero, luego Consultor Jurídico de la Cámara Inmobiliaria de Miranda. Logo: Aventura hasta el cambio a Delta (fines de oct 2026).
- No usar clips ya editados con logo (p. ej. `copy_7183…`); pedir los originales. Difuminar rostros y placas; nada de la propietaria.
- Leer en `material.md` la **ruta real de la casa** (confirmada por Eduardo) y seguirla **siempre en el mismo orden** en cualquier recorrido interior. En cadenas de transformación: fachada → interior → fachada.
- Entregar: guion principal (tabla Tiempo | Plano y cámara | Voz en off | Texto en pantalla | Origen y archivo) + 2 variantes, prompts sin ejecutar, qué se necesita, caption y hashtags. Guardar en `contenido/<propiedad>/ideas-eduardo/`. Ejemplo completo: `contenido/calle-miranda-51/ideas-eduardo/`.

## Estructura (≈130 s; cortes de 60 s y de 30 s): CADENA
Caída del espacio (opcional, 7 s) → **calle y alrededores caminando y en 360** → llegada y paneo 360 exterior al atardecer → HOY (real, frío) → **cadena de rubros, uno a la vez**:
`FACHADA se reconstruye al rubro (se quita lo del rubro anterior) → INTERIOR en 5 tomas de 3 s siguiendo la ruta real de la casa (obra → reveal) → vuelve a la FACHADA y monta el siguiente` → cierre en lo real (patio, terraza, fachada sin carro, precio).
Rubros decididos por Eduardo, en este orden: **restaurante gastronómico** (cocina de madera, gran salón, patio, terraza), **concesionario de motos** (estacionamiento y porche, gran salón, patio, fondo; se ven muchas motos en la calle, sin afirmar demanda), **coworking + estudio de fotografía y video** (juntos), **spa** (cuartos, baños, patio, terraza).
La misma **ruta real y el mismo patrón** se usan en los recorridos de las otras ideas. La ruta está en `material.md`.

## Proceso con Higgsfield
1) Renders del "después" desde la foto real (Nano Banana Pro 4K; comparar con FLUX 3): 4 fachadas + 5 espacios por rubro. 2) Transiciones en cadena (Seedance 2.5, imagen inicial = rubro anterior, final = rubro siguiente; borrador 480p antes del final). **Probar primero una sola cadena** (restaurante) y mostrarla. 3) Caída y paneo (Veo 3.1 ultra). Mostrar prompts y esperar el "dale". Comparar cada render con la foto real antes de animar.
Sin marcas, letras ni personas legibles; en la obra solo materiales y andamios.
