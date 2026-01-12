import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class LoginApp:
    def __init__(self, root):
        self.root = root

        # Configuração da tela inicial
        self.root.geometry("900x700")
        self.root.title("Tela de login")
        self.root.configure(bg='#333333')
        self.root.option_add('*Font','Roboto 16')
        self.root.resizable(False,False)

        # Mainframe Login
        self.login_frame = tk.Frame(root,bg='#333333')
        self.login_frame.pack()

        # Imagem como PhotoImage
        self.image = tk.PhotoImage(file='login.png',format='png')
        self.image = self.image.subsample(6)
        self.label_image = tk.Label(self.login_frame, image=self.image, bg='#333333')
        self.label_image.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

        # Label
        self.label_email = tk.Label(self.login_frame,text="Email:",fg='#ffffff',bg='#333333',font=("Roboto", 12))
        self.label_email.grid(row=1,column=0,pady=5)

        self.label_senha = tk.Label(self.login_frame,text="Senha:",fg='#ffffff',bg='#333333',font=("Roboto", 12))
        self.label_senha.grid(row=2,column=0,pady=5)
        # Entry
        self.input_email = ttk.Entry(self.login_frame,width=15)
        self.input_email.grid(row=1,column=1,pady=5)

        self.input_senha = ttk.Entry(self.login_frame,width=15)
        self.input_senha.grid(row=2, column=1,pady=5)

        # Button Frame
        self.button_frame = tk.Frame(root,bg="#333333")
        self.button_frame.pack(pady=10)
        # Buttons
        self.login_button = ttk.Button(self.button_frame, text="log in",style="TButton",command=self.valid_login)
        self.login_button.pack(side="right",padx=20)

        style_button = ttk.Style()
        style_button.configure('TButton',background ="#333333", fg = "#ffffff")

        style_entry = ttk.Style()
        style_entry.configure("TEntry" ,background = "#7E7E7E")

        self.signin_button = ttk.Button(self.button_frame, text="sign in")
        self.signin_button.pack(side="left",padx=20)

    def valid_login(self):
        user = self.input_email.get()
        password = self.input_senha.get()

        if user != 'admin':
            messagebox.showerror("Erro de Login", 'e-mail ou senha inválido')
            
        messagebox.showinfo(f'Login Bem sucedido', f'Bem vindo {user}')



if __name__ == "__main__":
    window = tk.Tk()
    app = LoginApp(window)
    window.mainloop()