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

comando = """INSERT INTO usuario (nome, email, senha, papel) 
            VALUES ('Maria Oliveira', 'maria.oliveira@example.com', 'senha456', 'admin')"""

cursor.execute(comando)
cursor.commit()
