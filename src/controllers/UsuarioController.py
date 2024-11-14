from flask import Blueprint, request, jsonify
from services.UsuarioService import UsuarioService

class UsuarioController:
    def __init__(self, db):
        self.db = db
        self.user_service = UsuarioService(db)
        self.usuario_bp = Blueprint('usuario', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        # Rota para criação de usuário
        self.usuario_bp.add_url_rule('/usuarios', 'create_user', self.create_user, methods=['POST'])
        
        # Rota para obter um usuário por ID
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'get_user', self.get_user, methods=['GET'])
        
        # Rota para atualização de usuário por ID
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'update_user', self.update_user, methods=['PUT'])
        
        # Rota para exclusão de usuário por ID
        self.usuario_bp.add_url_rule('/usuarios/<int:user_id>', 'delete_user', self.delete_user, methods=['DELETE'])

    def create_user(self):
        try:
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')
            papel = data.get('papel')

            self.user_service.create_user(nome, email, senha, papel)
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

    def update_user(self, user_id):
        try:
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')
            papel = data.get('papel')

            self.user_service.update_user(user_id, nome, email, senha, papel)
            return jsonify({"message": f"Usuário com ID {user_id} atualizado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar usuário: {str(e)}"}), 400

    def delete_user(self, user_id):
        try:
            self.user_service.delete_user(user_id)
            return jsonify({"message": f"Usuário com ID {user_id} deletado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar usuário: {str(e)}"}), 400
