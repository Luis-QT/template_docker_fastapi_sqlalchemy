""" Defines the validations of the API Register """
from app.apis.auth.register.input import RegisterInput
from libraries.api_manager.validator.validator_api import ValidatorAPI

class RegisterValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:RegisterInput

    def validate_api(self):
        """ Function that ejecutes all the validations """
