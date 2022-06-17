from hashlib import sha256
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from arquivos.view import *
from tkinter import messagebox
import customtkinter

#Tabela de cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

class Application:
    def __init__(self, master=None):
        global janela
        global frame_baixo

        frame_cima = customtkinter.CTkFrame(janela, width=300, height=50, fg_color="#348feb", border=1)
        frame_cima.grid(row=0, column=0)
        frame_baixo = customtkinter.CTkFrame(janela, width=300, height=350, relief="flat", border=1)
        frame_baixo.grid(row=1, column=0, padx=0, pady=1)

        btn_login = customtkinter.CTkButton(frame_baixo, text="Login", text_font=("Arial 24 bold"), width=200, fg_color="#348feb", height=10, command=tela_de_login)
        btn_login.place(x=50, y=100)

        btn_cadastrar = customtkinter.CTkButton(frame_baixo, text="Cadastrar", width=200, fg_color="#348feb", text_font=("Arial 24 bold"), height=10, command=tela_de_cadastro)
        btn_cadastrar.place(x=50, y=200)
 
def tela_principal():
    global janela
    janela.destroy()
    janela = customtkinter.CTk()
    customtkinter.set_default_color_theme("dark-blue")
    janela.title("Minha Biblioteca")
    label = customtkinter.CTkLabel(janela)
    label.place()
    janela.geometry("1000x450")
    janela.resizable(width=False, height=False)
 

    frame_cima = customtkinter.CTkFrame(janela, width=300, height=50, relief="flat")
    frame_cima.grid(row=0, column=0)

    frame_baixo = customtkinter.CTkFrame(janela, width=300, height=400, relief="flat")
    frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

    frame_direita = customtkinter.CTkFrame(janela, width=1000, bg_color="black", height=400, relief="flat")
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

    app_nome = customtkinter.CTkLabel(frame_cima, text="Minha Biblioteca", anchor=NW, text_font=("Ivy 20 bold"), fg=co3, relief="flat")
    app_nome.place(x=30, y=10)

    global tree

    def inserir():
        nome = l_entry.get()
        desc = descricao_entry.get()
        di = data_entry_i.get()
        df = data_entry_f.get()

        lista = [nome, desc, di.replace("/", "-"), df.replace("/", "-")]

        if nome == "":
            messagebox.showerror('Erro!', 'Os dados não podem ser vazios!')
        else:
            inserir_dados(lista)   
            messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso!') 

            l_entry.delete(0, "end")
            descricao_entry.delete(0, "end")
            data_entry_i.delete(0, "end")
            data_entry_f.delete(0, "end")

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    def atualizar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            l_entry.delete(0, "end")
            descricao_entry.delete(0, "end")
            data_entry_i.delete(0, "end")
            data_entry_f.delete(0, "end")

            l_entry.insert(0, tree_lista[1])
            descricao_entry.insert(0, tree_lista[2])
            data_entry_i.insert(0, tree_lista[3])
            data_entry_f.insert(0, tree_lista[4])

            def update():
                nome = l_entry.get()
                desc = descricao_entry.get()
                di = data_entry_i.get()
                df = data_entry_f.get()

                lista = [nome, desc, di, df, valor_id]

                if nome == "":
                    messagebox.showerror('Erro!', 'Os dados não podem ser vazios!')
                else:
                    atualizar_dados(lista)   
                    messagebox.showinfo('Sucesso!', 'Dados atualizados com sucesso!') 

                    l_entry.delete(0, "end")
                    descricao_entry.delete(0, "end")
                    data_entry_i.delete(0, "end")
                    data_entry_f.delete(0, "end")

                for widget in frame_direita.winfo_children():
                    widget.destroy()

                mostrar()

            btn_confirmar = customtkinter.CTkButton(frame_baixo, command=update, text="Confirmar", width=10, fg_color="green", text_font=("Times 10 bold"))
            btn_confirmar.place(x=102, y=370)

        except:
            messagebox.showerror('Erro!', 'Selecione um dos dados da tabela!')

    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            apagar_dados(valor_id)
            messagebox.showinfo('Sucesso!', 'Dados apagados com sucesso!')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        except:
            messagebox.showerror('Erro!', 'Selecione um dos dados da tabela!')


    l_nome = customtkinter.CTkLabel(frame_baixo, text="Nome do livro", anchor=NW, text_font=("Times 12 bold"), fg=co4)
    l_nome.place(x=0, y=0)

    l_entry = customtkinter.CTkEntry(frame_baixo, width=260, text_font=("Times 16 bold"), justify="left")
    l_entry.place(x=13, y=30)

    #Descrição do livro
    descricao = customtkinter.CTkLabel(frame_baixo, text="Descrição", anchor=NW, text_font=("Times 12 bold"), fg=co4)
    descricao.place(x=-15, y=70)

    descricao_entry = customtkinter.CTkEntry(frame_baixo, width=260, text_font=("Times 16 bold"), justify="left")
    descricao_entry.place(x=13, y=100)

    #Data de início e final
    data_i = customtkinter.CTkLabel(frame_baixo, text="Início", anchor=NW, text_font=("Times 12 bold"), fg=co4)
    data_i.place(x=-30, y=140)
    data_entry_i = DateEntry(frame_baixo, width=25, background="gray", foreground="white", borderwidth=2)
    data_entry_i.place(x=13, y=170)

    data_f = customtkinter.CTkLabel(frame_baixo, text="Final", width=260, anchor=NW, text_font=("Times 12 bold"), fg=co4)
    data_f.place(x=-90, y=220)
    data_entry_f = DateEntry(frame_baixo, width=25, background="gray", foreground="white", borderwidth=2)
    data_entry_f.place(x=13, y=250)

    #Botões
    btn_inserir = customtkinter.CTkButton(frame_baixo, command=inserir, text="Inserir", width=10, fg_color="green", text_font=("Times 10 bold"))
    btn_inserir.place(x=13, y=340)

    btn_atualizar = customtkinter.CTkButton(frame_baixo, command=atualizar, text="Atualizar", width=10, text_font=("Times 8 bold"))
    btn_atualizar.place(x=103, y=340)

    btn_apagar = customtkinter.CTkButton(frame_baixo, command=deletar, fg_color="#ef5350", text="Apagar", width=10, text_font=("Times 10 bold"))
    btn_apagar.place(x=203, y=340)

    def mostrar():
        global tree
        lista = mostrar_dados()
        #Cabeçalho
        tabela_head = ["Id", "Nome do livro", "Descrição", "Início", "Final"]

        # criando a tabela
        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")
        
        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        frame_direita.grid_rowconfigure(0, weight=12)


        hd=["nw","nw", "nw", "center","center"]
        h=[30, 170, 260, 100, 120]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            
            n+=1

        for item in lista:
            tree.insert('', 'end', values=item)

    mostrar()
    janela.mainloop()

