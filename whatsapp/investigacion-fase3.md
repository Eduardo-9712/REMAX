# Investigación para la Fase 3 (1 de octubre de 2026)

Qué encontré en la web y qué **no pude confirmar**. Lo que dice "por confirmar" se le pregunta al
proveedor antes de pagar nada.

## 1. Proveedor de WhatsApp con coexistencia

**Qué es la coexistencia:** el mismo número funciona a la vez en la app WhatsApp Business de Eduardo y en
la API. Lo que se escribe de un lado se refleja en el otro, y el historial se sincroniza.
([Whautomate](https://whautomate.com/whatsapp-coexistence), [Chakra](https://chakrahq.com/article/whatsapp-coexistence-business-app-register-cloud-api/amp/))

**Lo que encontré:**
- Según las guías de proveedores, la coexistencia ya está disponible en todos los países (a junio de 2026).
  Pide la app Business versión 2.24.17 o más nueva y que el número tenga actividad previa (se menciona 7+ días).
  Son fuentes de los propios proveedores: **por confirmar** con Meta/proveedor para Venezuela (+58).
- Los mensajes que Eduardo escribe desde su app le llegan al servidor como un aviso aparte (`smb_message_echoes`).
  Eso es lo que permite que **el asistente se calle cuando Eduardo entra al chat**.
  ([360dialog](https://docs.360dialog.com/docs/resources/phone-numbers/coexistence), [Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/))
- Límite: con coexistencia, el número queda limitado a unos 20 mensajes por segundo en total. Sobra para nosotros.

**Candidatos y costos (de las propias páginas de los proveedores, sin verificar):**

| Proveedor | Costo de la plataforma | Sobreprecio por mensaje | Nota |
|---|---|---|---|
| 360dialog | desde ~US$59/mes por número | No cobra sobreprecio | Pensado para conectar un servidor propio. Mejor candidato. |
| Dualhook | por confirmar | por confirmar | Se anuncia como opción económica de coexistencia. |
| Twilio | sin cuota fija conocida | ~US$0,005 por mensaje | Muy conocido; sale más caro con volumen. |
| WATI | desde ~US$25/mes (plan en rupias, por confirmar) | ~20 % sobre Meta | Trae panel propio, pero es más cerrado para un servidor propio. |

Fuentes: [360dialog](https://360dialog.com/blog/whatsapp-business-api-pricing-why-markup-on-messages-often-costs-you-more/),
[Dualhook](https://dualhook.com/best-whatsapp-coexistence-providers), [Sleekflow](https://sleekflow.io/en-us/blog/best-whatsapp-api-providers).

**Lo que Meta cobra (aparte del proveedor):** desde el 1-jul-2025 se cobra por mensaje de plantilla, según
categoría y país. **Las respuestas libres dentro de las 24 horas desde que el cliente escribe son gratis.**
Como nuestro asistente solo responde dentro de esa ventana, su costo de Meta debería ser prácticamente cero;
los seguimientos fuera de ventana los hace Eduardo desde su app.
([Wati](https://www.wati.io/en/blog/whatsapp-api-pricing-guide/), [YCloud](https://www.ycloud.com/blog/whatsapp-api-pricing-update))

**Lo que NO pude confirmar (preguntar a 360dialog y a otro más):**
1. Que acepten un número venezolano (+58) y lo conecten por coexistencia.
2. Cómo se paga desde Venezuela (tarjeta, límites, factura en dólares).
3. Que el servidor reciba el **historial de chats** al conectar (hace falta para el filtro de contactos).

**Mi recomendación:** pedir información a **360dialog** y a **Dualhook**; si el 360dialog acepta el número y
el pago, empezar por ahí.

## 2. Políticas de Meta para asistentes con IA

- Desde el 15-ene-2026, Meta prohíbe en la API de WhatsApp Business a las empresas cuyo **producto principal**
  es un chatbot de IA general (ChatGPT, Copilot, Perplexity y similares).
- Siguen permitidos los asistentes de IA que atienden clientes **como apoyo de otro negocio** (el principal es
  vender inmuebles). Nuestro asistente califica clientes de una inmobiliaria: queda del lado permitido.
  ([Dataslayer](https://www.dataslayer.ai/blog/meta-bans-general-purpose-ai-chatbots-on-whatsapp-business),
  [Alibaba Cloud](https://www.alibabacloud.com/help/en/chatapp/use-cases/whatsapp-ai-policy-2026-guide),
  [TechCrunch](https://techcrunch.com/2025/10/18/whatssapp-changes-its-terms-to-bar-general-purpose-chatbots-from-its-platform))
- Por eso conviene mantener el diseño actual: conversaciones solo sobre inmuebles, no un chat abierto.
- **Por confirmar** (con el proveedor, leyendo los términos vigentes): si hay que avisar al cliente que habla
  con un asistente automático y cómo manejar la opción de que el cliente pida hablar con una persona.
  Nuestro diseño ya lo hace (no dice ser una persona, y pasa el caso a Eduardo si lo piden).

## 3. Dónde vive la base de propiedades y los datos del asistente

**Hallazgo importante:** hoy la base (propiedades, Clientes, Conocimiento) vive **dentro de la página**. Un
servidor externo no la puede leer ni escribir por su cuenta; lo que sí escribe en ella son la propia página y
las sesiones mías. Yo no tengo confirmado que exista una vía para que un servidor externo la use.

Entonces el plan de "el servidor guarda la ficha en la pestaña Clientes" necesita una decisión:

| Opción | Cómo funciona | Pros / contras |
|---|---|---|
| **A. Una base de datos propia** (por ejemplo Supabase o similar) | El servidor y la página leen y escriben ahí. | Todo en tiempo real y confirmaciones al instante. Más trabajo de montar y migrar. **Recomendada para el final.** |
| **B. Archivos + sincronización** | La rutina semanal publica las propiedades en un archivo que lee el servidor; las fichas se guardan en el servidor y se pasan a la pestaña Clientes cada cierto tiempo. | Más simple de arrancar. Lo que se destaca o confirma entre lunes tarda en llegar al servidor. |

**Mi propuesta:** arrancar con la **B** en modo prueba (el asistente no envía solo) y pasar a la **A** cuando
funcione bien.

**Servidor:** un servicio pequeño en la nube (Cloudflare Workers, Render, Railway o Fly.io son opciones
típicas). Costos por confirmar al elegir.

## 4. Notas de voz

- WhatsApp entrega el audio como archivo (.ogg con códec Opus) y la coexistencia también sincroniza las notas
  de voz. ([Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages),
  [Instantreply](https://www.instantreply.co/blog/whatsapp-coexistence-what-actually-syncs-2026))
- Camino: llega el aviso → el servidor baja el audio → un servicio de voz a texto lo transcribe → el asistente
  lee el texto como si el cliente lo hubiera escrito.
- Costo orientativo de la transcripción: unos **US$0,003 a 0,006 por minuto** (OpenAI, Deepgram, AssemblyAI,
  Google). Un audio de un minuto cuesta menos de un centavo.
  ([Deepgram](https://deepgram.com/learn/best-speech-to-text-apis-2026), [AssemblyAI](https://www.assemblyai.com/blog/google-cloud-speech-to-text-alternatives))
- **Por probar:** qué tan bien entienden el español venezolano y el ruido de fondo. Se prueba con audios reales
  de Eduardo antes de decidir.
- Si el audio no se entiende o es muy largo, el asistente le pide al cliente que lo escriba y avisa a Eduardo.

## 5. Lo que hay que preguntarle a los proveedores (lista corta)

1. ¿Conectan un número de Venezuela (+58) con coexistencia?
2. ¿Cómo se paga desde Venezuela y en qué moneda se factura?
3. ¿El servidor recibe el historial de chats y la lista de números al conectar?
4. ¿Se pueden usar las etiquetas de la app Business (por ejemplo "Cliente") desde la API? (No lo pude confirmar.)
5. ¿Qué políticas de Meta sobre IA les piden aceptar?
6. ¿Cuánto cuesta al mes y por mensaje?
