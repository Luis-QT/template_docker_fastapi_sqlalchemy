""" Define las clases de entrada de la API register """
from fastapi import Depends
from pydantic import BaseModel, Field
from libraries.classes.input.input_api import InputAPI, input_api

class RegisterBody(BaseModel):
    """ Clase que define los datos del body de la API register """
    name: str = Field(..., example="test")
    username: str = Field(..., example="test")
    email: str = Field(..., example="test@test.com")
    password: str = Field(..., example="password")

class RegisterInput(InputAPI, RegisterBody):
    pass

def register_input(
    body: RegisterBody,
    input_api: InputAPI = Depends(input_api),
    ):
    return RegisterInput.parse_obj({
        **input_api.dict(),
        **body.dict()
    })
