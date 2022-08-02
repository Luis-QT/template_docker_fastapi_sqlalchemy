""" API Module """
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from app.apis.auth.login.flow import FlowLogin
from app.apis.auth.login.validator import ValidatorLogin
from app.base_schemas import TokenBase
from app.connections.database import get_db

router = APIRouter(prefix="/api/auth")

@router.post("/login", response_model=TokenBase)
def api_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    language: Optional[str] = Header("EN")
):
    """ Create token rtc """
    request = {
        'username': form_data.username,
        'password': form_data.password,
        'db': db,
        'language': language
    }
    ValidatorLogin(request).run()
    return FlowLogin(request).run()
