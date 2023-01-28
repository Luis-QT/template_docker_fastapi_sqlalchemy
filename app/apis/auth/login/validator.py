
""" Defines the validations of the API Login """
from app.apis.auth.login.input import LoginInput
from app.db.models.user import User
from libraries.api_manager.validator.validator_api import ValidatorAPI
from libraries.utils.crypto import verify_password

class LoginValidator(ValidatorAPI):
    """ Class that validates the input of the API """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:LoginInput
        self.user = None

    def validate_api(self):
        """ Function that ejecutes all the validations """
        self.val_email_exist()
        self.val_password()

    def val_email_exist(self):
        """ Validate if the email exist """
        self.user = self.db.query(User).filter_by(
            email=self.request.email
        ).first()
        if self.user is None:
            raise self.validation_exception(
                'email', 'No se encontró el usuario'
            )
        self.module_data['user'] = self.user

    def val_password(self):
        """ Validate if the password is correct """
        is_valid = verify_password(self.request.password, self.user.password)
        if not is_valid:
            raise self.validation_exception(
                'email', 'Contraseña incorrecta'
            )
