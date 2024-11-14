from Database_Folder.Database import Database
from Database_Folder.Usuario import Usuario

def main():
    # Define os parametros para conectar ao banco de dados
    db = Database(
        driver="PostgreSQL Unicode",
        server="PAT-1575",
        port="5432",
        database="organizeiTeste",
        user="postgres",
        password="masterkey"
    )

    # Tenta conectar ao banco de dados
    db.connect()

    new_user = Usuario.get_by_id(db, 5)
    print(new_user)

    print(new_user.nome)


    # Desconecta do banco de dados
    db.disconnect()

if __name__ == "__main__":
    main()
