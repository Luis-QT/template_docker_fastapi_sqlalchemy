""" API Flow """
from datetime import timedelta
from libraries.classes.api_base import APIBase
from libraries.utils import token_jwt

class FlowLogin(APIBase):
    """ API Flow """

    def run(self):
        """ Run flow """
        user = self.data.get('user')
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
