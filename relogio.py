import tkinter as tk
from datetime import datetime as dt

def atualizar_relogio():
    hora_atual = dt.now()
    format_hora_atual = hora_atual.strftime("%H:%M:%S")
    label_relogio.set(format_hora_atual)
    root.after(1000, atualizar_relogio)

root = tk.Tk()
root.geometry("900x500")
root.resizable(False,False)
root.option_add("*Font","Roboto 28")

label_relogio = tk.StringVar()
label = tk.Label(root, textvariable=label_relogio)
label.pack(pady=10)

atualizar_relogio()


root.mainloop()