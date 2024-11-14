class Usuario:
    def __init__(self, id=None, nome=None, email=None, senha=None, papel=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.papel = papel

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    def get_papel(self):
        return self.papel

    def set_papel(self, papel):
        self.papel = papel

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO usuario (nome, email, senha, papel)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (self.nome, self.email, self.senha, self.papel))
        db.connection.commit()

    def read(self, db, user_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, email, papel FROM usuario WHERE id = ?"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome, self.email, self.papel = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?, papel = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.email, self.senha, self.papel, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM usuario WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, user_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, email, senha, papel FROM usuario WHERE id = ?"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    def __str__(self):
        return f"Usuario(ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Papel: {self.papel})"
