class CategoriaPessoa:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO categoria_pessoa (nome)
            VALUES (?)
        """
        cursor.execute(query, (self.nome,))
        db.connection.commit()

    def read(self, db, categoria_pessoa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome FROM categoria_pessoa WHERE id = ?"
        cursor.execute(query, (categoria_pessoa_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE categoria_pessoa
            SET nome = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM categoria_pessoa WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, categoria_pessoa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome FROM categoria_pessoa WHERE id = ?"
        cursor.execute(query, (categoria_pessoa_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, nome FROM categoria_pessoa"
        cursor.execute(query)
        rows = cursor.fetchall()
        categorias = [cls(*row) for row in rows]
        return categorias

    def __str__(self):
        return f"CategoriaPessoa(ID: {self.id}, Nome: {self.nome})"