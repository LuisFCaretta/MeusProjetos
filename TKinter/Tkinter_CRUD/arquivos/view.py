import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_livros', user='root', password='', autocommit=True, use_unicode=True)


#inserir informações (CREATE)
def inserir_dados(i):
    cursor = con.cursor(buffered=True)
    cursor.execute('use db_livros;')
    
    query = "insert into MeusLivros values(default,%s,%s, STR_TO_DATE(%s, '%d-%m-%Y') , STR_TO_DATE(%s, '%d-%m-%Y'));"
    cursor.execute(query, i)

#ler informações(READ)
def mostrar_dados():
    lista = []
    cursor = con.cursor(buffered=True)
    ler_dados = 'select id, Nome, Descricao, DATE_FORMAT(DataInicio, "%d/%m/%Y") as DataInicio, DATE_FORMAT(DataFinal, "%d/%m/%Y") as DataFinal from MeusLivros;'
    cursor.execute(ler_dados)
    info = cursor.fetchall()

    for i in info:
        lista.append(i)
    return lista

#Editar informações(UPDATE)
def atualizar_dados(i):
    cursor = con.cursor(buffered=True)
    cursor.execute('use db_livros;')
    
    atualiza = "update MeusLivros set Nome=%s, Descricao=%s,  DataInicio=STR_TO_DATE(%s, '%d/%m/%Y'),  DataFinal=STR_TO_DATE(%s, '%d/%m/%Y') where id= %s;"
    cursor.execute(atualiza, i)

#Apagar dados(DELETE)
def apagar_dados(i):
    cursor = con.cursor(buffered=True)
    cursor.execute('use db_livros;')
    delete = f"delete from MeusLivros where id=%s;"
    cursor.execute(delete, i)

