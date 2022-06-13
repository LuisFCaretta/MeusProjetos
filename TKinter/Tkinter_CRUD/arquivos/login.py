from tkinter import TRUE, Button, Entry, Frame, Label, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import mysql.connector


class Login():
    def __init__(self, master=None):
        self.frame_cima = Frame(login, width=300, height=50, bg="#403d3d", relief="flat", border=1)
        self.frame_cima.grid(row=0, column=0)
        self.frame_baixo = Frame(login, width=300, height=350, relief="flat", border=1)
        self.frame_baixo.grid(row=1, column=0, padx=0, pady=1)

        self.frame_nome = Label(self.frame_cima, text="Login", anchor="sw", font=("Ivy 20 bold"), bg="#403d3d", relief="flat")
        self.frame_nome.place(x=100, y=5)

        self.l_email = Label(self.frame_baixo, text="Email", anchor="nw", font=("Times 20 bold"), relief="flat")
        self.l_email.place(x=20, y=0)

        self.email_entry = Entry(self.frame_baixo, width=30, font=("Times 12 bold"), justify="left", relief="raised")
        self.email_entry.place(x=20, y=40)

        self.l_senha = Label(self.frame_baixo, text="Senha", anchor="nw", font=("Times 20 bold"), relief="flat")
        self.l_senha.place(x=20, y=80)

        self.senha_entry = Entry(self.frame_baixo, width=30, font=("Times 12 bold"), justify="left", relief="raised")
        self.senha_entry.place(x=20, y=120)


        def verifica_login():
            email = self.email_entry.get()
            senha = self.senha_entry.get()
            if email == "" or senha == "":
                messagebox.showerror('Erro!', 'Os campos não podem ser vazios!')
                return
            ver = [email, senha]
            con = mysql.connector.connect(host='localhost', database='db_user_admin', user='root', password='', autocommit=True, use_unicode=True)
            cursor = con.cursor(buffered=True)
            cursor.execute("select email_admin, senha_admin, nome_admin from admin")
            verifica = cursor.fetchall()
            for admin in verifica:
                try:
                    if admin[0] == ver[0] and admin[1] == ver[1]:
                        messagebox.showinfo('Sucesso!', f'Seja bem vindo(a), {admin[2]}!')
                        login.destroy()
                        
                    
                    if admin[0] == ver[0] and admin[1] != ver[1]:
                        messagebox.showerror("Erro", "Senha incorreta, verifique e tente novamente!")
                        return
                    if admin[0] != ver[0] and admin[1] == ver[1]:
                        messagebox.showerror("Erro", "Email incorreto, verifique e tente novamente!")
                        return
                except:
                    return
            if ver[0] not in admin[0]:
                messagebox.showerror("Erro", "Você ainda não possui cadastro, verifique e tente novamente!")
            return
                
        self.btn_login = Button(self.frame_baixo, text="Login", font=("Ivy 10 bold"), width=20, height=2, bg="#403d3d", relief="groove", overrelief="sunken", command=verifica_login)
        self.btn_login.place(x=60, y=180)
        

        
        self.btn_cadastrar = Button(self.frame_baixo, text="Cadastrar", font=("Ivy 10 bold"), width=20, height=2, bg="#403d3d", relief="groove", overrelief="sunken" )
        self.btn_cadastrar.place(x=60, y=240)




        

        
login = ThemedTk(theme="black")
login.title("Minha Biblioteca Login")
login.geometry("300x400")
login.resizable(width=False, height=False)
Login(login)
login.mainloop()
