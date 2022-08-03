""" API Flow """
from datetime import timedelta
from app.apis.auth.login.input import LoginInput
from app.apis.auth.login.validator import LoginValidatorData
from libraries.utils import token_jwt
class LoginFlow:
    """ Clase que definir el flujo de la API register """

    def __init__(self, request: LoginInput):
        """ Constructor de la clase """
        self.data: LoginValidatorData
        self.request = request
        self.db = None

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        user = self.data.user
        access_token_expires = timedelta(minutes=token_jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = token_jwt.create_access_token(
            data={
                "id": str(user.id),
                "username": user.username,
                "avatar_url": user.avatar_url
            },
            expires_delta=access_token_expires,
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expired_in": token_jwt.ACCESS_TOKEN_EXPIRE_MINUTES*60
        }
