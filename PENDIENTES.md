# Documento maestro: dónde estamos y qué falta

Actualizado: 29-09-2026 (de noche). Aquí está todo en un solo lugar para no tener que buscar en las conversaciones:
lo que ya tenemos, lo que hice mientras dormías y lo que falta. Eso incluye tus respuestas, lo que me tienes que
mandar, lo que le pedimos a Alejandra y lo que le preguntamos a tu papá.
Cuando algo se resuelva, se marca con [x] y yo lo paso a donde corresponda.

**Cómo usarlo mañana:** contesta las secciones **1** y **7** como te salga (texto o nota de voz, en desorden sirve),
mándame lo de la sección **2** y yo sigo desde ahí.

---

## Lo que ya tenemos

| Pieza | Estado | Dónde |
|---|---|---|
| **Base maestra** (Análisis Comparativo Maestro) | ~378 propiedades de RE/MAX, Century 21, ZonaVen, BienesOnline y Admyser. Se actualiza sola cada lunes. Cada ficha trae precio, m², USD/m², veredicto de precio, fuente, enlace, notas, **contacto del anunciante** y **valor estimado por el equipo** | https://claude.ai/artifact/JnuELprRV41EFNRx6xXr46 |
| **Cierres reales de Delta** | **101 cierres** (2025 y enero–agosto de 2026). La pestaña Cierres muestra la evolución por año y zona, la rebaja real, los días para vender y los sectores donde más se vende. 14 marcados ⚠ | Pestaña Cierres · `analisis/cierres-delta.md` |
| **Documentos de la oficina** | Autorización de venta con y sin exclusividad, autorización de alquiler (modelo de Aventura), carta de recaudos y mensaje de recaudos para WhatsApp | `documentos/` |
| **Kira** (asistente de WhatsApp, nombre interno) | Copiloto mejorado (ver abajo). 1 cliente guardado (Idania). **16 fichas de conocimiento por aprobar** | Pestañas Copiloto, Clientes y Conocimiento · `whatsapp/` |
| **Casa de la Calle Miranda N.º 51** | Material revisado completo (62 videos, 68 fotos, plano y documentos). **3 propuestas de campaña** y prompts de Higgsfield en borrador. Nada producido todavía | `contenido/casa-calle-miranda.md` |
| **Proceso de videos con Higgsfield** | Borrador del "skill": el paso a paso para cada propiedad | `contenido/higgsfield/proceso-video-propiedad.md` |
| **Reels** | 3 guiones de reel a medio escribir y la estructura de tu video del curso de la Cámara | `contenido/reels.md` |
| **Rutinas automáticas** | Lunes 5:55 a. m.: actualiza la base. Lunes 6:53 a. m.: busca noticias para Kira. La de *Estudio de Mercado* quedó **apagada** | — |
| **Pull request** | Todo lo de estos días está en [Eduardo-9712/REMAX#6](https://github.com/Eduardo-9712/REMAX/pull/6): falta aprobarlo para pasarlo a main | GitHub |

### Lo que dicen los cierres (ventas de RE/MAX Delta)

| | 2025 | 2026 (enero–agosto) |
|---|---|---|
| Ventas cerradas | 46 | 35 |
| Precio de cierre típico | USD 21.500 | USD 32.000 |
| Rebaja típica sobre el precio publicado | 4,6 % | **0 %** |
| Vendidas sin rebaja | 17 de 42 | 16 de 31 |
| Días típicos desde que sale al mercado hasta el cierre | 75 | **57** |

Falta el USD/m² de cierre: el Excel no trae los metros (se los pedimos a Alejandra).

---

## Lo que hice mientras dormías

1. **Kira (copiloto de WhatsApp) mejorada** y publicada en la base:
   - Ahora **decide la etapa del chat**: calificar, enviar opciones, agendar visita, seguimiento o pasar a Eduardo.
     Cuando toca **enviar opciones**, agrega sola las 3 mejores propiedades de la base, con precio y enlace.
   - **Sigue tu trato**: si le hablas de usted, ella también.
   - **Te avisa en amarillo** si la respuesta trae más de una pregunta.
   - Casilla nueva **"Lo que dije en audios o llamadas"**, para que no pregunte lo que ya hablaste por nota de voz.
   - Campo **"¿De dónde vino?"** (oficina, Instagram, TikTok, portal, referido…), que se guarda en Clientes.
   - Si el cliente acepta varios tipos ("apto o casa"), busca en todos esos tipos y no mete otros.
2. **5 fichas nuevas de conocimiento para Kira**, todas *por aprobar* y hechas con lo que dicen tus contratos. Lo
   que no está confirmado va marcado **POR CONFIRMAR**:
   - Formas de pago (bolívares o dólares).
   - Proceso de compra paso a paso.
   - Quién paga qué.
   - Visitas.
   - **Plantillas de mensajes:** bienvenida, envío de opciones, seguimiento a las 24 y 72 horas, después de la visita y
     cliente que lo va a pensar.
3. **Casa de la Calle Miranda:** revisé todo el material y armé **3 propuestas de campaña**:
   - **A. "El Punto"**, para el comerciante y el inversionista. Es la que recomiendo como principal.
   - **B. "Guatire desde arriba"**, con la emoción y la ciudad desde la terraza.
   - **C. "Los números del centro"**, educativa y con datos.
   Cada una trae piezas, carrusel, contenido educativo y **7 prompts de Higgsfield en borrador**. También dejé el
   mapa de qué archivo de tu Drive muestra cada espacio.
4. **Borrador del proceso ("skill") de videos con Higgsfield** para usarlo con cada propiedad nueva.
5. **No toqué Higgsfield** ni gasté créditos.

---

## 1. Preguntas para ti, Eduardo (generales)

- [x] **Dos bases haciendo lo mismo:** nos quedamos con la base maestra; *Estudio de Mercado* quedó apagada.
- [x] **Nombre del asistente:** Kira, solo interno. Con los clientes es "el equipo de Eduardo León".
- [x] **Guardar en main:** el pull request ya está abierto.
- [ ] **1. Cómo te presentas en los mensajes.** Hoy dice "Eduardo León de RE/MAX". ¿Pongo "RE/MAX Delta" desde ya
  o esperamos al cambio de fines de octubre?
- [ ] **2. Captaciones de octubre.** Las que hagas antes del cambio, ¿van por Aventura o ya por Delta?
- [ ] **3. Zona de 8 urbanizaciones de los cierres:** Parque Alto, Vicente Emilio Sojo, Altos de Copacabana,
  Altos de Izcaragua, Canaima II, Canaima IV, Buena Vista y Hacienda Sojo. ¿Guatire o Guarenas?
- [ ] **4. Alquileres de los portales.** ¿Son mensuales en USD?
- [ ] **5. Margen de "precio justo".** Hoy es así: **Oportunidad** a −15 % o menos, **En mercado** hasta +10 %,
  **Por encima** hasta +25 % y **Sobreprecio** por encima de eso. ¿Lo dejamos así?
- [ ] **6. Costas Mirandinas.** Hoy cuento Brión, Páez, Pedro Gual, Andrés Bello y Buroz. ¿Sumamos Acevedo u otro?
- [ ] **7. Sectores con dos nombres** (por ejemplo "Castillejo" y "El Castillejo"). ¿Cuáles son el mismo?
- [ ] **8. Pull request #6:** revísalo y apruébalo en GitHub cuando puedas.

## 2. Lo que me tienes que mandar

- [x] Material de la casa de la Calle Miranda (carpeta de Drive).
- [ ] **Videos y fotos de Las Cuatro Esquinas y de los alrededores** de la casa (no estaban en la carpeta).
- [ ] **Tus respuestas a la sección 7** (la campaña y los videos de la casa).
- [ ] **Tus ideas de videos** para Higgsfield, como te salgan.
- [ ] **Tus videos ya grabados:** el del tema que tenías y el de tu paso por el curso de la Cámara.
- [ ] **Excel de productividad 2024**, si existe con la hoja de ventas.
- [ ] **Autorización de alquiler de Delta** y, si existe, la de alquiler sin exclusividad.
- [ ] **La "hoja de recaudos"** que menciona la carta de solicitud de documentos.
- [ ] **La cartera de terrenos y galpones de tu papá** (lista o fotos).
- [ ] **2 o 3 conversaciones más de WhatsApp** para Kira, y **guárdalas en Clientes** después de analizarlas.
  De las 3 que probaste, solo quedó guardada la de Idania.

## 3. Lo que te toca hacer

- [ ] **Mover las cédulas y el título de propiedad** de la carpeta de Drive de la casa a una carpeta privada. Hoy la
  carpeta está abierta a cualquiera con el enlace.
- [ ] **Corregir el anuncio de RE/MAX** de la casa: dice "Terreno: 419,86 m²", pero el terreno es de **295,41 m²** y
  la construcción, de 419,86 m².
- [ ] Revisar y aprobar (o pasarle a tu papá) las **16 fichas de Conocimiento**. Sin eso, Kira solo pregunta.
- [ ] Probar Kira con las mejoras nuevas: la casilla de audios, el origen y las etapas.
- [ ] Compartir la base con **Alejandra** como **Colaborador**.
- [ ] Revisar el **banco de preguntas** de Kira (`whatsapp/agente-diseno.md`, sección 9).
- [ ] Recordarle a tu papá que suba sus **terrenos y galpones** a la plataforma de RE/MAX.
- [ ] MercadoLibre sigue bloqueado: agregar a mano lo que valga la pena.

## 4. Para Alejandra

Todo se hace en la pestaña **Cierres** de la base: filtro "Solo por revisar" → **Editar**.

- [ ] **Los m² (construcción y terreno) de los 101 cierres.** Es lo más importante. Salen de NOVUS con el código de
  oficina o de los expedientes.
- [ ] **La forma de pago de cada cierre** (contado, crédito, Venezuela Renace, permuta).
- [ ] **Fechas exactas de cierre** de La Esperanza (Castillejo, USD 100.000) y de El Torreón (USD 65.000).
- [ ] **Apartamento de La Sabana (El Marqués), USD 42.000,** reservado el 08-09-2026: ¿se cerró? ¿En cuánto y cuándo?
- [ ] **Los 14 cierres con ⚠:**
  - La Sabana, obra gris (2025): ¿16.500 o 1.000?
  - Frigorífico Super Carne (2025): ¿37.000 o 5.450?
  - Galpón de Las Flores: ¿USD 9.563 es el canon mensual?
  - Canaima II: se reservó en 28.000 y se vendió en 27.000.
  - Terreno de Calle Zamora: se reservó en 46.000 y se vendió en 50.000.
  - Ciudad Casarapa, parcela 6: los precios de los dos apartamentos están cruzados.
  - Parque Habitat El Ingenio y Los Cardenales (2025): se reservaron en 14.800 y se vendieron en 14.000.
  - Canaima IV: la captación tiene fecha posterior a la reserva.
  - C.C. Vista Place, Los Cardenales (2026) y el galpón de Cloris: confirmar las fechas (ya pasados a 2026).
- [ ] **Códigos repetidos:** 0156-0796 (Canaima II y Las Rosas) y 0156-0770 (La Sabana y Ciudad Casarapa).
- [ ] **TH de Costa Grande (Higuerote):** aparece vendido en mayo y en noviembre de 2025. ¿Son dos distintos?
- [ ] **Parque Habitat B:** ¿casa o TH?
- [ ] **Precio publicado de 11 cierres** que no lo tienen (casi todos por alianza).
- [ ] **Confirmar propiedades de la base**, empezando por las de Delta.

## 5. Para Luis León

Las preguntas de fondo están en `analisis/preguntas-luis-leon.md`: regla de inversión, precios por zona, sectores,
terrenos y galpones, lo legal y el mercado. Además:

- [ ] **Comisión mínima de USD 1.000** en ventas: ¿la ponemos por escrito?
- [ ] **Comisión de alquiler:** ¿es uno o dos cánones (uno por cada parte)?
- [ ] **Depósito en garantía:** el tope es 5 % *con* IVA y los honorarios son 5 % *más* IVA. ¿La diferencia se cobra aparte?
- [ ] **Correcciones de los contratos:** dos cláusulas con el número 6, "SUDEBAM" en vez de SUDEBAN, y faltan
  espacios para apoderado, varios dueños, empresa y extranjeros (`documentos/README.md`).
- [ ] **Recaudos extra** cuando el propietario es una empresa, vive en el exterior o son varios dueños.
- [ ] **Aprobar o corregir las 16 fichas de Kira.** Sobre todo:
  - Formas de pago en bolívares.
  - Proceso de compra y tiempos.
  - Quién paga los gastos de registro.
  - Venezuela Renace.
- [ ] **Casa de la Calle Miranda:** ¿cómo se explica el **uso conforme** para ponerle un negocio a una casa de uso
  residencial? Sería su episodio de "Pregúntale al Broker" para esta campaña.
- [ ] **Subir sus terrenos y galpones** a la plataforma de RE/MAX.
- [ ] **Grabar "Pregúntale al Broker",** episodio 1 (`contenido/reels.md`).

## 6. Kira (WhatsApp): qué falta para seguir

**Fase 2, probar con el copiloto (ahora):**
1. Aprobar las fichas de conocimiento.
2. Probar con las mejoras nuevas y guardar cada cliente.
3. Mandarme las respuestas que no te gusten, con lo que tú hubieras escrito.

**Fase 3, conectarla a WhatsApp:**
1. Cuenta de **Meta Business** verificada.
2. **Proveedor** de la API con coexistencia que funcione en Venezuela (yo comparo opciones cuando me digas).
3. Cuenta en la **consola de Anthropic** con un límite de gasto.
4. Tu **WhatsApp personal** para las fichas.
5. Cómo lee el servidor la base: una copia semanal que publique la rutina.

Más detalle: `whatsapp/plan-agente.md` y `whatsapp/revision-copiloto.md`.

## 7. Casa de la Calle Miranda: preguntas para la campaña y los videos

Las 3 propuestas y los prompts están en `contenido/casa-calle-miranda.md`.

**La propiedad y la dueña**
- [ ] 1. ¿La dueña firma ella misma, o hay apoderado o herederos?
- [ ] 2. ¿El piso de arriba (el salón con techo de madera y la terraza) está incluido en los 419,86 m² del catastro,
  o se construyó después? ¿Dónde queda ese salón? No sale en el plano.
- [ ] 3. ¿Los USD 120.000 son fijos? ¿Cuánto margen hay para negociar?
- [ ] 4. ¿La autorización es exclusiva? ¿Cuándo vence? ¿Pasa contigo a Delta?
- [ ] 5. ¿Tiene todas las solvencias al día y ningún gravamen hoy?
- [ ] 6. ¿La dueña está de acuerdo con venderla como "activo para reconvertir"?
- [ ] 7. ¿Está vacía? ¿Qué horarios hay para visitas?
- [ ] 8. ¿Sabes algo de filtraciones, del estado de la estructura, de la luz trifásica o del agua?

**La campaña**
- [ ] 9. ¿Cuál es la meta: cuántos contactos o visitas, y en cuánto tiempo?
- [ ] 10. ¿Vas a pagar publicidad? ¿Con cuánto presupuesto?
- [ ] 11. ¿Por qué canales: Instagram, TikTok, estados, grupos, portales, la cartera de tu papá?
- [ ] 12. ¿A quién le hablamos primero: comerciante, médico, restaurante, inversionista o familia?
- [ ] 13. ¿Sale tu papá en algún video?
- [ ] 14. ¿La marca es Aventura ahora o esperamos a Delta?
- [ ] 15. ¿A qué número de WhatsApp llegan los contactos?
- [ ] 16. El video que editaste el 19 de agosto: ¿lo publicaste? ¿Cómo le fue? ¿Reusamos tu voz?
- [ ] 17. **¿Cuál de las 3 propuestas te gusta (A, B, C) o qué mezcla?**

**Los videos en Higgsfield**
- [ ] 18. Tus ideas de videos.
- [ ] 19. "Los skills de los videos": ¿es el proceso guardado y reutilizable para cada propiedad? (el borrador está
  en `contenido/higgsfield/proceso-video-propiedad.md`)
- [ ] 20. ¿Qué estilo quieres?
  - Cinematográfico con tu material.
  - Antes y después (con la etiqueta "Imagen ilustrativa").
  - Con tu cara o un avatar.
  - Con tu voz real o generada.
- [ ] 21. ¿Cuántos créditos quieres gastar? ¿Reviso tu saldo cuando me des luz verde?
- [ ] 22. ¿Qué formatos? Por ejemplo: 1 video principal de 30–45 s, cortos de 10–15 s e historias.

**Tomas que faltan**
- [ ] 23. Las Cuatro Esquinas y los alrededores (me los mandas mañana).
- [ ] 24. **1 minuto grabando frente a la casa en hora pico**, para contar la gente y los carros que pasan.
- [ ] 25. Tomas contigo en cuadro (caminando, abriendo el portón, subiendo) y un **atardecer desde la terraza**.
