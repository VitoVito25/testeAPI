from flask import Blueprint, request, jsonify, current_app
from services.EmpresaService import EmpresaService
from middleware.auth import Auth

class EmpresaController:
    def __init__(self, db):
        self.db = db
        self.empresa_service = EmpresaService(db)
        self.empresa_bp = Blueprint('empresa', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.empresa_bp.add_url_rule('/empresas', 'create_empresa', self.create_empresa, methods=['POST'])
        self.empresa_bp.add_url_rule('/empresas/<int:empresa_id>', 'get_empresa', self.get_empresa, methods=['GET'])
        self.empresa_bp.add_url_rule('/empresas', 'list_empresas', self.list_empresas, methods=['GET']) 
        self.empresa_bp.add_url_rule('/empresas/<int:empresa_id>', 'update_empresa', self.update_empresa, methods=['PUT'])
        self.empresa_bp.add_url_rule('/empresas/<int:empresa_id>', 'delete_empresa', self.auth.token_required(self.delete_empresa), methods=['DELETE'])

    def create_empresa(self):
        try:
            data = request.json
            nome = data.get('nome')
            cnpj = data.get('cnpj')

            if not nome or not cnpj:
                return jsonify({"error": "Todos os campos são obrigatórios!"}), 400

            self.empresa_service.create_empresa(nome, cnpj)
            return jsonify({"message": "Empresa criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar empresa: {str(e)}"}), 400

    def get_empresa(self, empresa_id):
        try:
            empresa = self.empresa_service.get_empresa_by_id(empresa_id)
            if empresa:
                return jsonify({"id": empresa.get_id(), "nome": empresa.get_nome(), "cnpj": empresa.get_cnpj()}), 200
            return jsonify({"error": "Empresa não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar empresa: {str(e)}"}), 400
        
    def list_empresas(self):
        try:
            empresas = self.empresa_service.get_all_empresas() 
            empresas_data = [{"id": empresa.get_id(), "nome": empresa.get_nome(), "cnpj": empresa.get_cnpj()} for empresa in empresas]
            return jsonify(empresas_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar empresas: {str(e)}"}), 400

    def update_empresa(self, empresa_id):
        try:
            data = request.json
            nome = data.get('nome')
            cnpj = data.get('cnpj')

            if not nome or not cnpj:
                return jsonify({"error": "Todos os campos são obrigatórios!"}), 400

            self.empresa_service.update_empresa(empresa_id, nome, cnpj)
            return jsonify({"message": f"Empresa com ID {empresa_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar empresa: {str(e)}"}), 400

    def delete_empresa(self, empresa_id):
        try:
            self.empresa_service.delete_empresa(empresa_id)
            return jsonify({"message": f"Empresa com ID {empresa_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar empresa: {str(e)}"}), 400