""" dict_mixin.py """
from app.db.base import model_as_dict

class DictMixin:
    """ Mixin to add as_dict() """

    def as_dict(self) -> dict:
        """ Convert object to dictionary """
        return model_as_dict(self)
