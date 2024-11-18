from models.UsuarioEmpresa import UsuarioEmpresa

class UsuarioEmpresaService:
    def __init__(self, db):
        self.db = db

    def create_usuario_empresa(self, usuario_id, empresa_id, permissao):
        if not usuario_id or not empresa_id or not permissao:
            raise ValueError("Os campos usuario_id, empresa_id e permissao devem ser fornecidos.")
        
        try:
            usuario_empresa = UsuarioEmpresa(usuario_id=usuario_id, empresa_id=empresa_id, permissao=permissao)
            usuario_empresa.create(self.db)
        except Exception as e:
            print(f"Erro ao criar usuario_empresa: {e}")
            raise

    def get_usuario_empresa_by_id(self, usuario_empresa_id):
        try:
            usuario_empresa = UsuarioEmpresa.get_by_id(self.db, usuario_empresa_id)
            if usuario_empresa:
                return usuario_empresa
            return None
        except Exception as e:
            print(f"Erro ao buscar usuario_empresa: {e}")
            raise

    def get_all_usuario_empresas(self):
        try:
            usuario_empresas = UsuarioEmpresa.get_all(self.db)
            return usuario_empresas
        except Exception as e:
            print(f"Erro ao listar usuario_empresas no serviço: {e}")
            raise

    def update_usuario_empresa(self, usuario_empresa_id, usuario_id=None, empresa_id=None, permissao=None):
        if usuario_id is None and empresa_id is None and permissao is None:
            raise ValueError("Pelo menos um campo deve ser fornecido para atualizar.")
        
        try:
            usuario_empresa = UsuarioEmpresa.get_by_id(self.db, usuario_empresa_id)
            if usuario_empresa:
                if usuario_id:
                    usuario_empresa.set_usuario_id(usuario_id)
                if empresa_id:
                    usuario_empresa.set_empresa_id(empresa_id)
                if permissao:
                    usuario_empresa.set_permissao(permissao)
                usuario_empresa.update(self.db)
            else:
                raise ValueError(f"UsuarioEmpresa com ID {usuario_empresa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao atualizar usuario_empresa: {e}")
            raise

    def delete_usuario_empresa(self, usuario_empresa_id):
        try:
            usuario_empresa = UsuarioEmpresa.get_by_id(self.db, usuario_empresa_id)
            if usuario_empresa:
                usuario_empresa.delete(self.db)
            else:
                raise ValueError(f"UsuarioEmpresa com ID {usuario_empresa_id} não encontrada.")
        except Exception as e:
            print(f"Erro ao deletar usuario_empresa: {e}")
            raise