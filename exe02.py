# Exercício 02 – Botão Simples (Básico)
# Crie uma janela que contenha um texto “Clique no botão” e um botão com o texto “OK”.
# Requisitos:
# - Usar Label e Button
# - Layout com pack
import tkinter as tk

app = tk.Tk()
app.geometry("1080x720")
app.title("Exercicio 2")
app.resizable(False,False)

mainframe = tk.Frame(app,width=1080,height=720)
mainframe.pack()

middle_box = tk.Frame(mainframe)
middle_box.configure(width=270,height=180,background="#444444")
middle_box.grid(row=0,column=1,padx=10,pady=10)

side_bar = tk.Frame(mainframe,width=70,height=180,background="#444444")
side_bar.grid(row=0,column=0,padx=50,pady=10, sticky="W")

side_bar_right = tk.Frame(mainframe,width=70,height=180,background="#444444")
side_bar_right.grid(row=0,column=5,padx=50,pady=10, sticky="E")


label = tk.Label(middle_box,font=("Roboto", 32), text="Clique no botão!",fg="white",background="#444444")
label.pack(padx=10,pady=10)

button = tk.Button(middle_box,text="OK :)")
button.pack(pady=30)



app.mainloop()


