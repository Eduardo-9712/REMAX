# MercadoLibre: cómo pedir ayuda a soporte de Developers

## Por dónde se envía

Según la documentación oficial ("Soporte para integradores"), el soporte de Developers funciona con
**tickets** desde el portal de desarrolladores, no por correo suelto. Pasos:

1. Entrar al portal de desarrolladores de MercadoLibre con la cuenta de Eduardo.
2. Abrir **Soporte** y crear un ticket.
3. Elegir categoría **Inmuebles** y la subcategoría que más se parezca.
4. Si pide una aplicación y no se pudo crear, dejarlo en blanco o escribir que la creación falló.
5. Tipo: **Problema**. Pegar el texto de abajo en la descripción (hasta 5.000 caracteres) y adjuntar o describir
   la captura del error.
6. Enviar. Llega un correo con un enlace "View request" y las respuestas se pueden dar desde el correo o el portal.

Atención personalizada: lunes a viernes, 9:00 a 18:00 (hora de Argentina, GMT-3). Antes responde un bot 24/7.
Si el portal no deja crear el ticket sin una aplicación, que Eduardo use el chat o ayuda general de MercadoLibre
y mencione el código del error. Eso no se puede enviar desde esta sesión.

## Texto sugerido

Asunto: Error PSC01-RBJAGGUMCM3C al crear una aplicación (inmuebles, Venezuela)

Hola, equipo de Developers de MercadoLibre.

Soy asesor inmobiliario de RE/MAX en Venezuela (Guarenas, Guatire y Costas Mirandinas). Al intentar crear una
aplicación en el portal de desarrolladores me aparece el error **PSC01-RBJAGGUMCM3C** y no puedo continuar.

Quiero usar la API para consultar, de forma permitida, las publicaciones de inmuebles de MercadoLibre Venezuela
(MLV) en esas zonas y llevar un análisis de mercado interno. No voy a publicar ni modificar anuncios ni a revender
los datos.

Les agradezco que me indiquen:
1. Qué significa el error y cómo corregirlo.
2. Si una aplicación de solo lectura puede consultar publicaciones de inmuebles de otros vendedores, y bajo qué
   condiciones.
3. Los límites de uso (rate limit) que aplicarían.

Usuario de MercadoLibre: _(Eduardo lo completa)_
Correo: _(Eduardo lo completa)_

Gracias.
Eduardo León, RE/MAX

## Mientras responden

- Usar el cuadro **Pegar el anuncio** de la pestaña Propiedades de la base maestra.
- Una lista de enlaces de MercadoLibre no sirve para que Claude los lea: MercadoLibre devolvió un bloqueo (error 403)
  al intentar abrir un listado. Por eso la opción es pegar el texto de cada anuncio.
