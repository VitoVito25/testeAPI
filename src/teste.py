from database.Database import Database
from src.models.Usuario import Usuario
from flask import Flask, jsonify

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

    app = Flask(__name__)


    @app.route('/kaio')
    def kaio():
        return 'Kaiao bonilha'
    
    app.run(host='0.0.0.0')

    # Desconecta do banco de dados
    db.disconnect()

if __name__ == "__main__":
    main()
