class ModuleAPI:
    def __init__(self):
        self.input_api = None
        self.validator_api = None
        self.flow_api = None

    def use_api(self):
        """ Función que ejecuta la API """
        self.validator_api.db = self.db
        self.flow_api.db = self.db
        data = self.validator_api.validate()
        self.flow_api.data = data
        response = self.flow_api.execute()
        return response
