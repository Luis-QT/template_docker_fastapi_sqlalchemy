""" Define the parent class for all API validators """

class FlowAPI:
    """ Parent class for all API flows """

    def __init__(self):
        self.request = None
        self.module_data = None
        self.db = None
        self.total = None
        self.response = None

    def init_attributes(self, request, db, module_data):
        """ Initialize attributes """
        self.request = request
        self.db = db
        self.module_data = module_data

    def execute(self):
        """ Interface execute flow """
        return None
