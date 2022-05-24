from SistemaCES.utilidades.utilidadescev.dado import *
from time import sleep


def linha(tam=42):
    return f'\033[34m{"-"}\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[34m{txt.center(42)}\033[m')
    print(linha())


def menu(lista):
    cabecalho('SISTEMA V1.0')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[34mSua opção: \033[m')
    return opc


def leiaint(frase):
    while True:
        try:
            n = int(input(frase))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[4;31mO usuário preferiu cancelar o programa.\033[m')
            break
        else:
            return n
