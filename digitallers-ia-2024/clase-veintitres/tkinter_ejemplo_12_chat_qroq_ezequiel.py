import os
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
from groq import Groq

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Chat con IA")
ventana.geometry("600x500")
ventana.configure(bg="#f0f4f8")  # Fondo claro

# Variable global para almacenar la API key y cliente
api_key = None
client = None

# Función para solicitar la API key
def solicitar_api_key():
    global api_key
    api_key = simpledialog.askstring("API Key", "Introduce tu API Key de Groq:")
    if not api_key:
        messagebox.showerror("Error", "API Key es requerida")
        ventana.destroy()
        return
    os.environ["GROQ_API_KEY"] = api_key
    iniciar_cliente()

# Configurar el cliente Groq
def iniciar_cliente():
    global client
    try:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        ventana.deiconify()  # Mostrar la ventana principal
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API: {str(e)}")
        ventana.destroy()

# Función para enviar el mensaje al servidor de IA y recibir la respuesta
def enviar_mensaje(event=None):
    user_input = entry.get("1.0", tk.END).strip()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Tú: {user_input}\n", 'user')
        chat_area.config(state=tk.DISABLED)
        entry.delete("1.0", tk.END)

        try:
            # Enviar el mensaje a la API de Groq
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_input}
                ],
                model="llama3-8b-8192",
            )

            ia_response = chat_completion.choices[0].message.content

        except Exception as e:
            ia_response = f"Error al conectar con la API: {str(e)}"

        # Mostrar la respuesta de la IA
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"IA: {ia_response}\n", 'ai')
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)

# Ocultar la ventana principal mientras se solicita la API key
ventana.withdraw()

# Solicitar la API key al iniciar
solicitar_api_key()

# Configurar la cuadrícula principal para que se ajuste al tamaño
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=0)

# Área de chat (texto ampliado)
chat_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=('Helvetica', 14), state=tk.DISABLED, bg="#ffffff", fg="#000000", insertbackground='black')
chat_area.tag_configure('user', foreground="#1f77b4", font=('Helvetica', 14, 'bold'))
chat_area.tag_configure('ai', foreground="#ff7f0e", font=('Helvetica', 14, 'italic'))
chat_area.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Frame para entrada de texto y botón de enviar
entry_frame = tk.Frame(ventana, bg="#f0f4f8")
entry_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

# Configurar la cuadrícula dentro del frame de entrada
entry_frame.grid_columnconfigure(0, weight=1)
entry_frame.grid_columnconfigure(1, weight=0)

# Campo de entrada de texto
entry = tk.Text(entry_frame, height=2, font=('Helvetica', 14), bg="#ffffff", fg="#000000", borderwidth=2, relief='groove')
entry.grid(row=0, column=0, sticky="ew", padx=10)

# Botón de enviar
send_button = tk.Button(entry_frame, text="Enviar", font=('Helvetica', 14, 'bold'), command=enviar_mensaje, bg="#1f77b4", fg="#ffffff", borderwidth=0, relief='flat')
send_button.grid(row=0, column=1, sticky="nsew", padx=10)

# Asegurar que el campo de texto tenga la misma altura que el botón
entry_frame.update_idletasks()
entry_height = send_button.winfo_height()
entry.config(height=int(entry_height / 20))  # Ajustar altura del campo de texto

# Enviar mensaje al presionar Enter
entry.bind("<Return>", enviar_mensaje)

# Iniciar la interfaz
ventana.mainloop()
