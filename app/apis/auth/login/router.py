""" Defines the router funtion of the API Login """
from fastapi import APIRouter, Depends, Body
from app.base_schemas.token import TokenBase
from app.connections.database import get_db
from app.db.base import Session
from .module import LoginModule
from .input import LoginBody, LoginHeader, LoginPath, LoginQuery, LoginInput

API_MODULE = "Auth"
router = APIRouter(tags=[API_MODULE])

@router.post("/api/auth/login", response_model=TokenBase)
def api_router(
    path: LoginPath = Depends(),
    header: LoginHeader = Depends(),
    body: LoginBody = Body(),
    query: LoginQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  LoginModule(LoginInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
