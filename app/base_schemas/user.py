""" User Schema """
from pydantic import BaseModel

class UserBase(BaseModel):
    """ User data """
    id: int
    name: str
    email: str
    avatar_url: str
