from models.Empresa import Empresa

class EmpresaService:
    def __init__(self, db):
        self.db = db

    def create_empresa(self, nome, cnpj):
        if not nome or not cnpj:
            raise ValueError("Todos os campos (nome, cnpj) devem ser fornecidos.")
        
        try:
            empresa = Empresa(nome=nome, cnpj=cnpj)
            empresa.create(self.db)
        except Exception as e:
            print(f"Erro ao criar empresa: {e}")
            raise

    def get_empresa_by_id(self, empresa_id):
        try:
            empresa = Empresa.get_by_id(self.db, empresa_id)
            if empresa:
                return empresa
            return None
        except Exception as e:
            print(f"Erro ao buscar empresa: {e}")
            raise

    def get_all_empresas(self):
        try:
            empresas = Empresa.get_all(self.db)
            return empresas
        except Exception as e:
            print(f"Erro ao listar empresas no serviço: {e}")
            raise

    def update_empresa(self, empresa_id, nome=None, cnpj=None):
        if nome is None and cnpj is None:
            raise ValueError("Pelo menos um campo (nome, cnpj) deve ser fornecido para atualizar.")
        
        try:
            empresa = Empresa.get_by_id(self.db, empresa_id)
            if empresa:
                if nome:
                    empresa.set_nome(nome)
                if cnpj:
                    empresa.set_cnpj(cnpj)
                empresa.update(self.db)
            else:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar empresa: {e}")
            raise

    def delete_empresa(self, empresa_id):
        try:
            empresa = Empresa.get_by_id(self.db, empresa_id)
            if empresa:
                empresa.delete(self.db)
            else:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar empresa: {e}")
            raise