import mysql.connector
#Criar banco de dados

con = mysql.connector.connect(host='localhost', database="db_livros", user='root', password='', autocommit=True, use_unicode=True)

cursor = con.cursor(buffered=True)
cursor.execute("CREATE TABLE MeusLivros(id INTEGER PRIMARY KEY AUTO_INCREMENT, Nome text, Descricao text, DataInicio date, DataFinal date);")


