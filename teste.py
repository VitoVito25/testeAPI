import pyodbc

connection_data = (
    "Driver={PostgreSQL Unicode};"
    "Server=PAT-1575;Port=5432;"
    "Database=organizeiTeste;"
)

connection = pyodbc.connect(connection_data)
print("Conexão Bem Sucedida")
