# Exercício 04 – Formulário com Grid (Intermediário)
# Crie um formulário contendo Nome, Email e um botão “Cadastrar”.
# Requisitos:
# - Usar grid
# - Não misturar pack e grid

import tkinter as tk

app = tk.Tk()
app.geometry("1720x880")
app.title("exercicio-04")
app.option_add("*Font","Roboto 14")

mainframe = tk.Frame(app)
mainframe.pack()

label_nome = tk.Label(mainframe, text="Nome:")
label_nome.grid(row=0,column=0,padx=10,pady=10)
entry_nome = tk.Entry(mainframe)
entry_nome.grid(row=0,column=1,padx=10,pady=10)

label_email = tk.Label(mainframe, text="Email:")
label_email.grid(row=1,column=0,padx=10,pady=10)
entry_email = tk.Entry(mainframe)
entry_email.grid(row=1,column=1,padx=10,pady=10)

button_login = tk.Button(mainframe,text="Log in")
button_login.grid(row=2, column=1,padx=10,pady=10)
button_cadastro = tk.Button(mainframe,text="Sign up")
button_cadastro.grid(row=3, column=1,padx=10,pady=10)


app.mainloop()