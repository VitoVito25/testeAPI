class Pessoa:
    def __init__(self, id=None, nome=None, cpf_cnpj=None, categoria_pessoa_id=None, cep=None, endereco_rua=None, endereco_numero=None, endereco_bairro=None, endereco_cidade=None, endereco_estado=None, email=None, celular=None):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.categoria_pessoa_id = categoria_pessoa_id
        self.cep = cep
        self.endereco_rua = endereco_rua
        self.endereco_numero = endereco_numero
        self.endereco_bairro = endereco_bairro
        self.endereco_cidade = endereco_cidade
        self.endereco_estado = endereco_estado
        self.email = email
        self.celular = celular

    # Getters e Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf_cnpj(self):
        return self.cpf_cnpj

    def set_cpf_cnpj(self, cpf_cnpj):
        self.cpf_cnpj = cpf_cnpj

    def get_categoria_pessoa_id(self):
        return self.categoria_pessoa_id

    def set_categoria_pessoa_id(self, categoria_pessoa_id):
        self.categoria_pessoa_id = categoria_pessoa_id

    def get_cep(self):
        return self.cep

    def set_cep(self, cep):
        self.cep = cep

    def get_endereco_rua(self):
        return self.endereco_rua

    def set_endereco_rua(self, endereco_rua):
        self.endereco_rua = endereco_rua

    def get_endereco_numero(self):
        return self.endereco_numero

    def set_endereco_numero(self, endereco_numero):
        self.endereco_numero = endereco_numero

    def get_endereco_bairro(self):
        return self.endereco_bairro

    def set_endereco_bairro(self, endereco_bairro):
        self.endereco_bairro = endereco_bairro

    def get_endereco_cidade(self):
        return self.endereco_cidade

    def set_endereco_cidade(self, endereco_cidade):
        self.endereco_cidade = endereco_cidade

    def get_endereco_estado(self):
        return self.endereco_estado

    def set_endereco_estado(self, endereco_estado):
        self.endereco_estado = endereco_estado

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_celular(self):
        return self.celular

    def set_celular(self, celular):
        self.celular = celular

    def create(self, db):
        cursor = db.get_cursor()
        query = """
            INSERT INTO pessoas (nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (self.nome, self.cpf_cnpj, self.categoria_pessoa_id, self.cep, self.endereco_rua, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado, self.email, self.celular))
        db.connection.commit()

    def read(self, db, pessoa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular FROM pessoas WHERE id = ?"
        cursor.execute(query, (pessoa_id,))
        result = cursor.fetchone()
        if result:
            self.id, self.nome, self.cpf_cnpj, self.categoria_pessoa_id, self.cep, self.endereco_rua, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado, self.email, self.celular = result
        return self

    def update(self, db):
        cursor = db.get_cursor()
        query = """
            UPDATE pessoas
            SET nome = ?, cpf_cnpj = ?, categoria_pessoa_id = ?, cep = ?, endereco_rua = ?, endereco_numero = ?, endereco_bairro = ?, endereco_cidade = ?, endereco_estado = ?, email = ?, celular = ?
            WHERE id = ?
        """
        cursor.execute(query, (self.nome, self.cpf_cnpj, self.categoria_pessoa_id, self.cep, self.endereco_rua, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado, self.email, self.celular, self.id))
        db.connection.commit()

    def delete(self, db):
        cursor = db.get_cursor()
        query = "DELETE FROM pessoas WHERE id = ?"
        cursor.execute(query, (self.id,))
        db.connection.commit()

    @classmethod
    def get_by_id(cls, db, pessoa_id):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular FROM pessoas WHERE id = ?"
        cursor.execute(query, (pessoa_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls, db):
        cursor = db.get_cursor()
        query = "SELECT id, nome, cpf_cnpj, categoria_pessoa_id, cep, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, email, celular FROM pessoas"
        cursor.execute(query)
        rows = cursor.fetchall()
        pessoas = [cls(*row) for row in rows]
        return pessoas

    def __str__(self):
        return f"Pessoa(ID: {self.id}, Nome: {self.nome}, CPF/CNPJ: {self.cpf_cnpj}, CategoriaPessoaID: {self.categoria_pessoa_id}, CEP: {self.cep}, Endereço: {self.endereco_rua}, {self.endereco_numero}, {self.endereco_bairro}, {self.endereco_cidade}, {self.endereco_estado}, Email: {self.email}, Celular: {self.celular})"