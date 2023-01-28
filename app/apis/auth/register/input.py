""" Defines the input schema of the API Register """
from pydantic import BaseModel
from fastapi import Body

class RegisterBody(BaseModel):
    """ Body API """
    name: str = Body(..., example="test")
    email: str = Body(..., example="test@test.com")
    password: str = Body(..., example="password")

class RegisterQuery(BaseModel):
    """ Query API """

class RegisterHeader(BaseModel):
    """ Header API """

class RegisterPath(BaseModel):
    """ Path API """

class RegisterInput(
    RegisterBody,
    RegisterQuery,
    RegisterHeader,
    RegisterPath
):
    """ Input API """
