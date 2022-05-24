def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[4;31mERRO! \"{entrada}\" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(frase):
    while True:
        try:
            frase
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[4;31mO usuário preferiu cancelar o programa.\033[m')
            return 0



def leiafloat(frase):
    while True:
        try:
            r = float(input(frase))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[4;31mO usuário preferiu cancelar o programa.\033[m')
            return 0
        else:
            return r

