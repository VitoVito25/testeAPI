import atexit
from flask import Flask
from controllers.UsuarioController import UsuarioController
from database.Database import Database

class App:
    def __init__(self):
        self.db = None
        self.app = None

    def initialize(self):
        # Define os parâmetros para conectar ao banco de dados
        self.db = Database(
            driver="PostgreSQL Unicode",
            server="PAT-1575",
            port="5432",
            database="organizeiTeste",
            user="postgres",
            password="masterkey"
        )

        # Tenta conectar ao banco de dados
        try:
            self.db.connect()
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            exit(1)

        # Inicializa o aplicativo Flask
        self.app = Flask(__name__)

        # Inicializa o controlador de usuários e registra as rotas
        usuario_controller = UsuarioController(self.db)
        self.app.register_blueprint(usuario_controller.usuario_bp)

        # Registrar a desconexão do banco de dados ao final da execução
        atexit.register(lambda: self.db.disconnect())

    def run(self):
        if not self.app:
            raise Exception("App não foi inicializado. Chame o método `initialize` antes de rodar o servidor.")
        
        self.app.run(host='0.0.0.0', port=5000, debug=True)


