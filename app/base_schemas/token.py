""" Token Schema """
from uuid import UUID
from pydantic import BaseModel

class TokenBase(BaseModel):
    """ Token generated"""
    access_token: str
    token_type: str
    expired_in: str

class TokenDataBase(BaseModel):
    """ Token data """
    id: UUID
    username: str
    avatar_url: str
    user_type: str
