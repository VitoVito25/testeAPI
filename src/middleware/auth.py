from functools import wraps
from flask import request, jsonify, current_app
import jwt
import datetime

class Auth:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    # Função para gerar o token JWT
    def generate_jwt(self, user):
        try:
            # Definir o payload do token
            payload = {
                'user_id': user.get_id(),
                'nome': user.get_nome(),
                'email': user.get_email(),
                'papel': user.get_papel(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiração de 1 hora
            }
            
            # Gerar o token JWT
            token = jwt.encode(payload, self.secret_key, algorithm='HS256')
            
            return token
        except Exception as e:
            raise Exception(f"Erro ao gerar o token: {str(e)}")

    # Função para proteger as rotas com token
    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            # Verificar se o token está no cabeçalho Authorization
            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']
                if auth_header.startswith("Bearer "):
                    token = auth_header.split(" ")[1]

            if not token:
                return jsonify({"error": "Token não fornecido"}), 401

            try:
                # Decodificar o token JWT
                payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
                request.user = payload  # Disponibilizar o payload para a rota
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token inválido"}), 401

            return f(*args, **kwargs)
        return decorated
