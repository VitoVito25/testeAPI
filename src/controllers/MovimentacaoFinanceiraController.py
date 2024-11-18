from flask import Blueprint, request, jsonify, current_app
from services.MovimentacaoFinanceiraService import MovimentacaoFinanceiraService
from middleware.auth import Auth

class MovimentacaoFinanceiraController:
    def __init__(self, db):
        self.db = db
        self.movimentacao_financeira_service = MovimentacaoFinanceiraService(db)
        self.movimentacao_financeira_bp = Blueprint('movimentacao_financeira', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.movimentacao_financeira_bp.add_url_rule('/movimentacoes_financeiras', 'create_movimentacao_financeira', self.create_movimentacao_financeira, methods=['POST'])
        self.movimentacao_financeira_bp.add_url_rule('/movimentacoes_financeiras/<int:movimentacao_financeira_id>', 'get_movimentacao_financeira', self.get_movimentacao_financeira, methods=['GET'])
        self.movimentacao_financeira_bp.add_url_rule('/movimentacoes_financeiras', 'list_movimentacoes_financeiras', self.list_movimentacoes_financeiras, methods=['GET']) 
        self.movimentacao_financeira_bp.add_url_rule('/movimentacoes_financeiras/<int:movimentacao_financeira_id>', 'update_movimentacao_financeira', self.update_movimentacao_financeira, methods=['PUT'])
        self.movimentacao_financeira_bp.add_url_rule('/movimentacoes_financeiras/<int:movimentacao_financeira_id>', 'delete_movimentacao_financeira', self.auth.token_required(self.delete_movimentacao_financeira), methods=['DELETE'])

    def create_movimentacao_financeira(self):
        try:
            data = request.json
            conta_id = data.get('conta_id')
            categoria_movimentacao_financeira_id = data.get('categoria_movimentacao_financeira_id')
            valor = data.get('valor')
            descricao = data.get('descricao')
            beneficiario_origem_id = data.get('beneficiario_origem_id')
            tipo_movimentacao = data.get('tipo_movimentacao')
            data_movimentacao = data.get('data_movimentacao')

            if not conta_id or not categoria_movimentacao_financeira_id or not valor or not tipo_movimentacao or not data_movimentacao:
                return jsonify({"error": "Os campos conta_id, categoria_movimentacao_financeira_id, valor, tipo_movimentacao e data_movimentacao são obrigatórios!"}), 400

            self.movimentacao_financeira_service.create_movimentacao_financeira(conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao)
            return jsonify({"message": "MovimentacaoFinanceira criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar movimentacao_financeira: {str(e)}"}), 400

    def get_movimentacao_financeira(self, movimentacao_financeira_id):
        try:
            movimentacao_financeira = self.movimentacao_financeira_service.get_movimentacao_financeira_by_id(movimentacao_financeira_id)
            if movimentacao_financeira:
                return jsonify({
                    "id": movimentacao_financeira.get_id(),
                    "conta_id": movimentacao_financeira.get_conta_id(),
                    "categoria_movimentacao_financeira_id": movimentacao_financeira.get_categoria_movimentacao_financeira_id(),
                    "valor": movimentacao_financeira.get_valor(),
                    "descricao": movimentacao_financeira.get_descricao(),
                    "beneficiario_origem_id": movimentacao_financeira.get_beneficiario_origem_id(),
                    "tipo_movimentacao": movimentacao_financeira.get_tipo_movimentacao(),
                    "data_movimentacao": movimentacao_financeira.get_data_movimentacao()
                }), 200
            return jsonify({"error": "MovimentacaoFinanceira não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar movimentacao_financeira: {str(e)}"}), 400
        
    def list_movimentacoes_financeiras(self):
        try:
            movimentacoes_financeiras = self.movimentacao_financeira_service.get_all_movimentacoes_financeiras() 
            movimentacoes_financeiras_data = [{
                "id": movimentacao_financeira.get_id(),
                "conta_id": movimentacao_financeira.get_conta_id(),
                "categoria_movimentacao_financeira_id": movimentacao_financeira.get_categoria_movimentacao_financeira_id(),
                "valor": movimentacao_financeira.get_valor(),
                "descricao": movimentacao_financeira.get_descricao(),
                "beneficiario_origem_id": movimentacao_financeira.get_beneficiario_origem_id(),
                "tipo_movimentacao": movimentacao_financeira.get_tipo_movimentacao(),
                "data_movimentacao": movimentacao_financeira.get_data_movimentacao()
            } for movimentacao_financeira in movimentacoes_financeiras]
            return jsonify(movimentacoes_financeiras_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar movimentacoes_financeiras: {str(e)}"}), 400

    def update_movimentacao_financeira(self, movimentacao_financeira_id):
        try:
            data = request.json
            conta_id = data.get('conta_id')
            categoria_movimentacao_financeira_id = data.get('categoria_movimentacao_financeira_id')
            valor = data.get('valor')
            descricao = data.get('descricao')
            beneficiario_origem_id = data.get('beneficiario_origem_id')
            tipo_movimentacao = data.get('tipo_movimentacao')
            data_movimentacao = data.get('data_movimentacao')

            if not conta_id or not categoria_movimentacao_financeira_id or not valor or not tipo_movimentacao or not data_movimentacao:
                return jsonify({"error": "Os campos conta_id, categoria_movimentacao_financeira_id, valor, tipo_movimentacao e data_movimentacao são obrigatórios!"}), 400

            self.movimentacao_financeira_service.update_movimentacao_financeira(movimentacao_financeira_id, conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao)
            return jsonify({"message": f"MovimentacaoFinanceira com ID {movimentacao_financeira_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar movimentacao_financeira: {str(e)}"}), 400

    def delete_movimentacao_financeira(self, movimentacao_financeira_id):
        try:
            self.movimentacao_financeira_service.delete_movimentacao_financeira(movimentacao_financeira_id)
            return jsonify({"message": f"MovimentacaoFinanceira com ID {movimentacao_financeira_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar movimentacao_financeira: {str(e)}"}), 400