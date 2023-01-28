""" Define the class that return the relation belongs to """

from libraries.api_manager.response.handler_response import HandlerResponse
from libraries.api_manager.response.response_field import ResponseField

class RelationHasOne(ResponseField):
    """ Class that return the relation belongs to """

    def __init__(self, field_name, parts, deleted=False):
        super().__init__(field_name)
        self.registry = None
        self.deleted = deleted
        self.parts = parts

    def get_field(self):
        """ Get field """
        field = {}
        if hasattr(self.registry, self.field_name):
            response_object = getattr(self.registry, self.field_name)
            response_dict = {}
            handler = HandlerResponse(response_object)
            handler.parts = self.parts
            response_dict.update(handler.get_response())
            field[self.field_name] = response_dict
        return field
