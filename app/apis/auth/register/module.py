""" Define el modulo de la API register """
from requests import Session
from app.apis.auth.register.flow import RegisterFlow
from app.apis.auth.register.input import RegisterInput
from app.apis.auth.register.validator import RegisterValidator
from libraries.classes.module.module_api import ModuleAPI

class RegisterModule(ModuleAPI):
    """ Clase que controla a los componentes de la API Register """

    def __init__(self, request: RegisterInput, db: Session):
        """ Constructor de la clase """
        super().__init__()
        self.validator_api = RegisterValidator(request)
        self.flow_api = RegisterFlow(request)
        self.db = db
