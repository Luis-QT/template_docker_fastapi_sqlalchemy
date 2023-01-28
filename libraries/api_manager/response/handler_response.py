""" Define logical class HandlerResponse """
class HandlerResponse:
    """ Class HandlerResponse """
    def __init__(self, value):
        self.value = value
        self.parts = []
        self.response = {}
        self.response_dict = {}

    def get_response(self):
        """ Return response """
        if isinstance(self.value, list):
            if isinstance(self.value, dict):
                self.set_dicts()
            else:
                self.set_values()
        else:
            self.set_dict()
        return self.response

    def set_dicts(self):
        """ Set dicts """
        self.response = []
        for part_value in self.value:
            self.response.append(part_value)

    def set_values(self):
        """ Set values """
        self.response = []
        for part_value in self.value:
            self.response_dict = {}
            for part in self.parts:
                part.registry = part_value
                self.response_dict.update(part.get_field())
            self.response.append(self.response_dict)

    def set_dict(self):
        """ Set dict """
        self.response = {}
        for part in self.parts:
            part.registry = self.value
            self.response.update(part.get_field())
