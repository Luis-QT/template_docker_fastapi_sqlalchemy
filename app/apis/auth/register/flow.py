""" Defines the flow of the API Register """
from app.apis.auth.register.input import RegisterInput
from app.db.models.user import User
from libraries.utils.crypto import hash_password
from libraries.utils.avatar import generate_avatar_url
from libraries.api_manager.flow.flow_api import FlowAPI

class RegisterFlow(FlowAPI):
    """ Class that defines the API flow """

    def __init__(self):
        """ Constructor of the class """
        super().__init__()
        self.request:RegisterInput
        self.user = None

    def execute(self):
        """ Function that ejecutes the flow """
        self.register_user()
        self.db.commit()
        return self.user.as_dict()

    def register_user(self):
        """ Register the user """
        self.user = User(
            email=self.request.email,
            name=self.request.name,
            password=hash_password(self.request.password),
            avatar_url=generate_avatar_url(self.request.email)
        )
        self.db.add(self.user)
        self.db.flush()
