import tkinter as t
import functools


class Tela(t.Frame):
    def __init__(self, parent, nome):
        t.Frame.__init__(self, parent)
        self.nome = nome
        t.Label(self, text='Voce esta na ' + self.nome).pack()

class Menu(t.Frame):
    def __init__(self, parent, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self
        for subtela in subtelas:
            t.Button(subtela, text='Voltar',
                command=functools.partial(self.muda_tela, self)).pack()
            t.Button(self, text=subtela.nome, 
                command=functools.partial(self.muda_tela, subtela)).pack()

    def muda_tela(self, qual):
        self.current_frame.pack_forget()
        qual.pack()
        self.current_frame = qual

if __name__ == '__main__':
    root = t.Tk()
    root.resizable(0, 0)
    t1 = Tela(root, 'Primeira tela')
    t2 = Tela(root, 'Segunda tela')
    t3 = Tela(root, 'Terceira tela')    

    m = Menu(root, t1, t2, t3)
    m.pack()

    root.mainloop()