from flask import Blueprint, request, jsonify, current_app
from services.PessoaService import PessoaService
from middleware.auth import Auth

class PessoaController:
    def __init__(self, db):
        self.db = db
        self.pessoa_service = PessoaService(db)
        self.pessoa_bp = Blueprint('pessoa', __name__)

        # Definir as rotas
        self._add_routes()

    def _add_routes(self):
        self.auth = Auth(current_app.config['SECRET_KEY'])  # Inicialize o Auth

        self.pessoa_bp.add_url_rule('/pessoas', 'create_pessoa', self.create_pessoa, methods=['POST'])
        self.pessoa_bp.add_url_rule('/pessoas/<int:pessoa_id>', 'get_pessoa', self.get_pessoa, methods=['GET'])
        self.pessoa_bp.add_url_rule('/pessoas', 'list_pessoas', self.list_pessoas, methods=['GET']) 
        self.pessoa_bp.add_url_rule('/pessoas/<int:pessoa_id>', 'update_pessoa', self.update_pessoa, methods=['PUT'])
        self.pessoa_bp.add_url_rule('/pessoas/<int:pessoa_id>', 'delete_pessoa', self.auth.token_required(self.delete_pessoa), methods=['DELETE'])

    def create_pessoa(self):
        try:
            data = request.json
            nome = data.get('nome')
            cpf_cnpj = data.get('cpf_cnpj')
            categoria_pessoa_id = data.get('categoria_pessoa_id')
            cep = data.get('cep')
            endereco_rua = data.get('endereco_rua')
            endereco_numero = data.get('endereco_numero')
            endereco_bairro = data.get('endereco_bairro')
            endereco_cidade = data.get('endereco_cidade')
            endereco_estado = data.get('endereco_estado')
            email = data.get('email')
            celular = data.get('celular')

            if not nome or not cpf_cnpj or not categoria_pessoa_id:
                return jsonify({"error": "Os campos nome, cpf_cnpj e categoria_pessoa_id são obrigatórios!"}), 400

            self.pessoa_service.create_pessoa(nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular)
            return jsonify({"message": "Pessoa criada com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error": f"Erro ao criar pessoa: {str(e)}"}), 400

    def get_pessoa(self, pessoa_id):
        try:
            pessoa = self.pessoa_service.get_pessoa_by_id(pessoa_id)
            if pessoa:
                return jsonify({
                    "id": pessoa.get_id(),
                    "nome": pessoa.get_nome(),
                    "cpf_cnpj": pessoa.get_cpf_cnpj(),
                    "categoria_pessoa_id": pessoa.get_categoria_pessoa_id(),
                    "cep": pessoa.get_cep(),
                    "endereco_rua": pessoa.get_endereco_rua(),
                    "endereco_numero": pessoa.get_endereco_numero(),
                    "endereco_bairro": pessoa.get_endereco_bairro(),
                    "endereco_cidade": pessoa.get_endereco_cidade(),
                    "endereco_estado": pessoa.get_endereco_estado(),
                    "email": pessoa.get_email(),
                    "celular": pessoa.get_celular()
                }), 200
            return jsonify({"error": "Pessoa não encontrada"}), 404
        except Exception as e:
            return jsonify({"error": f"Erro ao buscar pessoa: {str(e)}"}), 400
        
    def list_pessoas(self):
        try:
            pessoas = self.pessoa_service.get_all_pessoas() 
            pessoas_data = [{
                "id": pessoa.get_id(),
                "nome": pessoa.get_nome(),
                "cpf_cnpj": pessoa.get_cpf_cnpj(),
                "categoria_pessoa_id": pessoa.get_categoria_pessoa_id(),
                "cep": pessoa.get_cep(),
                "endereco_rua": pessoa.get_endereco_rua(),
                "endereco_numero": pessoa.get_endereco_numero(),
                "endereco_bairro": pessoa.get_endereco_bairro(),
                "endereco_cidade": pessoa.get_endereco_cidade(),
                "endereco_estado": pessoa.get_endereco_estado(),
                "email": pessoa.get_email(),
                "celular": pessoa.get_celular()
            } for pessoa in pessoas]
            return jsonify(pessoas_data), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao listar pessoas: {str(e)}"}), 400

    def update_pessoa(self, pessoa_id):
        try:
            data = request.json
            nome = data.get('nome')
            cpf_cnpj = data.get('cpf_cnpj')
            categoria_pessoa_id = data.get('categoria_pessoa_id')
            cep = data.get('cep')
            endereco_rua = data.get('endereco_rua')
            endereco_numero = data.get('endereco_numero')
            endereco_bairro = data.get('endereco_bairro')
            endereco_cidade = data.get('endereco_cidade')
            endereco_estado = data.get('endereco_estado')
            email = data.get('email')
            celular = data.get('celular')

            if not nome or not cpf_cnpj or not categoria_pessoa_id:
                return jsonify({"error": "Os campos nome, cpf_cnpj e categoria_pessoa_id são obrigatórios!"}), 400

            self.pessoa_service.update_pessoa(pessoa_id, nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular)
            return jsonify({"message": f"Pessoa com ID {pessoa_id} atualizada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao atualizar pessoa: {str(e)}"}), 400

    def delete_pessoa(self, pessoa_id):
        try:
            self.pessoa_service.delete_pessoa(pessoa_id)
            return jsonify({"message": f"Pessoa com ID {pessoa_id} deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": f"Erro ao deletar pessoa: {str(e)}"}), 400