""" Traslator class """
import json

class Traslator:
    """ Tanslator class """
    files = ['keywords']
    traslations = {}

    def __init__(self, language):
        """ Init """
        self.language = language

    def translate(self, translate_id: str):
        """ Translate message """
        return self.traslations[translate_id].get(self.language, translate_id)

    @classmethod
    def load_translations(cls):
        """ Load translations """
        cls.traslations = {}
        for filename in cls.files:
            with open(f'/app/libraries/translator/jsons/{filename}.json') as file:
                data = json.load(file)
                cls.traslations = {
                    **Traslator.traslations,
                    **data
                }
