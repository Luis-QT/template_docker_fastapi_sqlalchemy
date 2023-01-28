""" Defines the module of the API Register """
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import RegisterFlow
from .validator import RegisterValidator

class RegisterModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = RegisterValidator()
        self.flow_api = RegisterFlow()
        self.is_searchable_api = False
        self.db = db
