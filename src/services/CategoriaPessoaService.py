from models.CategoriaPessoa import CategoriaPessoa

class CategoriaPessoaService:
    def __init__(self, db):
        self.db = db

    def create_categoria_pessoa(self, nome):
        if not nome:
            raise ValueError("O campo nome deve ser fornecido.")
        
        try:
            categoria_pessoa = CategoriaPessoa(nome=nome)
            categoria_pessoa.create(self.db)
        except Exception as e:
            print(f"Erro ao criar categoria_pessoa: {e}")
            raise

    def get_categoria_pessoa_by_id(self, categoria_pessoa_id):
        try:
            categoria_pessoa = CategoriaPessoa.get_by_id(self.db, categoria_pessoa_id)
            if categoria_pessoa:
                return categoria_pessoa
            return None
        except Exception as e:
            print(f"Erro ao buscar categoria_pessoa: {e}")
            raise

    def get_all_categorias_pessoa(self):
        try:
            categorias_pessoa = CategoriaPessoa.get_all(self.db)
            return categorias_pessoa
        except Exception as e:
            print(f"Erro ao listar categorias_pessoa no serviço: {e}")
            raise

    def update_categoria_pessoa(self, categoria_pessoa_id, nome=None):
        if nome is None:
            raise ValueError("Pelo menos um campo (nome) deve ser fornecido para atualizar.")
        
        try:
            categoria_pessoa = CategoriaPessoa.get_by_id(self.db, categoria_pessoa_id)
            if categoria_pessoa:
                if nome:
                    categoria_pessoa.set_nome(nome)
                categoria_pessoa.update(self.db)
            else:
                raise ValueError(f"CategoriaPessoa com ID {categoria_pessoa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar categoria_pessoa: {e}")
            raise

    def delete_categoria_pessoa(self, categoria_pessoa_id):
        try:
            categoria_pessoa = CategoriaPessoa.get_by_id(self.db, categoria_pessoa_id)
            if categoria_pessoa:
                categoria_pessoa.delete(self.db)
            else:
                raise ValueError(f"CategoriaPessoa com ID {categoria_pessoa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar categoria_pessoa: {e}")
            raise