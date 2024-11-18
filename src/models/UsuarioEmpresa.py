class UsuarioEmpresa:
    def __init__(self, id=None, usuario_id=None, empresa_id=None, permissao=None):
        self.id = id
        self.usuario_id = usuario_id
        self.empresa_id = empresa_id
        self.permissao = permissao

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_usuario_id(self):
        return self.usuario_id

    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def get_empresa_id(self):
        return self.empresa_id

    def set_empresa_id(self, empresa_id):
        self.empresa_id = empresa_id

    def get_permissao(self):
        return self.permissao

    def set_permissao(self, permissao):
        self.permissao = permissao

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO usuario_empresa (usuario_id, empresa_id, permissao)
            VALUES (?, ?, ?)
        """
        cursor.execute(query, (self.usuario_id, self.empresa_id, self.permissao))
        db.connection.commit()

    def read(self, db, usuario_empresa_id):
        cursor = db.get_cursor()
        query = "SELECT id, usuario_id, empresa_id, permissao FROM usuario_empresa WHERE id = ?"
        cursor.execute(query, (usuario_empresa_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.usuario_id, self.empresa_id, self.permissao = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE usuario_empresa
            SET usuario_id = ?, empresa_id = ?, permissao = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.usuario_id, self.empresa_id, self.permissao, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM usuario_empresa WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, usuario_empresa_id):
        cursor = db.get_cursor()
        query = "SELECT id, usuario_id, empresa_id, permissao FROM usuario_empresa WHERE id = ?"
        cursor.execute(query, (usuario_empresa_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, usuario_id, empresa_id, permissao FROM usuario_empresa"
        cursor.execute(query)
        rows = cursor.fetchall()
        usuario_empresas = [cls(*row) for row in rows]
        return usuario_empresas

    def __str__(self):
        return f"UsuarioEmpresa(ID: {self.id}, Usuario ID: {self.usuario_id}, Empresa ID: {self.empresa_id}, Permissão: {self.permissao})"