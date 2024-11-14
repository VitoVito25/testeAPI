class Usuario:
    def __init__(self, id=None, nome=None, email=None, senha=None, papel=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
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
            # Instancia um objeto Usuario com os dados do banco
            return cls(*result)  # Desempacota a tupla em argumentos
        else:
            return None
        
    def __str__(self):
        return f"Usuario(ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Papel: {self.papel})"