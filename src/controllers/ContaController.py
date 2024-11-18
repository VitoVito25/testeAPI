from flask import Blueprint, request, jsonify, current_app
from services.ContaService import ContaService
from middleware.auth import Auth

class ContaController:
    def __init__(self, db):
        self.db = db
        self.conta_service = ContaService(db)
        self.conta_bp = Blueprint('conta', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.conta_bp.add_url_rule('/contas', 'create_conta', self.create_conta, methods=['POST'])
        self.conta_bp.add_url_rule('/contas/<int:conta_id>', 'get_conta', self.get_conta, methods=['GET'])
        self.conta_bp.add_url_rule('/contas', 'list_contas', self.list_contas, methods=['GET']) 
        self.conta_bp.add_url_rule('/contas/<int:conta_id>', 'update_conta', self.update_conta, methods=['PUT'])
        self.conta_bp.add_url_rule('/contas/<int:conta_id>', 'delete_conta', self.auth.token_required(self.delete_conta), methods=['DELETE'])

    def create_conta(self):
        
        try:
            data = request.json
            nome = data.get('nome')
            descricao = data.get('descricao')
            saldo_inicial = data.get('saldo_inicial')
            empresa_id = data.get('empresa_id')

            if not nome or not empresa_id:
                return jsonify({"error": "Os campos nome e empresa_id são obrigatórios!"}), 400

            self.conta_service.create_conta(nome, descricao, saldo_inicial, empresa_id)
            return jsonify({"message": "Conta criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar conta: {str(e)}"}), 400

    def get_conta(self, conta_id):
        try:
            conta = self.conta_service.get_conta_by_id(conta_id)
            if conta:
                return jsonify({
                    "id": conta.get_id(),
                    "nome": conta.get_nome(),
                    "descricao": conta.get_descricao(),
                    "saldo_inicial": conta.get_saldo_inicial(),
                    "empresa_id": conta.get_empresa_id()
                }), 200
            return jsonify({"error": "Conta não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar conta: {str(e)}"}), 400
        
    def list_contas(self):
        try:
            contas = self.conta_service.get_all_contas() 
            contas_data = [{
                "id": conta.get_id(),
                "nome": conta.get_nome(),
                "descricao": conta.get_descricao(),
                "saldo_inicial": conta.get_saldo_inicial(),
                "empresa_id": conta.get_empresa_id()
            } for conta in contas]
            return jsonify(contas_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar contas: {str(e)}"}), 400

    def update_conta(self, conta_id):
        try:
            data = request.json
            nome = data.get('nome')
            descricao = data.get('descricao')
            saldo_inicial = data.get('saldo_inicial')
            empresa_id = data.get('empresa_id')

            if not nome or not empresa_id:
                return jsonify({"error": "Os campos nome e empresa_id são obrigatórios!"}), 400

            self.conta_service.update_conta(conta_id, nome, descricao, saldo_inicial, empresa_id)
            return jsonify({"message": f"Conta com ID {conta_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar conta: {str(e)}"}), 400

    def delete_conta(self, conta_id):
        try:
            self.conta_service.delete_conta(conta_id)
            return jsonify({"message": f"Conta com ID {conta_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar conta: {str(e)}"}), 400