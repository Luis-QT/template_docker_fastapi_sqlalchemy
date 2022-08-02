"""" API Base """

from libraries.translator.translator import Traslator
from libraries.utils.exception import dao_exception


class APIBase:
    def __init__(self, request):
        self.request = request
        self.db = None
        self.user_session = None
        self.data = {}
        self.language = 'EN'
        self.timezone = None
        self.load_metadata()
        self.translator = Traslator(self.language)

    def load_metadata(self):
        """ Load metadata """
        self.db = self.request.get('db')
        self.user_session = self.request.get('user_session')
        self.language = self.request.get('language', 'EN')
        self.data = self.request
        self.timezone = self.request.get('timezone')

    def validation_exception(self, field, message):
        return dao_exception(
            400, field, self.translator.translate(message)
        )
