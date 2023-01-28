""" JWT utilities  """
import os
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from fastapi import Header
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.connections.database import get_db
from app.base_schemas import UserBase
from app.db.models import User

SECRET_KEY = os.environ['JWT_SECRET_KEY']
ALGORITHM = os.environ['JWT_ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ['JWT_ACCESS_TOKEN_EXPIRE_MINUTES'])

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    """ Generate token """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Header("Authorization"), db: Session = Depends(get_db)):
    """ Get current user """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        detoken = decode_token(token)
        if detoken['email'] is None:
            raise credentials_exception
    except (PyJWTError, ValidationError) as exception:
        raise credentials_exception from exception
    # Get model
    user= db.query(User).filter_by(
        id=detoken['id']
    ).first()
    if user is None:
        raise credentials_exception
    return UserBase(**user.as_dict())

def verify_token(token: str, db: Session):
    """ Verify Token """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")
        email: str = payload.get("email")
        if email is None:
            return False
    except (PyJWTError, ValidationError):
        return False
    user= db.query(User).filter_by(
        id=user_id
    ).first()
    if user is None:
        return False
    return True

def decode_token(token: str):
    """ Decode token """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return {
        'id': payload.get("id"),
        'email': payload.get("email"),
        'avatar_url': payload.get("avatar_url")
    }
