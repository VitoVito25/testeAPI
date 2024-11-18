from models.MovimentacaoFinanceira import MovimentacaoFinanceira

class MovimentacaoFinanceiraService:
    def __init__(self, db):
        self.db = db

    def create_movimentacao_financeira(self, conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao):
        if not conta_id or not categoria_movimentacao_financeira_id or not valor or not tipo_movimentacao or not data_movimentacao:
            raise ValueError("Os campos conta_id, categoria_movimentacao_financeira_id, valor, tipo_movimentacao e data_movimentacao devem ser fornecidos.")
        
        try:
            movimentacao_financeira = MovimentacaoFinanceira(conta_id=conta_id, categoria_movimentacao_financeira_id=categoria_movimentacao_financeira_id, valor=valor, descricao=descricao, beneficiario_origem_id=beneficiario_origem_id, tipo_movimentacao=tipo_movimentacao, data_movimentacao=data_movimentacao)
            movimentacao_financeira.create(self.db)
        except Exception as e:
            print(f"Erro ao criar movimentacao_financeira: {e}")
            raise

    def get_movimentacao_financeira_by_id(self, movimentacao_financeira_id):
        try:
            movimentacao_financeira = MovimentacaoFinanceira.get_by_id(self.db, movimentacao_financeira_id)
            if movimentacao_financeira:
                return movimentacao_financeira
            return None
        except Exception as e:
            print(f"Erro ao buscar movimentacao_financeira: {e}")
            raise

    def get_all_movimentacoes_financeiras(self):
        try:
            movimentacoes_financeiras = MovimentacaoFinanceira.get_all(self.db)
            return movimentacoes_financeiras
        except Exception as e:
            print(f"Erro ao listar movimentacoes_financeiras no serviço: {e}")
            raise

    def update_movimentacao_financeira(self, movimentacao_financeira_id, conta_id=None, categoria_movimentacao_financeira_id=None, valor=None, descricao=None, beneficiario_origem_id=None, tipo_movimentacao=None, data_movimentacao=None):
        if conta_id is None and categoria_movimentacao_financeira_id is None and valor is None and descricao is None and beneficiario_origem_id is None and tipo_movimentacao is None and data_movimentacao is None:
            raise ValueError("Pelo menos um campo deve ser fornecido para atualizar.")
        
        try:
            movimentacao_financeira = MovimentacaoFinanceira.get_by_id(self.db, movimentacao_financeira_id)
            if movimentacao_financeira:
                if conta_id:
                    movimentacao_financeira.set_conta_id(conta_id)
                if categoria_movimentacao_financeira_id:
                    movimentacao_financeira.set_categoria_movimentacao_financeira_id(categoria_movimentacao_financeira_id)
                if valor is not None:
                    movimentacao_financeira.set_valor(valor)
                if descricao:
                    movimentacao_financeira.set_descricao(descricao)
                if beneficiario_origem_id:
                    movimentacao_financeira.set_beneficiario_origem_id(beneficiario_origem_id)
                if tipo_movimentacao:
                    movimentacao_financeira.set_tipo_movimentacao(tipo_movimentacao)
                if data_movimentacao:
                    movimentacao_financeira.set_data_movimentacao(data_movimentacao)
                movimentacao_financeira.update(self.db)
            else:
                raise ValueError(f"MovimentacaoFinanceira com ID {movimentacao_financeira_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar movimentacao_financeira: {e}")
            raise

    def delete_movimentacao_financeira(self, movimentacao_financeira_id):
        try:
            movimentacao_financeira = MovimentacaoFinanceira.get_by_id(self.db, movimentacao_financeira_id)
            if movimentacao_financeira:
                movimentacao_financeira.delete(self.db)
            else:
                raise ValueError(f"MovimentacaoFinanceira com ID {movimentacao_financeira_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar movimentacao_financeira: {e}")
            raise