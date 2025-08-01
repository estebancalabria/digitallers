import tkinter as tk
from functools import partial
import threading
import time
import os
from groq import Groq

# -----------------------------------------------------------
# Lógica de chat
# -----------------------------------------------------------
def dialogar_step(chat, api_key, conversacion):
    if not api_key:
        _insert(chat, "Sistema: Falta API Key\n")
        return

    try:
        client = Groq(api_key=api_key)

        # Primera IA
        r1 = client.chat.completions.create(
            messages=[
                {"role": "system",
                 "content": "Eres una IA seductora que quiere conocer al usuario. "
                             "Responde con no más de 100 palabras."},
                *[{"role": "user" if i % 2 == 0 else "assistant", "content": msg}
                  for i, msg in enumerate(conversacion)]
            ],
            model="llama-3.3-70b-versatile",
            stream=False
        )
        resp1 = r1.choices[0].message.content
        conversacion.append(resp1)

        # Segunda IA
        r2 = client.chat.completions.create(
            messages=[
                {"role": "system",
                 "content": "Eres una IA misteriosa que desafía al usuario. "
                             "Responde con no más de 100 palabras."},
                *[{"role": "assistant" if i % 2 == 0 else "user", "content": msg}
                  for i, msg in enumerate(conversacion)]
            ],
            model="llama-3.3-70b-versatile",
            stream=False
        )
        resp2 = r2.choices[0].message.content
        conversacion.append(resp2)

        _insert(chat, f"IA1: {resp1}\n\n")
        _insert(chat, f"IA2: {resp2}\n\n")

    except Exception as e:
        _insert(chat, f"Error: {e}\n")


def _insert(chat, text):
    chat.configure(state="normal")
    chat.insert("end", text)
    chat.configure(state="disabled")
    chat.see("end")

# -----------------------------------------------------------
# Timer en segundo plano
# -----------------------------------------------------------
def timer_loop(chat, api_key, conversacion, stop_flag):
    while not stop_flag["stop"]:
        time.sleep(10)
        if stop_flag["stop"]:
            break
        chat.after(0, dialogar_step, chat, api_key.get(), conversacion)

def start_timer(chat, api_key, conversacion, stop_flag, thread_ref):
    if thread_ref[0] is None or not thread_ref[0].is_alive():
        stop_flag["stop"] = False
        t = threading.Thread(target=timer_loop,
                             args=(chat, api_key, conversacion, stop_flag),
                             daemon=True)
        t.start()
        thread_ref[0] = t

def stop_timer(stop_flag):
    stop_flag["stop"] = True

# -----------------------------------------------------------
# GUI
# -----------------------------------------------------------
root = tk.Tk()
root.title("Sala de chat infinita")
root.geometry("800x600")

api_key_var = tk.StringVar()
conversacion = ["Hola"]
stop_flag = {"stop": False}
thread_ref = [None]

# API Key
tk.Label(root, text="Groq API Key:").pack(pady=2)
tk.Entry(root, textvariable=api_key_var, show="*", width=50).pack(pady=2)

# Botones
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

chat_area = tk.Text(root, state="disabled", wrap="word")
chat_area.pack(fill="both", expand=True, padx=5, pady=5)

# Partial correctos
start_cmd = partial(start_timer, chat_area, api_key_var, conversacion, stop_flag, thread_ref)
stop_cmd = partial(stop_timer, stop_flag)

tk.Button(btn_frame, text="Iniciar conversación", command=start_cmd).pack(side="left", padx=5)
tk.Button(btn_frame, text="Detener conversación", command=stop_cmd).pack(side="left", padx=5)

root.mainloop()