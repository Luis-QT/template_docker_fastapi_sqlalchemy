""" Define parent class for model field """

class ModelFields:
    """ Parent class for model field """

    def __init__(self):
        self.registry = None

    def get_field(self):
        """ Get field """
        return self.registry.as_dict()
