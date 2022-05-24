import mysql.connector

from SistemaCES.lib.interface import *


def arquivoexiste():
    con = mysql.connector.connect(host='localhost', database='clientes', user='root', password='')
    if con.is_connected():
        print("Conectado ao banco de dados ", linha)
    cursor = con.cursor()
    cursor.close()
    con.close()


def lerarquivo(arq_cli):
    con = mysql.connector.connect(host='localhost', database='clientes', user='root', password='')
    if con.is_connected():
        cursor = con.cursor(buffered=True)
        cursor.execute("select database();")
        cursor.execute('select id, nome, nasc from pessoas;')
        print(f'{cursor.column_names[0]:<5}|{cursor.column_names[1]:<30}|{cursor.column_names[2]}')
        print('_' * 60)

        for row in cursor.fetchall():
            print(f'{row[0]:<5}{row[1]:<30}{row[2]}')

        if con.is_connected():
            cursor.close()
        con.close()


def cadastrar(nome, nasc):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="clientes"
    )
    cursor = connection.cursor()
    cursor.execute('use clientes;')
    cursor.execute('select nome, nasc from pessoas;')
    nomes = cursor.fetchall()
    try:
        sql = f'INSERT INTO pessoas (nome, nasc) ' \
              f'SELECT "{nome}", "{nasc}" FROM DUAL WHERE NOT EXISTS ' \
              f'(SELECT 1 FROM pessoas WHERE nome = "{nome}" AND nasc = "{nasc}") ' \
              f'LIMIT 1;'
        cursor.execute(sql)
        connection.commit()
        userid = cursor.lastrowid
        cursor.close()
        connection.close()

    except:
        print('Houve um erro ao escrever os dados;')

    else:
        print(f"\033[34mFoi cadastrado o novo usuário de nome: {nome}\033[m")


def atualizar(arq_cli, nome, nasc, atualiza):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="clientes"
    )
    cursor = connection.cursor()
    cursor.execute(f"UPDATE pessoas SET nome = '{nome}', nasc = '{nasc}' WHERE id = '{atualiza}';")
    connection.commit()
    recordsaffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsaffected, " registros alterados")


def excluir_contato(arq_cli, delete):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="clientes"
    )
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM pessoas WHERE id = {delete};")
    connection.commit()
    recordsaffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsaffected, " registros excluídos")


def lerarquivo_prod(arq_prod):
    con = mysql.connector.connect(host='localhost', database='produtos', user='root', password='')
    if con.is_connected():
        db_info = con.get_server_info()
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        cursor.execute('select id, nome, marca, valor_venda, estoque from prod_cadastrados order by nome;')
        print(
            f'{cursor.column_names[0]:<5}|{cursor.column_names[1]:<28}|{cursor.column_names[2]:<10}|{cursor.column_names[3]:<10}|{cursor.column_names[4]}')
        print('_' * 66)
        for row in cursor.fetchall():
            print(f'{row[0]:<5}{row[1]:<30}{row[2]:>8}{row[3]:>12}{row[4]:>10}')
        if con.is_connected():
            cursor.close()
        con.close()


def cadastrar_prod(arq_prod, nome, marca, descricao, valor_compra, valor_venda, estoque):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="produtos"
        )
        cursor = connection.cursor()
        sql = f"INSERT INTO prod_cadastrados VALUES" \
              f"(default,'{nome}','{marca}','{descricao}','{valor_compra}','{valor_venda}','{estoque}');"
        cursor.execute(sql)
        connection.commit()
        userid = cursor.lastrowid
        cursor.close()
        connection.close()
    except:
        print('Houve um erro ao escrever os dados;')

    else:
        print(f"\033[34mNovo produto de nome:", nome, "\033[m")


def atualizar_prod(arq_prod, atualiza, valor_compra, valor_venda, estoque):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="produtos"
    )
    cursor = connection.cursor()
    cursor.execute(f"UPDATE prod_cadastrados SET valor_compra = '{valor_compra}',"
                   f" valor_venda = '{valor_venda}',"
                   f" estoque = estoque + {estoque}"
                   f" WHERE id = '{atualiza}';")
    connection.commit()
    recordsaffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsaffected, " registros alterados")


def excluir_prod(arq_prod, delete):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="produtos"
    )
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM prod_cadastrados WHERE id = {delete};")
    connection.commit()
    recordsaffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsaffected, " registros excluídos")