def tela_de_login():
    global janela
    janela.destroy()
    janela = customtkinter.CTkToplevel()
    customtkinter.set_default_color_theme("dark-blue")
    janela.deiconify()
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
        global janela
        email = email_entry.get()
        senha = senha_entry.get()
        senha = sha256(senha.encode()).hexdigest()
        if email == "" or senha == "":
            messagebox.showerror('Erro!', 'Os campos não podem ser vazios!')
            return
        ver = [email, senha]
        con = mysql.connector.connect(host='localhost', database='db_user_admin', user='root', password='', autocommit=True, use_unicode=True)
        cursor = con.cursor(buffered=True)
        cursor.execute("select email_admin, senha_admin, nome_admin from admin")
        verifica = cursor.fetchall()

        for admin in verifica:
            if admin[0] == ver[0] and admin[1] == ver[1]:
                messagebox.showinfo('Sucesso!', f'Seja bem vindo(a), {admin[2]}!')
                tela_principal()
                janela.destroy()
                
            if admin[0] == ver[0] and admin[1] != ver[1]:
                messagebox.showerror("Erro", "Senha incorreta, verifique e tente novamente!")
                return
            if admin[0] != ver[0] and admin[1] == ver[1]:
                messagebox.showerror("Erro", "Email incorreto, verifique e tente novamente!")
                return

    btn_login = customtkinter.CTkButton(frame_baixo, text="Login", text_font=("Arial 24 bold"), width=200, fg_color="#348feb", height=10, command=verifica_login)
    btn_login.place(x=50, y=200)

def tela_de_cadastro():
    global frame_baixo
    global janela
    janela.destroy()
    janela = customtkinter.CTkToplevel()
    customtkinter.set_default_color_theme("dark-blue")
    janela.deiconify()
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

    def executar_cadastro():
        nome = l_nome_entry.get()
        email = email_entry.get()
        senha = senha_entry.get()
        senha2 = senha2_entry.get()

        if nome == "" or email == "" or senha == "" or senha2 == "":
            messagebox.showerror('Erro!', 'Os campos não podem ser vazios!')
            return
        if senha != senha2:
            messagebox.showerror('Erro!', 'As senhas devem ser iguais, tente novamente.')
            return
        
        senha = sha256(senha.encode()).hexdigest()
        novo = [nome, email, senha]
        
        con = mysql.connector.connect(host='localhost', database='db_user_admin', user='root', password='', autocommit=True, use_unicode=True)
        cursor = con.cursor(buffered=True)
        cursor.execute("use db_user_admin;")
        cursor.execute("select * from admin;")
        verifica = cursor.fetchall()
        for admin in verifica:
            if novo[1] == admin[2]:
                messagebox.showwarning('Erro!', f'Já existe o email {admin[2]} no nosso sistema!')
                return
            if novo[1] != admin[2]:
                pass
        cursor.execute(f"INSERT IGNORE INTO admin VALUES(default, '{novo[0]}', '{novo[1]}', '{novo[2]}');")
        messagebox.showinfo('Parabéns!', f'Cadastro realizado com sucesso, {novo[0]}!\nRedirecionando para login.')
        tela_de_login()

    btn_cadastrar = customtkinter.CTkButton(frame_baixo, text="Cadastrar", fg_color="#348feb", text_font=("Arial 24 bold"), width=200, height=10, command=executar_cadastro)
    btn_cadastrar.place(x=50, y=340)


if __name__ == "__main__":
    janela = customtkinter.CTk()
    janela.title("Minha biblioteca login")
    label = customtkinter.CTkLabel(janela)
    customtkinter.set_default_color_theme(("dark-blue"))  # Themes: "blue" (standard), "green", "dark-blue"
    label.place()
    janela.geometry("300x400")
    Application(janela)
    janela.resizable(width=False, height=False)
    janela.mainloop()
    