import pyodbc

connection_data = (
    "Driver={PostgreSQL Unicode};"
    "Server=PAT-1575;Port=5432;"
    "Database=organizeiTeste;"
    "Uid=postgres;"
    "Pwd=masterkey;"
)

connection = pyodbc.connect(connection_data)
print("Conexão Bem Sucedida")

cursor = connection.cursor()

cursor.close()
connection.close()


#CREATE
#comando = """INSERT INTO usuario (nome, email, senha, papel) 
#            VALUES ('Maria Oliveira', 'maria.oliveira@e.com', 'senha456', 'admin')"""
#cursor.commit()


comando = "SELECT * FROM usuario"
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado [1] [2])