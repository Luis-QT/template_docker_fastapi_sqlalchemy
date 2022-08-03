""" Define el modulo de la API register """
from requests import Session
from app.apis.auth.login.flow import LoginFlow
from app.apis.auth.login.input import LoginInput
from app.apis.auth.login.validator import LoginValidator
from libraries.classes.module.module_api import ModuleAPI

class LoginModule(ModuleAPI):
    """ Clase que controla a los componentes de la API Register """

    def __init__(self, request: LoginInput, db: Session):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = LoginValidator(request)
        self.flow_api = LoginFlow(request)
        self.db = db
