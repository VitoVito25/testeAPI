class Conta:
    def __init__(self, id=None, nome=None, descricao=None, saldo_inicial=0.00, empresa_id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.saldo_inicial = saldo_inicial
        self.empresa_id = empresa_id

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_saldo_inicial(self):
        return self.saldo_inicial

    def set_saldo_inicial(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial

    def get_empresa_id(self):
        return self.empresa_id

    def set_empresa_id(self, empresa_id):
        self.empresa_id = empresa_id

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO conta (nome, descricao, saldo_inicial, empresa_id)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (self.nome, self.descricao, self.saldo_inicial, self.empresa_id))
        db.connection.commit()

    def read(self, db, conta_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, descricao, saldo_inicial, empresa_id FROM conta WHERE id = ?"
        cursor.execute(query, (conta_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome, self.descricao, self.saldo_inicial, self.empresa_id = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE conta
            SET nome = ?, descricao = ?, saldo_inicial = ?, empresa_id = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.descricao, self.saldo_inicial, self.empresa_id, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM conta WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, conta_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, descricao, saldo_inicial, empresa_id FROM conta WHERE id = ?"
        cursor.execute(query, (conta_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, nome, descricao, saldo_inicial, empresa_id FROM conta"
        cursor.execute(query)
        rows = cursor.fetchall()
        contas = [cls(*row) for row in rows]
        return contas

    def __str__(self):
        return f"Conta(ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Saldo Inicial: {self.saldo_inicial}, Empresa ID: {self.empresa_id})"