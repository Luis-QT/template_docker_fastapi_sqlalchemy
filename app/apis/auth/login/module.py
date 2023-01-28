""" Defines the module of the API Login """
from libraries.api_manager.module.module_api import ModuleAPI
from .flow import LoginFlow
from .validator import LoginValidator

class LoginModule(ModuleAPI):
    """ Class that controls the components of the API """

    def __init__(self, request, db):
        """ Constructor of the class """
        super().__init__()
        self.request = request
        self.validator_api = LoginValidator()
        self.flow_api = LoginFlow()
        self.is_searchable_api = False
        self.db = db
