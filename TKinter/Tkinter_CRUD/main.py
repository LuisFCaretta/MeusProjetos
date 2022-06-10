from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *

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

janela = Tk()
janela.title("Minha Biblioteca")
janela.geometry("1000x450")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

#Divisão da tela
#Parte de cima label_cima
frame_cima = Frame(janela, width=300, height=50, bg=co9, relief="sunken")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=400, bg=co9, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=1000, height=400, bg=co1, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

app_nome = Label(frame_cima, text="Minha Biblioteca",   anchor=NW, font=("Ivy 20 bold"), bg=co9, fg=co3, relief="flat")
app_nome.place(x=30, y=10)

#Parte de baixo label_baixo
#Nome do livro
l_nome = Label(frame_baixo, text="Nome do livro",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
l_nome.place(x=30, y=0)

l_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
l_entry.place(x=13, y=30)

#Nome do Autor
a_nome = Label(frame_baixo, text="Autor",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
a_nome.place(x=30, y=60)

a_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
a_entry.place(x=13, y=90)

#Descrição do livro
descricao = Label(frame_baixo, text="Descrição",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
descricao.place(x=30, y=130)

descricao = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
descricao.place(x=13, y=160)

#Data de início e final
data_i = Label(frame_baixo, text="Início", anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
data_i.place(x=30, y=200)
data_entry_i = DateEntry(frame_baixo, width=25,background="gray", foreground="white", borderwidth=2)
data_entry_i.place(x=13, y=230)

data_f = Label(frame_baixo, text="Final", anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
data_f.place(x=30, y=260)
data_entry_f = DateEntry(frame_baixo, width=25, background="gray", foreground="white", borderwidth=2)
data_entry_f.place(x=13, y=290)

#Botões
btn_inserir = Button(frame_baixo, text="Inserir", width=10, font=("Times 10 bold"), bg=co2, fg=co1, relief="solid", overrelief="ridge")
btn_inserir.place(x=13, y=340)

btn_atualizar = Button(frame_baixo, text="Atualizar", width=10, font=("Times 10 bold"), bg=co6, fg=co1, relief="solid", overrelief="ridge")
btn_atualizar.place(x=103, y=340)

btn_apagar = Button(frame_baixo, text="Apagar", width=10, font=("Times 10 bold"), bg=co7, fg=co1, relief="solid", overrelief="ridge")
btn_apagar.place(x=193, y=340)

#Frame direita
#Dados BD
lista = [["1", "Dracula", "livro sobre vampiro", "25-08-1998", "12-10-2020"]]

# lista para cabecario
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

janela.mainloop()
