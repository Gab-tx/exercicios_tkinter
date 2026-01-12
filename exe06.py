# Exercício 06 – Mini Cadastro (Intermediário–Avançado)
# Crie um formulário com Nome, Email, Telefone e botão “Salvar”.
# Requisitos:
# - Uso exclusivo de grid
# - Interface organizada


import tkinter as tk

class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("500x500")
        self.resizable(False,False)
        self.option_add("*Font","Roboto 14")
        self.attributes('-topmost',True)

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(anchor="s",padx=10)

        self.label_nome = tk.Label(self.mainframe, text="Nome:")
        self.label_nome.grid(row=1,column=0,pady=10)
        self.entry_nome = tk.Entry(self.mainframe)
        self.entry_nome.grid(row=1,column=1,pady=10,columnspan=2)

        self.label_email = tk.Label(self.mainframe, text="Email:")
        self.label_email.grid(row=2,column=0,pady=10)
        self.entry_email = tk.Entry(self.mainframe)
        self.entry_email.grid(row=2,column=1,pady=10,columnspan=2)

        self.label_telefone = tk.Label(self.mainframe, text="Telefone:")
        self.label_telefone.grid(row=3,column=0,pady=10)
        self.entry_telefone = tk.Entry(self.mainframe)
        self.entry_telefone.grid(row=3,column=1,pady=10,columnspan=2)

        self.button_salvar = tk.Button(self.mainframe,text="Salvar",width=8)
        self.button_salvar.grid(row=4, column=1,pady=10,sticky="E",columnspan=2)

if __name__ == "__main__":
    app = App()

    app.mainloop()



    