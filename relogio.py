import tkinter as tk
from tkinter import ttk
from datetime import datetime as dt

def atualizar_relogio():
    hora_atual = dt.now()
    format_hora_atual = hora_atual.strftime("%H:%M:%S")
    label_relogio.set(format_hora_atual)
    root.after(1000, atualizar_relogio)

root = tk.Tk()
root.configure(bg="#333333")
root.geometry("200x80")
root.resizable(False,False)
root.option_add("*Font","DS-DIGITAL 36 bold")

label_relogio = tk.StringVar()
label = ttk.Label(root, textvariable=label_relogio,background="#333333",foreground="#00ff00")
label.pack(pady=10)

atualizar_relogio()


root.mainloop()