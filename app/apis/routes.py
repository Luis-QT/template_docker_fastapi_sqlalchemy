""" Módulo enrutador de APIs """
# pylint: disable=line-too-long
from fastapi import APIRouter
from app.apis.auth.login.router import router as login_router
from app.apis.auth.register.router import router as register_router

router = APIRouter()

def route(app):
    """ Enrutar APIs """
    app.include_router(login_router)
    app.include_router(register_router)
