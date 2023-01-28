""" Define parent class for all API validators """
from libraries.utils.exception import dao_exception

class ValidatorAPI:
    """ Parent class for all API validators """
    def __init__(self):
        self.request = None
        self.module_data = None
        self.db = None

    def init_attributes(self, request, db, module_data):
        """ Initialize attributes """
        self.request = request
        self.db = db
        self.module_data = module_data

    def validate_api(self):
        """ Interface validate api """
        return None

    def validation_exception(self, field, message):
        """ Return validation exception """
        return dao_exception(
            400, field, message
        )
