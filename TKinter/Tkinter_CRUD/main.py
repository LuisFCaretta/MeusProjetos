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

class Application:
    def __init__(self, master=None):
        self.frame_cima = Frame(root, width=300, height=50, relief="flat")
        self.frame_cima.grid(row=0, column=0)

        self.frame_baixo = Frame(root, width=300, height=400, relief="flat")
        self.frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

        self.frame_direita = Frame(root, width=1000, height=400, relief="flat")
        self.frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0,sticky=NSEW)

        self.app_nome = Label(self.frame_cima, text="Minha Biblioteca", anchor=NW, font=("Ivy 20 bold"), fg=co3, relief="flat")
        self.app_nome.place(x=30, y=10)

        global tree

        def inserir():
            self.nome = self.l_entry.get()
            self.desc = self.descricao_entry.get()
            self.di = self.data_entry_i.get()
            self.df = self.data_entry_f.get()

            lista = [self.nome, self.desc, self.di, self.df]

            if self.nome == "":
                messagebox.showerror('Erro!', 'Os dados não podem ser vazios!')
            else:
                inserir_dados(lista)   
                messagebox.showinfo('Sucesso!', 'Dados inseridos com sucesso!') 

                self.l_entry.delete(0, "end")
                self.descricao_entry.delete(0, "end")
                self.data_entry_i.delete(0, "end")
                self.data_entry_f.delete(0, "end")

            for widget in self.frame_direita.winfo_children():
                widget.destroy()

            mostrar()
    
        def atualizar():
            try:
                self.treev_dados = tree.focus()
                self.treev_dicionario = tree.item(self.treev_dados)
                self.tree_lista = self.treev_dicionario['values']

                self.valor_id = self.tree_lista[0]

                self.l_entry.delete(0, "end")
                self.descricao_entry.delete(0, "end")
                self.data_entry_i.delete(0, "end")
                self.data_entry_f.delete(0, "end")

                self.l_entry.insert(0, self.tree_lista[1])
                self.descricao_entry.insert(0, self.tree_lista[2])
                self.data_entry_i.insert(0, self.tree_lista[3])
                self.data_entry_f.insert(0, self.tree_lista[4])

                def update():
                    self.nome = self.l_entry.get()
                    self.desc = self.descricao_entry.get()
                    self.di = self.data_entry_i.get()
                    self.df = self.data_entry_f.get()

                    lista = [self.nome, self.desc, self.di, self.df, self.valor_id]

                    if self.nome == "":
                        messagebox.showerror('Erro!', 'Os dados não podem ser vazios!')
                    else:
                        atualizar_dados(lista)   
                        messagebox.showinfo('Sucesso!', 'Dados atualizados com sucesso!') 

                        self.l_entry.delete(0, "end")
                        self.descricao_entry.delete(0, "end")
                        self.data_entry_i.delete(0, "end")
                        self.data_entry_f.delete(0, "end")

                    for widget in self.frame_direita.winfo_children():
                        widget.destroy()

                    mostrar()

                btn_confirmar = Button(self.frame_baixo, command=update, text="Confirmar", width=10, font=("Times 10 bold"), bg=co2, fg=co1, relief="solid", overrelief="ridge")
                btn_confirmar.place(x=102, y=370)
                

            except:
                messagebox.showerror('Erro!', 'Selecione um dos dados da tabela!')

        def deletar():
            try:
                self.treev_dados = tree.focus()
                self.treev_dicionario = tree.item(self.treev_dados)
                self.tree_lista = self.treev_dicionario['values']

                self.valor_id = [self.tree_lista[0]]

                apagar_dados(self.valor_id)
                messagebox.showinfo('Sucesso!', 'Dados apagados com sucesso!')

                for widget in self.frame_direita.winfo_children():
                    widget.destroy()

                mostrar()

            except:
                messagebox.showerror('Erro!', 'Selecione um dos dados da tabela!')


        self.l_nome = Label(self.frame_baixo, text="Nome do livro", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
        self.l_nome.place(x=30, y=0)

        self.l_entry = Entry(self.frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
        self.l_entry.place(x=13, y=30)

        #Descrição do livro
        self.descricao = Label(self.frame_baixo, text="Descrição", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
        self.descricao.place(x=30, y=70)

        self.descricao_entry = Entry(self.frame_baixo, width=25, font=("Times 16 bold"), justify="left", relief="solid")
        self.descricao_entry.place(x=13, y=100)

        #Data de início e final
        self.data_i = Label(self.frame_baixo, text="Início", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
        self.data_i.place(x=30, y=140)
        self.data_entry_i = DateEntry(self.frame_baixo, width=25,background="gray", foreground="white", borderwidth=2)
        self.data_entry_i.place(x=13, y=170)

        self.data_f = Label(self.frame_baixo, text="Final", anchor=NW, font=("Times 12 bold"), fg=co4, relief="flat")
        self.data_f.place(x=30, y=220)
        self.data_entry_f = DateEntry(self.frame_baixo, width=25, background="gray", foreground="white", borderwidth=2)
        self.data_entry_f.place(x=13, y=250)

        #Botões
        self.btn_inserir = Button(self.frame_baixo, command=inserir, text="Inserir", width=10, font=("Times 10 bold"), bg=co2, fg=co1, relief="raised", overrelief="groove")
        self.btn_inserir.place(x=13, y=340)

        self.btn_atualizar = Button(self.frame_baixo, command=atualizar, text="Atualizar", width=10, font=("Times 10 bold"), bg=co6, fg=co1, relief="raised", overrelief="groove")
        self.btn_atualizar.place(x=103, y=340)

        self.btn_apagar = Button(self.frame_baixo, command=deletar, text="Apagar", width=10, font=("Times 10 bold"), bg=co7, fg=co1, relief="raised", overrelief="groove")
        self.btn_apagar.place(x=193, y=340)

        def mostrar():
            global tree
            self.lista = mostrar_dados()
            #Cabeçalho
            tabela_head = ["Id", "Nome do livro", "Descrição", "Início", "Final"]


            # criando a tabela
            tree = ttk.Treeview(self.frame_direita, selectmode="extended", columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(self.frame_direita, orient="vertical", command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar( self.frame_direita, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            self.frame_direita.grid_rowconfigure(0, weight=12)


            hd=["nw","nw", "nw", "center","center"]
            h=[30, 170, 260, 100, 120]
            n=0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the column's width to the header string
                tree.column(col, width=h[n],anchor=hd[n])
                
                n+=1

            for item in self.lista:
                tree.insert('', 'end', values=item)

        mostrar()

root = ThemedTk(theme="black")
root.title("Minha Biblioteca")
root.geometry("1005x450")
root.resizable(width=False, height=False)
Application(root)
root.mainloop()
