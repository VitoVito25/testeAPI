import atexit
from flask import Flask
from database.Database import Database
from config import Config
from controllers.UsuarioController import UsuarioController
from controllers.EmpresaController import EmpresaController
from controllers.CategoriaPessoaController import CategoriaPessoaController
from controllers.PessoaController import PessoaController
from controllers.ContaController import ContaController
from controllers.UsuarioEmpresaController import UsuarioEmpresaController
from controllers.CategoriaMovimentacaoFinanceiraController import CategoriaMovimentacaoFinanceiraController
from controllers.MovimentacaoFinanceiraController import MovimentacaoFinanceiraController

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
        self.app.config.from_object(Config)

        # Inicializa o controlador de usuários e registra as rotas dentro do contexto da aplicação
        with self.app.app_context():
            usuario_controller = UsuarioController(self.db)
            self.app.register_blueprint(usuario_controller.usuario_bp)

            empresa_controller = EmpresaController(self.db)
            self.app.register_blueprint(empresa_controller.empresa_bp)

            categoria_pessoa_controller = CategoriaPessoaController(self.db)
            self.app.register_blueprint(categoria_pessoa_controller.categoria_pessoa_bp)

            pessoa_controller = PessoaController(self.db)
            self.app.register_blueprint(pessoa_controller.pessoa_bp)

            conta_controller = ContaController(self.db)
            self.app.register_blueprint(conta_controller.conta_bp)

            usuario_empresa_controller = UsuarioEmpresaController(self.db)
            self.app.register_blueprint(usuario_empresa_controller.usuario_empresa_bp)

            categoria_movimentacao_financeira_controller = CategoriaMovimentacaoFinanceiraController(self.db)
            self.app.register_blueprint(categoria_movimentacao_financeira_controller.categoria_movimentacao_financeira_bp)

            movimentacao_financeira_controller = MovimentacaoFinanceiraController(self.db)
            self.app.register_blueprint(movimentacao_financeira_controller.movimentacao_financeira_bp)

        # Registrar a desconexão do banco de dados ao final da execução
        atexit.register(lambda: self.db.disconnect())

    def run(self):
        if not self.app:
            raise Exception("App não foi inicializado. Chame o método `initialize` antes de rodar o servidor.")
        
        self.app.run(host='0.0.0.0', port=5000, debug=True) # lembrar de tirar o debug no momento de lançamento

def main():
    app = App()
    app.initialize()
    app.run()

if __name__ == "__main__":
    main()