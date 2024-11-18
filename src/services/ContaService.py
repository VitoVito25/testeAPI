from models.Conta import Conta

class ContaService:
    def __init__(self, db):
        self.db = db

    def create_conta(self, nome, descricao, saldo_inicial, empresa_id):
        if not nome or not empresa_id:
            raise ValueError("Os campos nome e empresa_id devem ser fornecidos.")
        
        try:
            conta = Conta(nome=nome, descricao=descricao, saldo_inicial=saldo_inicial, empresa_id=empresa_id)
            conta.create(self.db)
        except Exception as e:
            print(f"Erro ao criar conta: {e}")
            raise

    def get_conta_by_id(self, conta_id):
        try:
            conta = Conta.get_by_id(self.db, conta_id)
            if conta:
                return conta
            return None
        except Exception as e:
            print(f"Erro ao buscar conta: {e}")
            raise

    def get_all_contas(self):
        try:
            contas = Conta.get_all(self.db)
            return contas
        except Exception as e:
            print(f"Erro ao listar contas no serviço: {e}")
            raise

    def update_conta(self, conta_id, nome=None, descricao=None, saldo_inicial=None, empresa_id=None):
        if nome is None and descricao is None and saldo_inicial is None and empresa_id is None:
            raise ValueError("Pelo menos um campo deve ser fornecido para atualizar.")
        
        try:
            conta = Conta.get_by_id(self.db, conta_id)
            if conta:
                if nome:
                    conta.set_nome(nome)
                if descricao:
                    conta.set_descricao(descricao)
                if saldo_inicial is not None:
                    conta.set_saldo_inicial(saldo_inicial)
                if empresa_id:
                    conta.set_empresa_id(empresa_id)
                conta.update(self.db)
            else:
                raise ValueError(f"Conta com ID {conta_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar conta: {e}")
            raise

    def delete_conta(self, conta_id):
        try:
            conta = Conta.get_by_id(self.db, conta_id)
            if conta:
                conta.delete(self.db)
            else:
                raise ValueError(f"Conta com ID {conta_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar conta: {e}")
            raise