from flask import Blueprint, request, jsonify, current_app
from services.UsuarioEmpresaService import UsuarioEmpresaService
from middleware.auth import Auth

class UsuarioEmpresaController:
    def __init__(self, db):
        self.db = db
        self.usuario_empresa_service = UsuarioEmpresaService(db)
        self.usuario_empresa_bp = Blueprint('usuario_empresa', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.usuario_empresa_bp.add_url_rule('/usuario_empresas', 'create_usuario_empresa', self.create_usuario_empresa, methods=['POST'])
        self.usuario_empresa_bp.add_url_rule('/usuario_empresas/<int:usuario_empresa_id>', 'get_usuario_empresa', self.get_usuario_empresa, methods=['GET'])
        self.usuario_empresa_bp.add_url_rule('/usuario_empresas', 'list_usuario_empresas', self.list_usuario_empresas, methods=['GET']) 
        self.usuario_empresa_bp.add_url_rule('/usuario_empresas/<int:usuario_empresa_id>', 'update_usuario_empresa', self.update_usuario_empresa, methods=['PUT'])
        self.usuario_empresa_bp.add_url_rule('/usuario_empresas/<int:usuario_empresa_id>', 'delete_usuario_empresa', self.auth.token_required(self.delete_usuario_empresa), methods=['DELETE'])

    def create_usuario_empresa(self):
        try:
            data = request.json
            usuario_id = data.get('usuario_id')
            empresa_id = data.get('empresa_id')
            permissao = data.get('permissao')

            if not usuario_id or not empresa_id or not permissao:
                return jsonify({"error": "Os campos usuario_id, empresa_id e permissao são obrigatórios!"}), 400

            self.usuario_empresa_service.create_usuario_empresa(usuario_id, empresa_id, permissao)
            return jsonify({"message": "UsuarioEmpresa criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar usuario_empresa: {str(e)}"}), 400

    def get_usuario_empresa(self, usuario_empresa_id):
        try:
            usuario_empresa = self.usuario_empresa_service.get_usuario_empresa_by_id(usuario_empresa_id)
            if usuario_empresa:
                return jsonify({
                    "id": usuario_empresa.get_id(),
                    "usuario_id": usuario_empresa.get_usuario_id(),
                    "empresa_id": usuario_empresa.get_empresa_id(),
                    "permissao": usuario_empresa.get_permissao()
                }), 200
            return jsonify({"error": "UsuarioEmpresa não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar usuario_empresa: {str(e)}"}), 400
        
    def list_usuario_empresas(self):
        try:
            usuario_empresas = self.usuario_empresa_service.get_all_usuario_empresas() 
            usuario_empresas_data = [{
                "id": usuario_empresa.get_id(),
                "usuario_id": usuario_empresa.get_usuario_id(),
                "empresa_id": usuario_empresa.get_empresa_id(),
                "permissao": usuario_empresa.get_permissao()
            } for usuario_empresa in usuario_empresas]
            return jsonify(usuario_empresas_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar usuario_empresas: {str(e)}"}), 400

    def update_usuario_empresa(self, usuario_empresa_id):
        try:
            data = request.json
            usuario_id = data.get('usuario_id')
            empresa_id = data.get('empresa_id')
            permissao = data.get('permissao')

            if not usuario_id or not empresa_id or not permissao:
                return jsonify({"error": "Os campos usuario_id, empresa_id e permissao são obrigatórios!"}), 400

            self.usuario_empresa_service.update_usuario_empresa(usuario_empresa_id, usuario_id, empresa_id, permissao)
            return jsonify({"message": f"UsuarioEmpresa com ID {usuario_empresa_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar usuario_empresa: {str(e)}"}), 400

    def delete_usuario_empresa(self, usuario_empresa_id):
        try:
            self.usuario_empresa_service.delete_usuario_empresa(usuario_empresa_id)
            return jsonify({"message": f"UsuarioEmpresa com ID {usuario_empresa_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar usuario_empresa: {str(e)}"}), 400