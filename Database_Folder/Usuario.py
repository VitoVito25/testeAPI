class Usuario:
    def __init__(self, id=None, nome=None, email=None, senha=None, papel=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.papel = papel

    # Getters
    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def get_papel(self):
        return self.papel

    # Setters
    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_senha(self, senha):
        self.senha = senha

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
        try:
            cursor = db.get_cursor()
            query = "DELETE FROM usuario WHERE id = ?"
            cursor.execute(query, (self.id,))

            # Confirma a transação no banco
            db.connection.commit()

            # Verifica se alguma linha foi afetada
            if cursor.rowcount > 0:
                print(f"Usuário com ID {self.id} excluído com sucesso.")
            else:
                print(f"Nenhum usuário encontrado com ID {self.id}. Nenhuma exclusão realizada.")

        except Exception as e:
            # Captura e exibe erros
            print(f"Erro ao tentar excluir o usuário com ID {self.id}: {e}")
            db.connection.rollback()  # Caso ocorra erro, desfaz a transação

    @classmethod
    def get_by_id(cls, db, user_id):
        try:
            cursor = db.get_cursor()
            query = "SELECT id, nome, email, senha, papel FROM usuario WHERE id = ?"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if result:
                # Instancia um objeto Usuario com os dados do banco
                return cls(*result)  # Desempacota a tupla em argumentos
            else:
                # Retorna None se o usuário não for encontrado
                print(f"User with ID {user_id} not found.")
                return None
        except Exception as e:
            # Tratamento de qualquer erro que possa ocorrer durante a execução da query
            print(f"An error occurred while fetching the user: {e}")
            return None
        
    def __str__(self):
        return f"Usuario(ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Papel: {self.papel})"