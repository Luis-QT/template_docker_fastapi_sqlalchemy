""" Define parent class for all API responses """
from libraries.api_manager.response.handler_response import HandlerResponse

class ResponseAPI:
    """ Parent class for all API responses """

    def __init__(self):
        """ Constructor of the class """
        self.value = None
        self.handler = None

    def set_response(self):
        """ Interface set response """

    def set_value(self, value):
        """ Set value
        @param value: API Flow component response
        """
        self.value = value

    def set_structure(self, parts):
        """ Set response structure """
        self.handler = HandlerResponse(self.value)
        self.handler.parts = parts

    def get_response(self):
        """ Return API response """
        self.set_response()
        return self.handler.get_response()
