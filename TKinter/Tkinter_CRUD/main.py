
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
janela.configure(background=co4)
janela.resizable(width=False, height=False)

#Divisão da tela
#Parte de cima label_cima
frame_cima = Frame(janela, width=300, height=50, bg=co9, relief="sunken")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=400, bg=co9, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=700, height=400, bg=co8, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

app_nome = Label(frame_cima, text="Minha Biblioteca",   anchor=NW, font=("Ivy 20 bold"), bg=co9, fg=co3, relief="flat")
app_nome.place(x=30, y=10)

#Parte de baixo label_baixo
#Nome do livro
l_nome = Label(frame_baixo, text="Nome do livro",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
l_nome.place(x=30, y=20)

l_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
l_entry.place(x=13, y=50)

#Nome do Autor
a_nome = Label(frame_baixo, text="Autor",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
a_nome.place(x=30, y=90)

a_entry = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
a_entry.place(x=13, y=110)

#Descrição do livro
descricao = Label(frame_baixo, text="Descrição",   anchor=NW, font=("Times 12 bold"), bg=co9, fg=co4, relief="flat")
descricao.place(x=30, y=150)

descricao = Entry(frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
descricao.place(x=13, y=180)




janela.mainloop()
