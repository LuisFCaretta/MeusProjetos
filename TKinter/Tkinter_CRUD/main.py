from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from arquivos.view import *
from tkinter import messagebox
from ttkthemes import ThemedTk

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


janela = ThemedTk(theme="yaru")
janela.title("Minha Biblioteca")
janela.geometry("1005x450")
janela.configure(background=co1)
janela.resizable(width=False, height=False)



#Divisão da tela
#Parte de cima label_cima
frame_cima = Frame(janela, width=300, height=50, relief="flat")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=400, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=1000, height=400, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

app_nome = Label(frame_cima, text="Minha Biblioteca", anchor=NW, font=("Ivy 20 bold"), fg=co3, relief="flat")
app_nome.place(x=30, y=10)

global tree

def inserir():
    nome = l_entry.get()
    desc = descricao_entry.get()
    di = data_entry_i.get()
    df = data_entry_f.get()

    lista = [nome, desc, di, df]

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

        btn_confirmar = Button(frame_baixo, command=update, text="Confirmar", width=10, font=("Times 10 bold"), bg=co2, fg=co1, relief="solid", overrelief="ridge")
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




#Parte de baixo label_baixo
#Nome do livro
l_nome = Label(frame_baixo, text="Nome do livro", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
l_nome.place(x=30, y=0)

l_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
l_entry.place(x=13, y=30)

#Descrição do livro
descricao = Label(frame_baixo, text="Descrição", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
descricao.place(x=30, y=70)

descricao_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
descricao_entry.place(x=13, y=100)

#Data de início e final
data_i = Label(frame_baixo, text="Início", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
data_i.place(x=30, y=140)
data_entry_i = DateEntry(frame_baixo, width=25,background="gray", foreground="white", borderwidth=2)
data_entry_i.place(x=13, y=170)

data_f = Label(frame_baixo, text="Final", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
data_f.place(x=30, y=220)
data_entry_f = DateEntry(frame_baixo, width=25, background="gray", foreground="white", borderwidth=2)
data_entry_f.place(x=13, y=250)

#Botões
btn_inserir = Button(frame_baixo, command=inserir, text="Inserir", width=10, font=("Times 10 bold"), bg=co2, fg=co1, relief="raised", overrelief="groove")
btn_inserir.place(x=13, y=340)

btn_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=10, font=("Times 10 bold"), bg=co6, fg=co1, relief="raised", overrelief="groove")
btn_atualizar.place(x=103, y=340)

btn_apagar = Button(frame_baixo, command=deletar, text="Apagar", width=10, font=("Times 10 bold"), bg=co7, fg=co1, relief="raised", overrelief="groove")
btn_apagar.place(x=193, y=340)

#Frame direita
#Dados BD

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

