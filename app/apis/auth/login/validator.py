
""" Define las validaciones de la API register """
from app.apis.auth.login.input import LoginInput
from app.db.models.user import User
from libraries.classes.validator.validator_api import ValidatorAPI
from libraries.translator.translator import Traslator
from libraries.utils.crypto import verify_password

class LoginValidatorData:
    def __init__(self, user:User):
        self.user = user

class LoginValidator(ValidatorAPI, LoginValidatorData):
    """ Clase que valida la API Register """

    def __init__(self, request:LoginInput):
        """ Constructor de la clase """
        super().__init__()
        self.translator = Traslator(request.language)
        self.request = request
        self.db = None

    def validate(self):
        """ Función que ejecuta las validaciones de la API """
        self.val_username_exist()
        self.val_password()
        return LoginValidatorData(
            user=self.user
        )

    def val_username_exist(self):
        """ Validar si existe el usuario """
        self.user = self.db.query(User).filter_by(
            username=self.request.username
        ).first()
        if self.user is None:
            raise self.validation_exception(
                'username', 'The username not found'
            )

    def val_password(self):
        """ Validar si la contraseña es correcta """
        is_valid = verify_password(self.request.password, self.user.password)
        if not is_valid:
            raise self.validation_exception(
                'username', 'The username not found'
            )
