# Exercício 01 – Janela com Texto (Básico)
# Crie uma aplicação Tkinter que abra uma janela e exiba um texto centralizado com o título “Sistema Desktop”.
# Requisitos:
# - Usar Label
# - Usar pack
# - Definir título da janela

import tkinter as tk

app = tk.Tk()

app.title("Sistema Desktop")
app.configure(background="#757575")
app.geometry("1080x720")

label = tk.Label(app,text="SENAC",font=("Roboto",24),background="#a7a7a7")
label.pack(padx=10,pady=10)

# PhotoImage
imagem = tk.PhotoImage(file="login.png", format="png")
imagem = imagem.subsample(4)

label_imagem = tk.Label(app, image=imagem)
label_imagem.pack()

app.mainloop()