import mysql.connector


def fazer_login(situacao=False):
    nome = str(input('Digite seu nome de login: ')).strip()
    while nome == '':
        nome = str(input('Digite seu nome de login: ')).strip()

    senha = str(input('Digite sua senha: ')).strip()
    while senha == '':
        senha = str(input('Digite sua senha: ')).strip()

    global l
    con = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user='root',
                                  password='')
    cursor = con.cursor()
    cursor.execute('select nome, senha from cadastrados;')
    for l in cursor.fetchall():
        if nome == l[0]:
            if senha == l[1]:
                print(f'Bem vindo(a), {nome}!')
                situacao = True
                return situacao
            cursor.close()
            con.close()
    else:
        print('Nome de usuário e/ou senha incorretos!')
        return fazer_login()


def criar_login():
    nome = str(input('Crie seu nome de login desejado: '))
    senha = str(input('Crie sua senha: '))
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
