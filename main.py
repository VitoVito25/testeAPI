from Database_Folder.Database import Database
from Database_Folder.Usuario.Usuario import Usuario

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

    new_user = Usuario.get_by_id(db, 1)
    print(new_user)

    del_user = Usuario.get_by_id(db, 4)
    del_user.delete(db)



    # Desconecta do banco de dados
    db.disconnect()

if __name__ == "__main__":
    main()
