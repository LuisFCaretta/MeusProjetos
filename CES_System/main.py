from kivy.app import App
from kivy.lang import Builder
import mysql.connector
from hashlib import sha256

GUI = Builder.load_file("telalogin.kv")
GUI1 = Builder.load_file('mainmenu.kv')
arqlogin = mysql.connector.connect(host='localhost', database='clientes', user='root', password='')


class MainApp(App):
    def build(self):
        return GUI

    def login(self):
        while True:
            nome = self.root.ids.usuario.text
            while nome == '':
                self.root.ids.msg.text = 'O campo nome não pode ser vazio!'
                nome = self.root.ids.usuario.text

            senha = self.root.ids.senha.text
            while senha == '':
                self.root.ids.msg.text = 'O campo senha não pode ser vazio!'
                senha = self.root.ids.senha.text
                if senha != '':
                    pass
            con = mysql.connector.connect(host='localhost',
                                          database='cadastro',
                                          user='root',
                                          password='')
            cursor = con.cursor()
            cursor.execute(f"select nome from cadastrados where nome = '{nome}';")
            verifica_nome = cursor.fetchall()
            try:
                if verifica_nome[0][0] == nome:
                    senhar = sha256(senha.encode()).hexdigest()
                    cursor.execute(f"select senha from cadastrados where nome = '{nome}';")
                    verifica_senha = cursor.fetchall()
                    if verifica_senha[0][0] == senhar:
                        self.root.ids.msg.text = f'Bem vindo(a), {nome}!'
                        break
                    else:
                        return
            except:
                self.root.ids.msg.text = f'{nome} não existe ou está incorreto!'
                return
    def menu_cliente(self):
        pass


class MenuPrincipal(App):
    def build(self):
        return GUI1




    '''def main_menu(self):
        while True:
            resposta = menu(['Clientes',
                             'Produtos',
                             'Sair'])

            if resposta == 1:
                return menu_cliente()

            elif resposta == 2:
                return menu_produto()

            elif resposta == 3:
                cabecalho(f'\033[34m{"Saindo do sistema...Até breve!":^42}\033[m')
                break

            else:
                print('\033[4;31mERRO! Digite uma opção válida!\033[m')
            sleep(2)


    def menu_cliente(self):
        while True:
            resposta = menu(['Listar clientes',
                             'Cadastrar clientes',
                             'Atualizar Cadastro',
                             'Deletar cadastro',
                             'Menu principal'])

            if resposta == 1:
                lerarquivo(arq_cli)

            elif resposta == 2:
                nome = str(input('Nome: '))
                anasc = leiaint('Ano de Nascimento: ')
                mnasc = leiaint('Mês de Nascimento: ')
                dnasc = leiaint('Dia de Nascimento: ')

                nasc = f'{anasc}-{mnasc}-{dnasc}'
                cadastrar(nome, nasc)

            elif resposta == 3:
                atualiza = leiaint('\033[34mDigite o ID referente ao qual deseja atualizar: \033[m')
                nome = str(input('Nome: '))
                nasc = str(input('Nascimento(YYYY/MM/DD): '))
                atualizar(arq_cli, nome, nasc, atualiza)

            elif resposta == 4:
                delete = leiaint('\033[34mDigite o ID referente ao qual deseja excluir: \033[m')
                excluir_contato(arq_cli, delete)

            elif resposta == 5:
                main_menu()
                break

            else:
                print('\033[4;31mERRO! Digite uma opção válida!\033[m')
            sleep(2)


    def menu_produto(self):
        while True:
            resposta = menu(['Produtos',
                             'Cadastrar produtos',
                             'Atualizar produtos',
                             'Deletar produto',
                             'Voltar'])

            if resposta == 1:
                return lerarquivo_prod(arq_prod)

            elif resposta == 2:
                nome = str(input('Nome do produto: '))
                marca = str(input('Marca: '))
                descricao = str(input('Descrição: '))
                valor_compra = leiadinheiro('Valor de compra: ')
                valor_venda = leiadinheiro('Valor de venda: ')
                estoque = leiaint('Quantidade para adicionar ao estoque: ')
                return cadastrar_prod(arq_prod, nome, marca, descricao, valor_compra, valor_venda, estoque)

            elif resposta == 3:
                atualiza = leiaint('Digite o código do produto que deseja atualizar: ')
                valor_compra = leiadinheiro('Valor de compra: ')
                valor_venda = leiadinheiro('Valor de venda: ')
                estoque = leiaint('Quantidade à somar ao estoque: ')
                return atualizar_prod(arq_prod, atualiza, valor_compra, valor_venda, estoque)

            elif resposta == 4:
                delete = leiaint('Digite o ID do produto que deseja excluir: ')
                return excluir_prod(arq_prod, delete)

            elif resposta == 5:
                main_menu()
                break

            else:
                print('\033[4;31mERRO! Digite uma opção válida!\033[m')
            sleep(2)'''


MainApp().run()
