""" Módulo enrutador de APIs """
from fastapi import APIRouter, Depends
from requests import Session
from app.apis.auth.login.input import LoginInput, login_input
from app.apis.auth.login.module import LoginModule
from app.apis.auth.register.input import RegisterInput, register_input
from app.apis.auth.register.module import RegisterModule
from app.base_schemas.token import TokenBase
from app.connections.database import get_db

API_MODULE = "Auth"
router = APIRouter(prefix="/api/auth")

@router.post("/login", response_model=TokenBase)
def api_login(
    request: LoginInput = Depends(login_input),
    db: Session = Depends(get_db)
    ):
    module =  LoginModule(request, db)
    return module.use_api()

@router.post("/register")
def api_register(
    request: RegisterInput = Depends(register_input),
    db: Session = Depends(get_db)
    ):
    """ Register user """
    module =  RegisterModule(request, db)
    return module.use_api()

def route(app):
    """ Enrutar APIs """
    app.include_router(router, tags=[API_MODULE])
