from tkinter import messagebox
import mysql.connector
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Minha biblioteca login")
label = customtkinter.CTkLabel(janela)
label.place()
janela.geometry("300x400")
janela.resizable(width=False, height=False)

frame_cima = customtkinter.CTkFrame(janela, width=300, height=50, fg_color="#348feb", border=1)
frame_cima.grid(row=0, column=0)
frame_baixo = customtkinter.CTkFrame(janela, width=300, height=350, relief="flat", border=1)
frame_baixo.grid(row=1, column=0, padx=0, pady=1)

frame_nome = customtkinter.CTkLabel(frame_cima, text="Login", bg_color="#348feb", anchor="center", text_font=("Arial 24 bold"))
frame_nome.place(x=75, y=5)

l_email = customtkinter.CTkLabel(frame_baixo, text="Email", width=80, anchor="nw", text_font=("Arial 18 bold"))
l_email.place(x=10, y=20)

email_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised")
email_entry.place(x=20, y=60)

l_senha = customtkinter.CTkLabel(frame_baixo, text="Senha", width=80, anchor="nw", text_font=("Arial 18 bold"))
l_senha.place(x=10, y=100)

senha_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised", show="*")
senha_entry.place(x=20, y=140)

def verifica_login():
    email = email_entry.get()
    senha = senha_entry.get()
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
                ...
                
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

btn_login = customtkinter.CTkButton(frame_baixo, text="Login", text_font=("Arial 24 bold"), width=200, fg_color="#348feb", height=10, command=verifica_login)
btn_login.place(x=50, y=200)

def telaCadastro():
    global janela
    janela.destroy()
    janela = customtkinter.CTkToplevel()
    janela.title("Minha Biblioteca Cadastro")
    janela.geometry("300x500")
    janela.resizable(width=False, height=False)

    frame_cima = customtkinter.CTkFrame(janela, width=300, height=50, fg_color="#348feb", relief="flat", border=1)
    frame_cima.grid(row=0, column=0)
    frame_baixo = customtkinter.CTkFrame(janela, width=300, height=450, relief="flat", border=1)
    frame_baixo.grid(row=1, column=0, padx=0, pady=1)

    frame_nome = customtkinter.CTkLabel(frame_cima, text="Cadastrar", bg_color="#348feb", anchor="sw", text_font=("Arial 24 bold"), relief="flat")
    frame_nome.place(x=65, y=5)

    l_nome = customtkinter.CTkLabel(frame_baixo, width=80, text="Nome", text_font=("Arial 18 bold"), anchor="nw", relief="flat")
    l_nome.place(x=10, y=0)

    l_nome_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised")
    l_nome_entry.place(x=20, y=40)    

    l_email = customtkinter.CTkLabel(frame_baixo, width=80, text="Email", text_font=("Arial 18 bold"), anchor="nw", relief="flat")
    l_email.place(x=10, y=80)

    email_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised")
    email_entry.place(x=20, y=120)

    l_senha = customtkinter.CTkLabel(frame_baixo, width=80, text="Senha", text_font=("Arial 18 bold"), anchor="nw", relief="flat")
    l_senha.place(x=10, y=160)

    senha_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised", show="*")
    senha_entry.place(x=20, y=200)

    l_senha2 = customtkinter.CTkLabel(frame_baixo, width=80, text="Repita sua senha", text_font=("Arial 18 bold"), anchor="nw", relief="flat")
    l_senha2.place(x=10, y=240)

    senha2_entry = customtkinter.CTkEntry(frame_baixo, width=260, justify="left", relief="raised", show="*")
    senha2_entry.place(x=20, y=280)

    btn_cadastrar = customtkinter.CTkButton(frame_baixo, text="Cadastrar", fg_color="#348feb", text_font=("Arial 24 bold"), width=200, height=10)
    btn_cadastrar.place(x=50, y=340)

btn_cadastrar = customtkinter.CTkButton(frame_baixo, text="Cadastrar", width=200, fg_color="#348feb", text_font=("Arial 24 bold"), height=10, command=telaCadastro)
btn_cadastrar.place(x=50, y=280)

janela.mainloop()