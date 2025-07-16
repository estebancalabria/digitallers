import gradio as gr
from groq import Groq

def dialogar(chat, api_key, conversacion):
  if api_key:  
    try:
      client = Groq(api_key=api_key)

      chat_completion = client.chat.completions.create(
          messages=[
              {
                  "role": "system",
                  "content": "Eres una IA seductora que quieres conocer a tu usuario. Tu objetivo es conocer a fondo a tu interlocutor y lograr empatizar. Respondes con oraciones y parrafos no mas de 100 palabras en total.",
              },
              *[{"role": "user" if i % 2 == 0 else "assistant", "content": msg} for i, msg in enumerate(conversacion)]
          ],
          model="llama-3.3-70b-versatile",
          stream=False
      )

      conversacion.append(chat_completion.choices[0].message.content)

      chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "system",
              "content": "Eres una IA misteriosa e intrigante que le gusta conversar. Tu objetivo es desafiar a tu interlocutor y llevarlo al limite conocer sus secretos mas oscuros. Respondes con oraciones y parrafos no mas de 100 palabras en total.",
          },
          *[{"role": "assistant" if i % 2 == 0 else "user", "content": msg} for i, msg in enumerate(conversacion)]

      ],
      model="llama-3.3-70b-versatile",
      stream=False
    )
      
      conversacion.append(chat_completion.choices[0].message.content)

      chat.append( [conversacion[-2], conversacion[-1]] )
    
    except Exception as e:
      chat.append(["Error", str(e)])

  return chat, conversacion

with gr.Blocks() as interfaz:
  titulo = gr.Markdown("## Sala de chat Infinita")
  api_key_input = gr.Textbox(label="Ingrese Api Key de Groq", type="password")
  #conversacion = gr.Textbox(label="Conversacion", lines=15)
  conversacion = gr.State(["Hola"])
  start_btn = gr.Button("Iniciar Conversacion")
  stop_btn = gr.Button("Detener Conversacion")
  #boton = gr.Button("Avanzar Dialogo")
  chatbot = gr.Chatbot(label="Conversacion")
  timer = gr.Timer(value=10)
  #boton.click(dialogar, inputs=[chatbot, api_key_input, conversacion], outputs=[chatbot, conversacion])
  timer.tick(dialogar, inputs=[chatbot, api_key_input, conversacion], outputs=[chatbot, conversacion])
  start_btn.click(lambda: gr.update(running=True), outputs=timer)
  stop_btn.click(lambda: gr.update(running=False), outputs=timer)


interfaz.launch()
