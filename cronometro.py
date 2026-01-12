import tkinter as tk
import ttkbootstrap as ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x180")
        self.root.title("Cronometro Simples")
        self.root.configure(bg='#333333')
        self.root.option_add('*Font','Roboto 20')
        self.root.resizable(False,False)
        self.root.attributes('-topmost',True)

        # Mainframe
        self.mainframe = ttk.Frame(root,bootstyle="DARK")
        self.mainframe.pack(pady=10)

        # Label principal
        self.label = ttk.Label(self.mainframe,text='00:00:00', foreground="white",background="#333333",font="DS-DIGITAL 56 bold")
        self.label.grid(row=0,column=0,pady=5)

        # ButtonFrame
        self.button_frame = ttk.Frame(root,bootstyle="DARK")
        self.button_frame.pack()

        # Buttons

        self.button_iniciar = ttk.Button(self.button_frame, text="Iniciar",bootstyle="SUCCESS",command=self.iniciar,width=10)
        self.button_iniciar.pack(side="left",padx=2)

        self.button_parar = ttk.Button(self.button_frame,text="Parar",bootstyle="DANGER",command=self.parar,width=10)
        self.button_parar.pack(side="left", padx=2)

        self.button_resetar = ttk.Button(self.button_frame, text="Resetar",bootstyle="SECONDARY",command=self.resetar,width=10)
        self.button_resetar.pack(side="right", padx=2)

        self.cronometro = 0
        self.rodando = False

    def cronometro_timer(self):

        if self.rodando:
            self.cronometro += 1

            h = self.cronometro // 3600
            m = (self.cronometro % 3600) // 60
            s = self.cronometro % 60

            self.label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            self.root.after(1000, self.cronometro_timer)

    def iniciar(self):
        
        if self.rodando == True:
            return None
        
        if self.rodando == False:
            self.rodando = True
            self.cronometro_timer()

    def parar(self):
        self.rodando = False

    def resetar(self):
        self.cronometro = 0
        self.label.config(text=f"00:00:00")

        self.rodando = False

if __name__ == "__main__":
    window = ttk.Window()
    app = App(window)
    window.mainloop()


    