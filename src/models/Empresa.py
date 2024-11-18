class Empresa:
    def __init__(self, id=None, nome=None, cnpj=None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO empresa (nome, cnpj)
            VALUES (?, ?)
        """
        cursor.execute(query, (self.nome, self.cnpj))
        db.connection.commit()

    def read(self, db, empresa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cnpj FROM empresa WHERE id = ?"
        cursor.execute(query, (empresa_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome, self.cnpj = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE empresa
            SET nome = ?, cnpj = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.cnpj, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM empresa WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, empresa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cnpj FROM empresa WHERE id = ?"
        cursor.execute(query, (empresa_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cnpj FROM empresa"
        cursor.execute(query)
        rows = cursor.fetchall()
        empresas = [cls(*row) for row in rows]
        return empresas

    def __str__(self):
        return f"Empresa(ID: {self.id}, Nome: {self.nome}, CNPJ: {self.cnpj})"