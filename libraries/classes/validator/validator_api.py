from libraries.translator.translator import Traslator
from libraries.utils.exception import dao_exception


class ValidatorAPI:
    def __init__(self):
        self.request = None
        self.db = None
        self.translator = None
    
    def validate(self):
        return None

    def validation_exception(self, field, message):
        """ Validation exception """
        return dao_exception(
            400, field, self.translator.translate(message)
        )
