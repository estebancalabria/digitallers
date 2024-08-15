import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
from groq import Groq

api_key = simpledialog.askstring("API Key", "Ingrese su API Key de Groq para continuar")
if not api_key:
    exit()

groq = Groq(api_key = api_key)
#Aca mantenemos el historial de mensajes en memoria para que el chatbot tenga contexto
chat_mensajes = []

#Diseniar con grid esta pantalla
# [                         ]
# [                         ]
# [      Text               ]
# [                         ]
# [Entry            ][Button]

def agregar_mensaje_chat(role, mensaje):
    area_texto.config(state=tk.NORMAL)  # Habilitar la edición en el área de texto
    area_texto.insert(tk.END, f"{role}: {mensaje}\n")  # Insertar el mensaje en el área de texto
    area_texto.config(state=tk.DISABLED)  # Deshabilitar la edición de nuevo
    entrada.delete(0, tk.END)  # Limpiar el campo de entrada
    area_texto.yview(tk.END)  # Hacer scroll hasta el final del texto

def enviar_mensaje():
    mensaje = entrada.get()  # Obtener el texto del campo de entrada
    
    if mensaje.strip():  # Verificar que no esté vacío
        chat_mensajes.append({
            "role" : "user",
            "content" : mensaje
        })

        #Vamos mostrando los mensajes en el chat (el mio)
        agregar_mensaje_chat("Tu", mensaje)

        respuesta = groq.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=chat_mensajes
        )

        str_respuesta = respuesta.choices[0].message.content

        chat_mensajes.append({
            "role" : "system",
            "content" : str_respuesta
        })

        #Vamos mostrando los mensajes en el chat (La respuesta)
        agregar_mensaje_chat("Groq",str_respuesta)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz tipo Chat")
ventana.geometry("640x480")
ventana.minsize(400, 500)

# Configurar la ventana para que las filas y columnas sean escalables
ventana.grid_rowconfigure(1, weight=1)  # Hacer que la segunda fila (área de chat) sea escalable
ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna se ajuste al ancho disponible

# Crear un área de texto para mostrar los mensajes del chat (con scroll)
area_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state=tk.DISABLED, font=("Helvetica", 12))
area_texto.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Crear el campo de entrada de texto
entrada = tk.Entry(ventana, font=("Helvetica", 12))
entrada.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Crear el botón de envío (en color azul)
boton_enviar = tk.Button(ventana, text="Enviar", bg="blue", fg="white", font=("Helvetica", 12), command=enviar_mensaje)
boton_enviar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()

