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
