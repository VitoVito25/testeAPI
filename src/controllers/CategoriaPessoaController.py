from flask import Blueprint, request, jsonify, current_app
from services.CategoriaPessoaService import CategoriaPessoaService
from middleware.auth import Auth

class CategoriaPessoaController:
    def __init__(self, db):
        self.db = db
        self.categoria_pessoa_service = CategoriaPessoaService(db)
        self.categoria_pessoa_bp = Blueprint('categoria_pessoa', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.categoria_pessoa_bp.add_url_rule('/categorias_pessoa', 'create_categoria_pessoa', self.create_categoria_pessoa, methods=['POST'])
        self.categoria_pessoa_bp.add_url_rule('/categorias_pessoa/<int:categoria_pessoa_id>', 'get_categoria_pessoa', self.get_categoria_pessoa, methods=['GET'])
        self.categoria_pessoa_bp.add_url_rule('/categorias_pessoa', 'list_categorias_pessoa', self.list_categorias_pessoa, methods=['GET']) 
        self.categoria_pessoa_bp.add_url_rule('/categorias_pessoa/<int:categoria_pessoa_id>', 'update_categoria_pessoa', self.update_categoria_pessoa, methods=['PUT'])
        self.categoria_pessoa_bp.add_url_rule('/categorias_pessoa/<int:categoria_pessoa_id>', 'delete_categoria_pessoa', self.auth.token_required(self.delete_categoria_pessoa), methods=['DELETE'])

    def create_categoria_pessoa(self):
        try:
            data = request.json
            nome = data.get('nome')

            if not nome:
                return jsonify({"error": "O campo nome é obrigatório!"}), 400

            self.categoria_pessoa_service.create_categoria_pessoa(nome)
            return jsonify({"message": "CategoriaPessoa criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar categoria_pessoa: {str(e)}"}), 400

    def get_categoria_pessoa(self, categoria_pessoa_id):
        try:
            categoria_pessoa = self.categoria_pessoa_service.get_categoria_pessoa_by_id(categoria_pessoa_id)
            if categoria_pessoa:
                return jsonify({"id": categoria_pessoa.get_id(), "nome": categoria_pessoa.get_nome()}), 200
            return jsonify({"error": "CategoriaPessoa não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar categoria_pessoa: {str(e)}"}), 400
        
    def list_categorias_pessoa(self):
        try:
            categorias_pessoa = self.categoria_pessoa_service.get_all_categorias_pessoa() 
            categorias_pessoa_data = [{"id": categoria_pessoa.get_id(), "nome": categoria_pessoa.get_nome()} for categoria_pessoa in categorias_pessoa]
            return jsonify(categorias_pessoa_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar categorias_pessoa: {str(e)}"}), 400

    def update_categoria_pessoa(self, categoria_pessoa_id):
        try:
            data = request.json
            nome = data.get('nome')

            if not nome:
                return jsonify({"error": "O campo nome é obrigatório!"}), 400

            self.categoria_pessoa_service.update_categoria_pessoa(categoria_pessoa_id, nome)
            return jsonify({"message": f"CategoriaPessoa com ID {categoria_pessoa_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar categoria_pessoa: {str(e)}"}), 400

    def delete_categoria_pessoa(self, categoria_pessoa_id):
        try:
            self.categoria_pessoa_service.delete_categoria_pessoa(categoria_pessoa_id)
            return jsonify({"message": f"CategoriaPessoa com ID {categoria_pessoa_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar categoria_pessoa: {str(e)}"}), 400