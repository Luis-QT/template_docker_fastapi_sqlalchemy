""" Define el flujo del API register """
from app.apis.auth.register.input import RegisterInput
from app.apis.auth.register.validator import RegisterValidatorData
from app.db.models.user import User
from libraries.utils.crypto import hash_password
from libraries.utils.avatar import generate_avatar_url

class RegisterFlow:
    """ Clase que definir el flujo de la API register """

    def __init__(self, request: RegisterInput):
        """ Constructor de la clase """
        self.data: RegisterValidatorData
        self.request = request
        self.db = None

    def execute(self):
        """ Función que ejecuta el flujo de la API register """
        self.register_user()
        self.db.commit()
        return self.user.as_dict()

    def register_user(self):
        """ Registrar usuario """
        self.user = User(
            username=self.request.username,
            email=self.request.email,
            name=self.request.name,
            password=hash_password(self.request.password),
            avatar_url=generate_avatar_url(self.request.username)
        )
        self.db.add(self.user)
        self.db.flush()
