import src.models.Usuario as Usuario

class UserService:
    def __init__(self, db):
        self.db = db

    def create_user(self, name, email, password, role):
        # Validation for NOT NULL fields
        if not name or not email or not password or not role:
            print("Error: All fields (name, email, password, role) must be provided.")
            return

        try:
            user = Usuario(nome=name, email=email, senha=password, papel=role)
            user.create(self.db)
            print(f"User {name} created successfully.")
        except Exception as e:
            print(f"Error creating user: {e}")

    def get_user_by_id(self, user_id):
        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                print(f"User found: {user}")
            else:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error retrieving user by ID: {e}")
    
    def update_user(self, user_id, name=None, email=None, password=None, role=None):
        # Validation for NOT NULL fields during update
        if name is None and email is None and password is None and role is None:
            print("Error: At least one field (name, email, password, or role) must be provided for update.")
            return

        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                if name:
                    user.set_nome(name)
                if email:
                    user.set_email(email)
                if password:
                    user.set_senha(password)
                if role:
                    user.set_papel(role)
                user.update(self.db)
                print(f"User with ID {user_id} updated successfully.")
            else:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        try:
            user = Usuario.get_by_id(self.db, user_id)
            if user:
                user.delete(self.db)
            else:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error deleting user: {e}")
