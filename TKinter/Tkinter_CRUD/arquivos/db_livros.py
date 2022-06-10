import mysql.connector
#Criar banco de dados

con = mysql.connector.connect(host='localhost', database='db_livros', user='root', password='', autocommit=True, use_unicode=True)
cursor = con.cursor(buffered=True)

cursor = con.cursor()
cursor.execute("CREATE TABLE meus_livros(id integer auto_increment primary key, nome text, autor text, descricao text);")