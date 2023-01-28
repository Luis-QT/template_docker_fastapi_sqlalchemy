""" Define class that implements the Bearer Authentication """
import os
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = os.environ['JWT_SECRET_KEY']
ALGORITHM = os.environ['JWT_ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ['JWT_ACCESS_TOKEN_EXPIRE_MINUTES'])

class JWTBearer(HTTPBearer):
    """ Class that implements the Bearer Authentication """
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """ Inyect the token in the request """
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials is None:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
        if not self.verify_jwt(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid token or expired token.")
        return decode_token(credentials.credentials)

    def verify_jwt(self, jwtoken: str) -> bool:
        """ Verify the token """
        is_token_valid: bool = False
        try:
            payload = decode_token(jwtoken)
        except: # pylint: disable=bare-except
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid

def decode_token(token: str):
    """ Decode token """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return {
        'id': payload.get("id"),
        'name': payload.get("name"),
        'email': payload.get("email"),
        'avatar_url': payload.get("avatar_url")
    }
