""" User Schema """
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    """ User data """
    id: UUID
    name: str
    username: str
    email: str
    status: str
    updated_at: datetime
    avatar_url: str
