---
name: video-propiedad-maestro
description: Skill maestro para cualquier video de transformación o remodelación con IA de una propiedad (restaurante, concesionario, coworking, spa, etc.): regla de obra con obreros acelerada a 2×, fidelidad a la estructura, flujo por etapas, costos reales de Higgsfield y control de calidad. Úsalo SIEMPRE que se planee o genere una remodelación, transición de obra o antes/después de una propiedad, junto con el skill de la idea concreta.
---

# Skill maestro: transformaciones y remodelaciones con IA

Responde en español, tono de amigo, a Eduardo. Reglas del CLAUDE.md: **no inventar datos**, **respetar la estructura del inmueble**, **no gastar créditos sin el «dale» de Eduardo por etapa**, solo material de la propiedad y voz en off de Eduardo (salvo la idea del delivery). Los prompts completos están en `contenido/calle-miranda-51/ideas-eduardo/prompts-maestros.md` y la guía de modelos y costos en `higgsfield-calidad.md`.

## REGLA MAESTRA DE REMODELACIÓN (decidida por Eduardo el 05-10-2026; aplica a TODAS las remodelaciones)
1. **Se genera LARGO y se publica a 2×:** fachada **10 s → 5 s**; interiores **5 s → 2,5 s** (más dramático: 1,5×). Se acelera en la edición (CapCut: flujo óptico/mezcla de cuadros y desenfoque de movimiento).
2. **Obreros visibles:** 3–4 en la fachada y 2 por interior, con **casco, chaleco reflectivo y overol**, en plano medio o general, **de espaldas o de perfil, sin rostros nítidos**, sin logos ni texto; trabajan de verdad (pintan, instalan vidrios y puertas, sueldan con chispas, arman andamio, cargan materiales, colocan plantas). Son ficción de IA, genéricos.
3. **Secuencia:** desmontan lo anterior → andamio con **malla verde de seguridad** → trabajos → retiran la malla → remates (plantas y luces) → **reveal** con barrido de luz.
4. **Estructura intacta:** no se cambia el volumen ni la distribución; solo acabados, vidrio, mobiliario, luz y función. Eduardo permite ser **creativo** (estacionamiento, plantas, luces, detalles premium) siempre **acorde a la estructura**.
5. **Cámara fija (trípode)** para que inicio y final calcen. **Sonido en edición** (martillo, taladro, soldadura, radio de obra, *whoosh* al revelar).
6. **Rótulo siempre:** "Recreación con IA · No es un proyecto aprobado" (y "Imagen ilustrativa con IA" en aéreas y caída).

## Flujo de trabajo (siempre por etapas)
1. **Preparar** las fotos: recorte 9:16 + una referencia despejada. Cotizar con `get_cost:true` (no gasta).
2. **Renders** (Nano Banana Pro 4K, 4 créditos c/u): 1 variante; 2 solo si hace falta comparar.
3. **Transiciones** (Kling v3.0 pro): **fachada 10 s = 17,5 créditos; interior 5 s = 8,75**. Primero **una sola cadena de prueba** y se la muestra a Eduardo.
4. **Revisar cuadro por cuadro** contra la foto real (niveles, terraza/techo, ventanas, puertas, vecinos). Máximo **un reintento** por pieza sin consultar; si se pasa del presupuesto dicho, avisar.
5. **Entregar** a Eduardo: antes/después, tablero de fotogramas y el video, con el **gasto exacto** y el saldo (`balance`).
6. Guardar resultados y aprendizajes en `contenido/<propiedad>/prueba-higgsfield/` y actualizar los prompts maestros.

## Control de calidad
Rechazar si cambia la estructura, hay letras/logos/placas/rostros nítidos, algo se derrite o parpadea, o el andamio tapa la terraza más de un instante. Avisar siempre de lo que la IA cambió fuera de lo pedido (p. ej. quitó cables o agregó banqueta).

## Más ideas para elevar el video
Ver `mejoras-espectaculares.md` (camión y materiales, chispas, letrero en blanco, reveal con inauguración, plano animado con el croquis, sound design por rubro, 4 mini-reels de una sola cadena).
