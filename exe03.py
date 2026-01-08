# Exercício 03 – Campo de Entrada (Básico–Intermediário)
# Crie uma interface contendo um Label com o texto “Nome” e um campo Entry logo abaixo.
# Requisitos:
# - Uso correto de Entry
# - Layout organizado
import tkinter as tk
app=tk.Tk()
app.geometry("1820x980")
app.title("Exercicio 3")
app.resizable(False,False)
app.configure(background="white")
app.option_add("*Font", "Roboto 14")


mainframe = tk.Frame(app)
mainframe.pack()


label = tk.Label(mainframe,text="Nome:",background="white")
label.grid(row=0,column=0,padx=10,pady=10)
entry = tk.Entry(mainframe)
entry.grid(row=0,column=1,padx=10,pady=10)

app.mainloop()