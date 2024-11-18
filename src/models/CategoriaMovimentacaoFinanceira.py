class CategoriaMovimentacaoFinanceira:
    def __init__(self, id=None, nome=None, tipo=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO categoria_movimentacao_financeira (nome, tipo)
            VALUES (?, ?)
        """
        cursor.execute(query, (self.nome, self.tipo))
        db.connection.commit()

    def read(self, db, categoria_movimentacao_financeira_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, tipo FROM categoria_movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (categoria_movimentacao_financeira_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome, self.tipo = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE categoria_movimentacao_financeira
            SET nome = ?, tipo = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.tipo, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM categoria_movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, categoria_movimentacao_financeira_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, tipo FROM categoria_movimentacao_financeira WHERE id = ?"
        cursor.execute(query, (categoria_movimentacao_financeira_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, nome, tipo FROM categoria_movimentacao_financeira"
        cursor.execute(query)
        rows = cursor.fetchall()
        categorias = [cls(*row) for row in rows]
        return categorias

    def __str__(self):
        return f"CategoriaMovimentacaoFinanceira(ID: {self.id}, Nome: {self.nome}, Tipo: {self.tipo})"