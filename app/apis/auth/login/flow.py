""" Defines the flow of the API Login """
from datetime import timedelta
from app.apis.auth.login.input import LoginInput
from libraries.utils import token_jwt
from libraries.api_manager.flow.flow_api import FlowAPI

class LoginFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        super().__init__()
        self.request:LoginInput

    def execute(self):
        """ Function that ejecutes the flow """
        user = self.module_data['user']
        access_token_expires = timedelta(minutes=token_jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = token_jwt.create_access_token(
            data={
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "avatar_url": user.avatar_url
            },
            expires_delta=access_token_expires,
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expired_in": token_jwt.ACCESS_TOKEN_EXPIRE_MINUTES*60
        }
