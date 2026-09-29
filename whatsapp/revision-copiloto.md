# Revisión del copiloto (Kira): primera prueba, 29-09-2026

## Lo que se revisó

En la pestaña Clientes quedó guardado **1 cliente**: Idania, que llegó por la oficina de Aventura. Los otros
dos chats se analizaron, pero no se guardaron: para que queden hay que tocar **Guardar en Clientes**.
El conocimiento aprobado era **0**, así que Kira solo podía preguntar.

## Qué hizo bien

- Sacó los datos clave del chat:
  - Presupuesto: USD 25.000.
  - Forma de pago: en bolívares.
  - Zona: Guarenas y Guatire.
  - Tipo: apartamento o casa.
- La calificó como 🌤️ tibia, con un buen motivo: tiene presupuesto, pero le faltan el sector y el plazo.
- Encontró 8 propiedades de la base dentro del presupuesto.
- No repitió preguntas que la cliente ya había respondido.

## Qué hay que corregir

| # | Problema | Por qué importa | Arreglo |
|---|---|---|---|
| 1 | **Hizo dos preguntas en un solo mensaje** (sector y para qué es) | La regla es una sola pregunta por mensaje | Reforzar la regla y revisarlo en el formato de salida |
| 2 | **Tuteó** ("¿tienes…?"), pero Eduardo le habló de usted | El trato tiene que seguir el de Eduardo, no solo el del cliente | Copiar el trato que usa Eduardo en el chat |
| 3 | **No sabe qué dijo Eduardo en el audio** (`<mensaje de voz omitido>`) | Puede preguntar algo que ya se habló | Agregar una casilla **"Lo que dije en audios o llamadas"** |
| 4 | **No reconoce en qué etapa va el chat.** La cliente ya dijo "quedo atenta a su información" y Kira volvió a preguntar | En ese punto lo que toca es enviarle opciones | Que primero decida la etapa: calificar, enviar opciones, agendar visita o dar seguimiento |
| 5 | **No registra de dónde vino el cliente** (oficina, Instagram, portal, referido) | Sirve para medir qué canal trae clientes | Agregar el campo "Origen" a la ficha |
| 6 | **Pago en bolívares:** no sabe qué decir | Muchos propietarios quieren dólares, y Idania paga en bolívares | Crear una ficha de conocimiento (por confirmar con Luis León) |

## El conocimiento que le falta a Kira (por redactar y aprobar)

1. **Formas de pago:** bolívares a tasa BCV, dólares en efectivo, transferencia, Zelle, y qué suelen aceptar
   los propietarios. *Por confirmar con Luis León.*
2. **El proceso de compra, paso a paso:** reserva, opción de compraventa, documentos, registro y tiempos
   aproximados.
3. **Quién paga qué:** comisión, gastos de registro y Forma 33. *Por confirmar con Luis León.*
4. **Las visitas:** cómo se agendan y qué llevar.
5. **Plantillas de mensajes:** bienvenida, envío de opciones, seguimiento a las 24 y 72 horas, después de la
   visita y cliente que no responde.

## Próximos pasos (cuando retomemos)

1. Aplicar los arreglos 1 a 5 en el copiloto (página de la base).
2. Redactar las fichas de conocimiento, dejarlas **por aprobar** y que Luis León las revise.
3. Probar con los 3 chats de nuevo y **guardarlos** en Clientes.

## Aplicado (29-09-2026, de noche)

- ✅ **1. Una sola pregunta:** la regla quedó reforzada y la página avisa en amarillo si la respuesta trae más de un "?".
- ✅ **2. Trato:** Kira usa el mismo trato que Eduardo en el chat (usted o tú).
- ✅ **3. Audios:** casilla nueva "Lo que dije en audios o llamadas", que se guarda con el cliente.
- ✅ **4. Etapas:** Kira decide si toca calificar, enviar opciones, agendar visita, dar seguimiento o pasar a Eduardo.
  Cuando toca **enviar opciones**, la página agrega sola las 3 mejores propiedades de la base, con enlace.
- ✅ **5. Origen:** campo "¿De dónde vino?" que se guarda y se ve en Clientes.
- ✅ **Tipos:** si el cliente acepta varios tipos ("apto o casa"), Kira busca solo en esos tipos.
- ✅ **Conocimiento:** 5 fichas nuevas *por aprobar*: formas de pago, proceso de compra, quién paga qué, visitas y
  plantillas de mensajes. Lo no confirmado va marcado POR CONFIRMAR.
- ⏳ **Pendiente de Eduardo:** aprobar las fichas, volver a probar con los 3 chats y guardarlos en Clientes.
