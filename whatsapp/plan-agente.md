# Asistente de WhatsApp: dónde estamos y cómo llegamos

## Dónde queremos llegar

Un asistente que atiende el WhatsApp Business de Eduardo (mismo número), habla como "el equipo de
Eduardo León", lee toda la conversación antes de responder, califica al cliente, le envía opciones
reales de la base maestra y le pasa a Eduardo una ficha por su WhatsApp personal y a la pestaña
"Clientes". Eduardo puede entrar en cualquier momento y el asistente se aparta.

## Dónde estamos (28-09-2026)

| Pieza | Estado |
|---|---|
| Diseño: personalidad, preguntas, ficha, reglas (`whatsapp/agente-diseno.md`) | ✅ Listo, falta que Eduardo revise el banco de preguntas |
| Copiloto dentro de la base maestra (pegar conversación → respuesta + ficha + propiedades) | ✅ Construido, falta probarlo con clientes reales |
| Pestañas Clientes y Conocimiento | ✅ Construidas; el conocimiento cargado está "por aprobar" |
| Base de propiedades (RE/MAX, Century 21, ZonaVen, BienesOnline, Admyser) | ✅ ~380 propiedades, actualización semanal |
| Rutina semanal de noticias por aprobar | ⏳ Por hacer |
| Conexión real con WhatsApp | ⏳ Fase 3 |

## Las 3 fases

### Fase 2 (ahora): probar con el copiloto, 1 a 2 semanas
- Eduardo usa el copiloto con clientes reales: pega la conversación, revisa la respuesta, la ajusta y la envía.
- Anotamos qué respuestas cambió y por qué, y afinamos el tono y las reglas.
- Tu papá aprueba el conocimiento (guía de Venezuela Renace, respuestas a inversionistas, oficina).
- **Meta:** que en la mayoría de los casos Eduardo envíe la respuesta sugerida casi sin cambios.

### Fase 3: conectar con WhatsApp

Cómo funcionaría:

```
Cliente escribe por WhatsApp
      │
      ▼
Proveedor de la API de WhatsApp (con coexistencia: Eduardo sigue usando su app)
      │  aviso de mensaje nuevo
      ▼
Servidor del asistente (un programa pequeño en la nube)
      │  lee el historial completo del chat
      ├─► Claude: redacta la respuesta y actualiza la ficha
      ├─► Base de propiedades: busca opciones que calcen
      │
      ├─► Responde al cliente por WhatsApp
      └─► Si hay que pasarlo: envía la ficha al WhatsApp personal de Eduardo y la guarda en "Clientes"
```

Reglas técnicas importantes:
- **Si Eduardo escribe en el chat, el asistente se calla** en esa conversación (la coexistencia permite detectar los mensajes que Eduardo envía desde su app).
- **Solo responde dentro de las 24 horas** desde el último mensaje del cliente (regla de WhatsApp). Los seguimientos los hace Eduardo.
- **Modo prueba primero:** durante los primeros días el asistente no envía nada solo; deja la respuesta lista para que Eduardo la apruebe con un toque. Después se activa el envío automático, empezando por los mensajes de bienvenida y calificación.

### Decisiones pendientes para la fase 3

1. **Proveedor de WhatsApp con coexistencia** que funcione con números de Venezuela. Hay que comparar 2 o 3 (costos mensuales, si permiten conectar un servidor propio y si soportan coexistencia) y confirmar las políticas vigentes de Meta para asistentes con IA.
2. **Dónde vive la base de propiedades para el servidor.** Hoy la base vive dentro de la página del análisis, y un servidor externo no puede leerla directo. Opciones:
   - a) La rutina semanal también publica una copia de las propiedades en un archivo que el servidor lee (lo más simple).
   - b) Mover la base a una base de datos propia (más trabajo, más flexible).
3. **Dónde corre el servidor:** un servicio en la nube de bajo costo. Se decide junto con el proveedor.
4. **Cuenta de la API de Claude:** el asistente usa la API de Anthropic, que se paga por uso. Una conversación de calificación cuesta centavos, pero hay que abrir la cuenta y poner un límite de gasto mensual.

### Lo que necesitaría de Eduardo para la fase 3
- Cuenta de **Meta Business** verificada (la pide cualquier proveedor de la API de WhatsApp).
- Elegir el proveedor y crear la cuenta (lo hacemos juntos, paso a paso).
- Una cuenta en la **consola de Anthropic** con método de pago y límite de gasto.
- Su **WhatsApp personal** para recibir las fichas.

## Riesgos y cuidados
- **Confianza:** el asistente nunca dice ser una persona. Si lo preguntan, dice que es el asistente virtual del equipo.
- **Datos personales:** las conversaciones y fichas se guardan solo donde Eduardo decida, y no se comparten fuera del equipo.
- **Errores:** el asistente no da precios, asesoría legal ni promesas; ante la duda, pasa el cliente a Eduardo.
