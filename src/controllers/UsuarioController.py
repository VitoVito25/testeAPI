from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, current_app
from services.UsuarioService import UsuarioService
from middleware.auth import Auth

class UsuarioController:
    def __init__(self, db):
        self.db = db
        self.user_service = UsuarioService(db)
        self.usuario_bp = Blueprint('usuario', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.usuario_bp.add_url_rule('/usuarios', 'create_user', self.create_user, methods=['POST'])
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'get_user', self.get_user, methods=['GET'])
        self.usuario_bp.add_url_rule('/usuarios', 'list_users', self.list_users, methods=['GET']) 
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'update_user', self.update_user, methods=['PUT'])
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'delete_user', self.auth.token_required(self.delete_user), methods=['DELETE'])
        self.usuario_bp.add_url_rule('/login', 'login', self.login, methods=['POST'])

    def create_user(self):
        try:
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')
            papel = data.get('papel')

            if not nome or not email or not senha or not papel:
                return jsonify({"error": "Todos os campos são obrigatórios!"}), 400

            # Criptografar a senha antes de salvar
            hashed_password = generate_password_hash(senha)

            self.user_service.create_user(nome, email, hashed_password, papel)
            return jsonify({"message": "Usuário criado com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar usuário: {str(e)}"}), 400

    def get_user(self, user_id):
        try:
            user = self.user_service.get_user_by_id(user_id)
            if user:
                return jsonify({"id": user.get_id(), "nome": user.get_nome(), "email": user.get_email(), "papel": user.get_papel()}), 200
            return jsonify({"error": "Usuário não encontrado"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar usuário: {str(e)}"}), 400
        
    def list_users(self):
        try:
            users = self.user_service.get_all_users() 
            users_data = [{"id": user.get_id(), "nome": user.get_nome(), "email": user.get_email(), "papel": user.get_papel()} for user in users]
            return jsonify(users_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar usuários: {str(e)}"}), 400

    def update_user(self, user_id):
        try:
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')
            papel = data.get('papel')

            if not nome or not email or not papel:
                return jsonify({"error": "Todos os campos são obrigatórios!"}), 400

            # Criptografar a senha antes de atualizar
            hashed_password = generate_password_hash(senha) if senha else None

            self.user_service.update_user(user_id, nome, email, hashed_password, papel)
            return jsonify({"message": f"Usuário com ID {user_id} atualizado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar usuário: {str(e)}"}), 400

    def delete_user(self, user_id):
        try:
            self.user_service.delete_user(user_id)
            return jsonify({"message": f"Usuário com ID {user_id} deletado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar usuário: {str(e)}"}), 400

    def login(self):

        try:
            data = request.json
            email = data.get('email')
            senha = data.get('senha')

            if not email or not senha:
                return jsonify({"error": "Email e senha são obrigatórios!"}), 400

            # Buscar o usuário pelo email
            user = self.user_service.get_user_by_email(email)
            if not user:
                return jsonify({"error": "Usuário não encontrado"}), 404

            # Validar a senha
            if check_password_hash(user.get_senha(), senha):
                # Gerar o token JWT
                token = self.auth.generate_jwt(user)  # Usando a instância de Auth para gerar o token

                return jsonify({
                    "message": "Login bem-sucedido",
                    "user": {
                        "id": user.get_id(),
                        "nome": user.get_nome(),
                        "email": user.get_email(),
                        "papel": user.get_papel()
                    },
                    "token": token  # Retorna o token JWT no corpo da resposta
                }), 200
            else:
                return jsonify({"error": "Senha incorreta"}), 401
        except Exception as e:
            return jsonify({"error": f"Erro ao realizar login: {str(e)}"}), 400