import mysql.connector
from SistemaCES.lib.interface import *
from SistemaCES.lib.arquivos import *
import getpass
from hashlib import sha256

arq_cli = mysql.connector.connect(host='localhost', database='clientes', user='root', password='')
arq_prod = mysql.connector.connect(host='localhost', database='produtos', user='root', password='')


def fazer_login(situacao=False):
    while situacao == False:
        nome = str(input('Digite seu nome de login: ')).strip()
        while nome == '':
            nome = str(input('Digite seu nome de login: ')).strip()

        senha = getpass.getpass('Digite sua senha: ').strip()
        while senha == '':
            senha = getpass.getpass('Digite sua senha: ').strip()
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
                    pass
            senhar = sha256(senha.encode()).hexdigest()
            cursor.execute(f"select senha from cadastrados where nome = '{nome}';")
            verifica_senha = cursor.fetchall()
            if verifica_senha[0][0] == senhar:
                situacao = True
                print(f'Bem vindo(a), {nome}!', situacao)
                return main_menu()        
            else:
                print('Senha incorreta')
                return menu_login()
        except:
            print(f'{nome} não existe ou está incorreto!')
            return menu_login()


def criar_login():
    nome = str(input('Crie seu nome de login desejado: '))
    senha = getpass.getpass('Crie sua senha: ')
    senha = sha256(senha.encode()).hexdigest()

    con = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user='root',
                                  password='')
    cursor = con.cursor()
    cursor.execute(f'insert into cadastrados values(default, "{nome}","{senha}");')
    print(f'{nome} cadastrado com sucesso!')
    con.close()
    cursor.close()
    return


def menu_login():
    while True:
        resp = menu(['Fazer login',
                     'Criar Usuário',
                     'Sair'])
        if resp == 1:
            return fazer_login()
        elif resp == 2:
            return criar_login()
        elif resp == 3:
            cabecalho('Saindo...')
            break

        else:
            print('\033[4;31mERRO! Digite uma opção válida!\033[m')


def main_menu():
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


def menu_cliente():
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


def menu_produto():
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
        sleep(2)


menu_login()
