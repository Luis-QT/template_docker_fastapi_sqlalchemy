""" Defines the router funtion of the API Register """
from fastapi import APIRouter, Depends, Body
from app.base_schemas import UserBase
from app.connections.database import get_db
from app.db.base import Session
from .module import RegisterModule
from .input import RegisterBody, RegisterHeader, RegisterPath, RegisterQuery, RegisterInput

API_MODULE = "Auth"
router = APIRouter(tags=[API_MODULE])

@router.post("/apis/auth/register", response_model=UserBase)
def api_router(
    path: RegisterPath = Depends(),
    header: RegisterHeader = Depends(),
    body: RegisterBody = Body(),
    query: RegisterQuery = Depends(),
    db: Session = Depends(get_db)
    ):
    """ Instance and run the API module """
    module =  RegisterModule(RegisterInput.parse_obj({
        **path.dict(),
        **header.dict(),
        **body.dict(),
        **query.dict()
    }), db)
    return module.use_api()
