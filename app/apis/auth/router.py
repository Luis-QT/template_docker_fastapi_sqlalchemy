""" Módulo enrutador de APIs """
from app.apis.auth.login.module import router as login_router

API_MODULE = "Auth"

def route(app):
    """ Enrutar APIs """
    app.include_router(login_router, tags=[API_MODULE])
