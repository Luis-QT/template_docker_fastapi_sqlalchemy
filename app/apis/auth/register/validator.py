""" Define las validaciones de la API register """
from app.apis.auth.register.input import RegisterInput
from libraries.classes.validator.validator_api import ValidatorAPI
from libraries.translator.translator import Traslator

class RegisterValidatorData:
    def __init__(self):
        """ Constructor de la clase """
        pass

class RegisterValidator(ValidatorAPI, RegisterValidatorData):
    """ Clase que valida la API Register """

    def __init__(self, request:RegisterInput):
        """ Constructor de la clase """
        super().__init__()
        self.translator = Traslator(request.language)
        self.request = request
        self.db = None

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        return RegisterValidatorData()
