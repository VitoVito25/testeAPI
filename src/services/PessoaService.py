from models.Pessoa import Pessoa

class PessoaService:
    def __init__(self, db):
        self.db = db

    def create_pessoa(self, nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular):
        if not nome or not cpf_cnpj or not categoria_pessoa_id:
            raise ValueError("Os campos nome, cpf_cnpj e categoria_pessoa_id devem ser fornecidos.")
        
        try:
            pessoa = Pessoa(nome=nome, cpf_cnpj=cpf_cnpj, categoria_pessoa_id=categoria_pessoa_id, cep=cep, endereco_rua=endereco_rua, endereco_numero=endereco_numero, endereco_bairro=endereco_bairro, endereco_cidade=endereco_cidade, endereco_estado=endereco_estado, email=email, celular=celular)
            pessoa.create(self.db)
        except Exception as e:
            print(f"Erro ao criar pessoa: {e}")
            raise

    def get_pessoa_by_id(self, pessoa_id):
        try:
            pessoa = Pessoa.get_by_id(self.db, pessoa_id)
            if pessoa:
                return pessoa
            return None
        except Exception as e:
            print(f"Erro ao buscar pessoa: {e}")
            raise

    def get_all_pessoas(self):
        try:
            pessoas = Pessoa.get_all(self.db)
            return pessoas
        except Exception as e:
            print(f"Erro ao listar pessoas no serviço: {e}")
            raise

    def update_pessoa(self, pessoa_id, nome=None, cpf_cnpj=None, categoria_pessoa_id=None, cep=None, endereco_rua=None, endereco_numero=None, endereco_bairro=None, endereco_cidade=None, endereco_estado=None, email=None, celular=None):
        if nome is None and cpf_cnpj is None and categoria_pessoa_id is None and cep is None and endereco_rua is None and endereco_numero is None and endereco_bairro is None and endereco_cidade is None and endereco_estado is None and email is None and celular is None:
            raise ValueError("Pelo menos um campo deve ser fornecido para atualizar.")
        
        try:
            pessoa = Pessoa.get_by_id(self.db, pessoa_id)
            if pessoa:
                if nome:
                    pessoa.set_nome(nome)
                if cpf_cnpj:
                    pessoa.set_cpf_cnpj(cpf_cnpj)
                if categoria_pessoa_id:
                    pessoa.set_categoria_pessoa_id(categoria_pessoa_id)
                if cep:
                    pessoa.set_cep(cep)
                if endereco_rua:
                    pessoa.set_endereco_rua(endereco_rua)
                if endereco_numero:
                    pessoa.set_endereco_numero(endereco_numero)
                if endereco_bairro:
                    pessoa.set_endereco_bairro(endereco_bairro)
                if endereco_cidade:
                    pessoa.set_endereco_cidade(endereco_cidade)
                if endereco_estado:
                    pessoa.set_endereco_estado(endereco_estado)
                if email:
                    pessoa.set_email(email)
                if celular:
                    pessoa.set_celular(celular)
                pessoa.update(self.db)
            else:
                raise ValueError(f"Pessoa com ID {pessoa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar pessoa: {e}")
            raise

    def delete_pessoa(self, pessoa_id):
        try:
            pessoa = Pessoa.get_by_id(self.db, pessoa_id)
            if pessoa:
                pessoa.delete(self.db)
            else:
                raise ValueError(f"Pessoa com ID {pessoa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar pessoa: {e}")
            raise