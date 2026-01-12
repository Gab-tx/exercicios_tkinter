# Exercício 07 – Desafio (Avançado)
# Crie uma tela inicial contendo um título e dois botões: “Cadastrar Usuário” e “Sair”.
# Requisitos:
# - Uso de Label e Button
# - Layout livre e organizado

import tkinter as tk

class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.geometry("1080x720")
        self.resizable(False,False)
        self.title("exercicio 07")
        self.option_add("*Font","Roboto 16")

        # Mainframe
        self.mainframe = tk.Frame(self,pady=50)
        self.mainframe.pack() 

        # Label
        self.label = tk.Label(self.mainframe, text="Bem-vindo!", font=("DS-DIGITAL",70))
        self.label.grid()

        # Button
        self.buttonFrame = tk.Frame(self,padx=10,pady=10 )
        self.buttonFrame.pack(pady=10)

        self.buttonCadastrar = tk.Button(self.buttonFrame, text="Cadastrar")
        self.buttonCadastrar.grid(column=1, row=0,padx=8)

        self.buttonSair = tk.Button(self.buttonFrame,background="#c94e4e",text="Sair",width=7)
        self.buttonSair.grid(column=0, row=0,padx=8)

if __name__ == "__main__":
    app = App()

    app.mainloop()