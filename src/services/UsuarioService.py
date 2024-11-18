from models.Usuario import Usuario

class UsuarioService:
    def __init__(self, db):
        self.db = db

    def create_user(self, nome, email, senha, papel):
        if not nome or not email or not senha or not papel:
            raise ValueError("Todos os campos (nome, email, senha, papel) devem ser fornecidos.")
        
        try:
            user = Usuario(nome=nome, email=email, senha=senha, papel=papel)
            user.create(self.db)
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            raise

    def get_user_by_id(self, user_id):
        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                return user
            return None
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            raise

    def get_user_by_email(self, email):
        try:
            cursor = self.db.cursor()
            query = "SELECT id, nome, email, senha, papel FROM usuarios WHERE email = ?"
            cursor.execute(query, (email,))
            row = cursor.fetchone()

            if row:
                return Usuario(row[0], row[1], row[2], row[3], row[4])  # Atualize de acordo com a classe do modelo
            return None
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário pelo email: {str(e)}")

    def get_all_users(self):
        try:
            cursor = self.db.cursor()
            query = "SELECT id, nome, email, papel FROM usuarios"
            cursor.execute(query)
            rows = cursor.fetchall()

            users = []
            for row in rows:
                user = Usuario(row[0], row[1], row[2], row[3])
                users.append(user)

            return users
        except Exception as e:
            raise Exception(f"Erro ao buscar todos os usuários: {str(e)}")

    def update_user(self, user_id, nome=None, email=None, senha=None, papel=None):
        if nome is None and email is None and senha is None and papel is None:
            raise ValueError("Pelo menos um campo (nome, email, senha, papel) deve ser fornecido para atualizar.")
        
        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                if nome:
                    user.set_nome(nome)
                if email:
                    user.set_email(email)
                if senha:
                    user.set_senha(senha)
                if papel:
                    user.set_papel(papel)
                user.update(self.db)
            else:
                raise ValueError(f"Usuário com ID {user_id} não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            raise

    def delete_user(self, user_id):
        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                user.delete(self.db)
            else:
                raise ValueError(f"Usuário com ID {user_id} não encontrado.")
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            raise
