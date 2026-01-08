import tkinter as tk

app = tk.Tk()
app.geometry("1080x720")
app.title("Exercicio 2")
app.resizable(False,False)

upper_frame = tk.Frame(app,background="#444444", width=1080,height=50)
upper_frame.grid(row= 0,column= 0)

side_frame = tk.Frame(app,background="#444444", height=720,width=50)
side_frame.grid(row=1,column=0,sticky="W")

# PhotoImage
imagem = tk.PhotoImage(file="login.png", format="png")
# imagem.subsample(4)

label_imagem = tk.Label(app, image=imagem)
label_imagem.grid(row=1,column=1, padx=10, pady=10)

app.mainloop()