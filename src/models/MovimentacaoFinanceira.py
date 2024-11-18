class MovimentacaoFinanceira:
    def __init__(self, id=None, conta_id=None, categoria_movimentacao_financeira_id=None, valor=None, descricao=None, beneficiario_origem_id=None, tipo_movimentacao=None, data_movimentacao=None):
        self.id = id
        self.conta_id = conta_id
        self.categoria_movimentacao_financeira_id = categoria_movimentacao_financeira_id
        self.valor = valor
        self.descricao = descricao
        self.beneficiario_origem_id = beneficiario_origem_id
        self.tipo_movimentacao = tipo_movimentacao
        self.data_movimentacao = data_movimentacao

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_conta_id(self):
        return self.conta_id

    def set_conta_id(self, conta_id):
        self.conta_id = conta_id

    def get_categoria_movimentacao_financeira_id(self):
        return self.categoria_movimentacao_financeira_id

    def set_categoria_movimentacao_financeira_id(self, categoria_movimentacao_financeira_id):
        self.categoria_movimentacao_financeira_id = categoria_movimentacao_financeira_id

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_beneficiario_origem_id(self):
        return self.beneficiario_origem_id

    def set_beneficiario_origem_id(self, beneficiario_origem_id):
        self.beneficiario_origem_id = beneficiario_origem_id

    def get_tipo_movimentacao(self):
        return self.tipo_movimentacao

    def set_tipo_movimentacao(self, tipo_movimentacao):
        self.tipo_movimentacao = tipo_movimentacao

    def get_data_movimentacao(self):
        return self.data_movimentacao

    def set_data_movimentacao(self, data_movimentacao):
        self.data_movimentacao = data_movimentacao

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO movimentacao_financeira (conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (self.conta_id, self.categoria_movimentacao_financeira_id, self.valor, self.descricao, self.beneficiario_origem_id, self.tipo_movimentacao, self.data_movimentacao))
        db.connection.commit()

    def read(self, db, movimentacao_financeira_id):
        cursor = db.get_cursor()
        query = "SELECT id, conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao FROM movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (movimentacao_financeira_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.conta_id, self.categoria_movimentacao_financeira_id, self.valor, self.descricao, self.beneficiario_origem_id, self.tipo_movimentacao, self.data_movimentacao = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE movimentacao_financeira
            SET conta_id = ?, categoria_movimentacao_financeira_id = ?, valor = ?, descricao = ?, beneficiario_origem_id = ?, tipo_movimentacao = ?, data_movimentacao = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.conta_id, self.categoria_movimentacao_financeira_id, self.valor, self.descricao, self.beneficiario_origem_id, self.tipo_movimentacao, self.data_movimentacao, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, movimentacao_financeira_id):
        cursor = db.get_cursor()
        query = "SELECT id, conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao FROM movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (movimentacao_financeira_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, conta_id, categoria_movimentacao_financeira_id, valor, descricao, beneficiario_origem_id, tipo_movimentacao, data_movimentacao FROM movimentacao_financeira"
        cursor.execute(query)
        rows = cursor.fetchall()
        movimentacoes = [cls(*row) for row in rows]
        return movimentacoes

    def __str__(self):
        return f"MovimentacaoFinanceira(ID: {self.id}, Conta ID: {self.conta_id}, CategoriaMovimentacaoFinanceira ID: {self.categoria_movimentacao_financeira_id}, Valor: {self.valor}, Descrição: {self.descricao}, Beneficiário/Origem ID: {self.beneficiario_origem_id}, Tipo Movimentação: {self.tipo_movimentacao}, Data Movimentação: {self.data_movimentacao})"