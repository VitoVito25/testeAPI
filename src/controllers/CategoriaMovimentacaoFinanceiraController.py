from flask import Blueprint, request, jsonify, current_app
from services.CategoriaMovimentacaoFinanceiraService import CategoriaMovimentacaoFinanceiraService
from middleware.auth import Auth

class CategoriaMovimentacaoFinanceiraController:
    def __init__(self, db):
        self.db = db
        self.categoria_movimentacao_financeira_service = CategoriaMovimentacaoFinanceiraService(db)
        self.categoria_movimentacao_financeira_bp = Blueprint('categoria_movimentacao_financeira', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.categoria_movimentacao_financeira_bp.add_url_rule('/categorias_movimentacao_financeira', 'create_categoria_movimentacao_financeira', self.create_categoria_movimentacao_financeira, methods=['POST'])
        self.categoria_movimentacao_financeira_bp.add_url_rule('/categorias_movimentacao_financeira/<int:categoria_movimentacao_financeira_id>', 'get_categoria_movimentacao_financeira', self.get_categoria_movimentacao_financeira, methods=['GET'])
        self.categoria_movimentacao_financeira_bp.add_url_rule('/categorias_movimentacao_financeira', 'list_categorias_movimentacao_financeira', self.list_categorias_movimentacao_financeira, methods=['GET']) 
        self.categoria_movimentacao_financeira_bp.add_url_rule('/categorias_movimentacao_financeira/<int:categoria_movimentacao_financeira_id>', 'update_categoria_movimentacao_financeira', self.update_categoria_movimentacao_financeira, methods=['PUT'])
        self.categoria_movimentacao_financeira_bp.add_url_rule('/categorias_movimentacao_financeira/<int:categoria_movimentacao_financeira_id>', 'delete_categoria_movimentacao_financeira', self.auth.token_required(self.delete_categoria_movimentacao_financeira), methods=['DELETE'])

    def create_categoria_movimentacao_financeira(self):
        try:
            data = request.json
            nome = data.get('nome')
            tipo = data.get('tipo')

            if not nome or not tipo:
                return jsonify({"error": "Os campos nome e tipo são obrigatórios!"}), 400

            self.categoria_movimentacao_financeira_service.create_categoria_movimentacao_financeira(nome, tipo)
            return jsonify({"message": "CategoriaMovimentacaoFinanceira criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar categoria_movimentacao_financeira: {str(e)}"}), 400

    def get_categoria_movimentacao_financeira(self, categoria_movimentacao_financeira_id):
        try:
            categoria_movimentacao_financeira = self.categoria_movimentacao_financeira_service.get_categoria_movimentacao_financeira_by_id(categoria_movimentacao_financeira_id)
            if categoria_movimentacao_financeira:
                return jsonify({
                    "id": categoria_movimentacao_financeira.get_id(),
                    "nome": categoria_movimentacao_financeira.get_nome(),
                    "tipo": categoria_movimentacao_financeira.get_tipo()
                }), 200
            return jsonify({"error": "CategoriaMovimentacaoFinanceira não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar categoria_movimentacao_financeira: {str(e)}"}), 400
        
    def list_categorias_movimentacao_financeira(self):
        try:
            categorias_movimentacao_financeira = self.categoria_movimentacao_financeira_service.get_all_categorias_movimentacao_financeira() 
            categorias_movimentacao_financeira_data = [{
                "id": categoria_movimentacao_financeira.get_id(),
                "nome": categoria_movimentacao_financeira.get_nome(),
                "tipo": categoria_movimentacao_financeira.get_tipo()
            } for categoria_movimentacao_financeira in categorias_movimentacao_financeira]
            return jsonify(categorias_movimentacao_financeira_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar categorias_movimentacao_financeira: {str(e)}"}), 400

    def update_categoria_movimentacao_financeira(self, categoria_movimentacao_financeira_id):
        try:
            data = request.json
            nome = data.get('nome')
            tipo = data.get('tipo')

            if not nome or not tipo:
                return jsonify({"error": "Os campos nome e tipo são obrigatórios!"}), 400

            self.categoria_movimentacao_financeira_service.update_categoria_movimentacao_financeira(categoria_movimentacao_financeira_id, nome, tipo)
            return jsonify({"message": f"CategoriaMovimentacaoFinanceira com ID {categoria_movimentacao_financeira_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar categoria_movimentacao_financeira: {str(e)}"}), 400

    def delete_categoria_movimentacao_financeira(self, categoria_movimentacao_financeira_id):
        try:
            self.categoria_movimentacao_financeira_service.delete_categoria_movimentacao_financeira(categoria_movimentacao_financeira_id)
            return jsonify({"message": f"CategoriaMovimentacaoFinanceira com ID {categoria_movimentacao_financeira_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar categoria_movimentacao_financeira: {str(e)}"}), 400