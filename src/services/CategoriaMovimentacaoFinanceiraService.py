from models.CategoriaMovimentacaoFinanceira import CategoriaMovimentacaoFinanceira

class CategoriaMovimentacaoFinanceiraService:
    def __init__(self, db):
        self.db = db

    def create_categoria_movimentacao_financeira(self, nome, tipo):
        if not nome or not tipo:
            raise ValueError("Os campos nome e tipo devem ser fornecidos.")
        
        try:
            categoria_movimentacao_financeira = CategoriaMovimentacaoFinanceira(nome=nome, tipo=tipo)
            categoria_movimentacao_financeira.create(self.db)
        except Exception as e:
            print(f"Erro ao criar categoria_movimentacao_financeira: {e}")
            raise

    def get_categoria_movimentacao_financeira_by_id(self, categoria_movimentacao_financeira_id):
        try:
            categoria_movimentacao_financeira = CategoriaMovimentacaoFinanceira.get_by_id(self.db, categoria_movimentacao_financeira_id)
            if categoria_movimentacao_financeira:
                return categoria_movimentacao_financeira
            return None
        except Exception as e:
            print(f"Erro ao buscar categoria_movimentacao_financeira: {e}")
            raise

    def get_all_categorias_movimentacao_financeira(self):
        try:
            categorias_movimentacao_financeira = CategoriaMovimentacaoFinanceira.get_all(self.db)
            return categorias_movimentacao_financeira
        except Exception as e:
            print(f"Erro ao listar categorias_movimentacao_financeira no serviço: {e}")
            raise

    def update_categoria_movimentacao_financeira(self, categoria_movimentacao_financeira_id, nome=None, tipo=None):
        if nome is None and tipo is None:
            raise ValueError("Pelo menos um campo deve ser fornecido para atualizar.")
        
        try:
            categoria_movimentacao_financeira = CategoriaMovimentacaoFinanceira.get_by_id(self.db, categoria_movimentacao_financeira_id)
            if categoria_movimentacao_financeira:
                if nome:
                    categoria_movimentacao_financeira.set_nome(nome)
                if tipo:
                    categoria_movimentacao_financeira.set_tipo(tipo)
                categoria_movimentacao_financeira.update(self.db)
            else:
                raise ValueError(f"CategoriaMovimentacaoFinanceira com ID {categoria_movimentacao_financeira_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar categoria_movimentacao_financeira: {e}")
            raise

    def delete_categoria_movimentacao_financeira(self, categoria_movimentacao_financeira_id):
        try:
            categoria_movimentacao_financeira = CategoriaMovimentacaoFinanceira.get_by_id(self.db, categoria_movimentacao_financeira_id)
            if categoria_movimentacao_financeira:
                categoria_movimentacao_financeira.delete(self.db)
            else:
                raise ValueError(f"CategoriaMovimentacaoFinanceira com ID {categoria_movimentacao_financeira_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar categoria_movimentacao_financeira: {e}")
            raise