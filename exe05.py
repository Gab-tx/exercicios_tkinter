# Exercício 05 – Organização Visual (Intermediário)
# Ajuste o formulário anterior adicionando espaçamento e centralizando o botão.
# Requisitos:
# - Uso de padx, pady
# - Uso de columnspan

import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry("1720x880")
app.title("exercicio-04")
app.option_add("*Font","Roboto 14")

mainframe = ttk.Frame(app)
mainframe.pack()

label_nome = ttk.Label(mainframe, text="Nome:")
label_nome.grid(row=1,column=0,pady=10)
entry_nome = ttk.Entry(mainframe)
entry_nome.grid(row=2,column=0,pady=10)

label_email = ttk.Label(mainframe, text="Email:")
label_email.grid(row=3,column=0,pady=10)
entry_email = ttk.Entry(mainframe)
entry_email.grid(row=4,column=0,pady=10)

button_login = ttk.Button(mainframe,text="Log in",width=20)
button_login.grid(row=5, column=0,padx=10,pady=10)
button_cadastro = ttk.Button(mainframe,text="Sign up",width=20)
button_cadastro.grid(row=6, column=0,padx=10,pady=10)

# PhotoImage
imagem = tk.PhotoImage(file="login.png", format="png")
imagem = imagem.subsample(6)

label_imagem = tk.Label(mainframe, image=imagem)
label_imagem.grid(row=0, column=0)


app.mainloop()