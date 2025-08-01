import tkinter as tk
import itertools

# --- Funciones sin variables globales ---------------------------------------
def add_line(chat, timer_id, people, turn):
    person = next(turn)
    chat.configure(state="normal")
    chat.insert("end", f"{person}: hola\n")
    chat.configure(state="disabled")
    chat.see("end")
    timer_id[0] = chat.after(2000, add_line, chat, timer_id, people, turn)

# --- Ventana y widgets --------------------------------------------------------
root = tk.Tk()
root.title("Chat Alicia & Bob")
root.geometry("800x600")
root.resizable(False, False)

# Área de chat
chat_area = tk.Text(root, state="disabled", wrap="word")
chat_area.pack(fill="both", expand=True, padx=5, pady=5)

# Marco inferior
bottom = tk.Frame(root)
bottom.pack(fill="x", padx=5, pady=5)

# Botón para detener
stop_btn = tk.Button(bottom, text="Detener")
stop_btn.pack(side="right")

# Generador de turnos
people = ("Alicia", "Bob")
turn = itertools.cycle(people)

# Referencia mutable al id del timer
timer_id = [None]

def stop():
    if timer_id[0]:
        root.after_cancel(timer_id[0])
        timer_id[0] = None
stop_btn.configure(command=stop)

# Arrancar el primer ciclo
timer_id[0] = root.after(2000, add_line, chat_area, timer_id, people, turn)

root.mainloop()