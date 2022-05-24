from SistemaCES.lib.login import *
from SistemaCES.lib.interface import *
from SistemaCES.lib.arquivos import *

arq_cli = mysql.connector.connect(host='localhost', database='clientes', user='root', password='')
arq_prod = mysql.connector.connect(host='localhost', database='produtos', user='root', password='')


def menu_login():
    while True:
        resp = menu(['Fazer login', 'Criar Usuário', 'Sair'])
        if resp == 1:
            fazer_login()
            return main_menu()
        elif resp == 2:
            return criar_login()
        elif resp == 3:
            cabecalho('Saindo...')
            break
        else:
            print('\033[4;31mERRO! Digite uma opção válida!\033[m')


def main_menu():
    while True:
        resposta = menu(['Clientes', 'Produtos', 'Sair'])
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


def menu_cliente():
    while True:
        resposta = menu(['Listar clientes', 'Cadastrar clientes', 'Atualizar Cadastro', 'Deletar cadastro', 'Menu principal'])
        if resposta == 1:
            lerarquivo(arq_cli)
        elif resposta == 2:
            nome = str(input('Nome: '))
            nasc = str(input('Nascimento(YYYY/MM/DD): '))
            cadastrar(arq_cli, nome, nasc)
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


def menu_produto():
    while True:
        resposta = menu(['Produtos', 'Cadastrar produtos', 'Atualizar produtos', 'Deletar produto', 'Voltar'])
        if resposta == 1:
            lerarquivo_prod(arq_prod)
        elif resposta == 2:
            nome = str(input('Nome do produto: '))
            marca = str(input('Marca: '))
            descricao = str(input('Descrição: '))
            valor_compra = leiadinheiro('Valor de compra: ')
            valor_venda = leiadinheiro('Valor de venda: ')
            estoque = leiaint('Quantidade para adicionar ao estoque: ')
            cadastrar_prod(arq_prod, nome, marca, descricao, valor_compra, valor_venda, estoque)
        elif resposta == 3:
            atualiza = leiaint('Digite o código do produto que deseja atualizar: ')
            valor_compra = leiadinheiro('Valor de compra: ')
            valor_venda = leiadinheiro('Valor de venda: ')
            estoque = leiaint('Quantidade à somar ao estoque: ')
            atualizar_prod(arq_prod, atualiza, valor_compra, valor_venda, estoque)
        elif resposta == 4:
            delete = leiaint('Digite o ID do produto que deseja excluir: ')
            excluir_prod(arq_prod, delete)
        elif resposta == 5:
            main_menu()
            break
        else:
            print('\033[4;31mERRO! Digite uma opção válida!\033[m')
        sleep(2)


menu_login()
