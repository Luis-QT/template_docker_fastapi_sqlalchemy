""" API Validator """
from libraries.classes.api_base import APIBase
from libraries.utils.crypto import verify_password
from libraries.utils.exception import dao_exception
from libraries.translator.translator import Traslator
from app.db.models import User

class ValidatorLogin(APIBase):
    """ API Validator """

    def run(self):
        """ Run validator """
        self.find_user()
        self.val_username_exist()
        self.val_password()

    def find_user(self):
        self.data['user'] = self.db.query(User).filter_by(
            username=self.data.get('username')
        ).first()

    def val_username_exist(self):
        """ Validar si existe el usuario """
        if self.data.get('user') is None:
            raise self.validation_exception(
                'username', 'The username not found'
            )

    def val_password(self):
        """ Validar si la contraseña es correcta """
        is_valid = verify_password(self.data.get('password'), self.data.get('user').password)
        if not is_valid:
            raise self.validation_exception(
                'username', 'The username not found'
            )
