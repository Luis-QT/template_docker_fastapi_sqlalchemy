""" Crypto utilities """
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    """ Hash string """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """ Compare string with hash string """
    return pwd_context.verify(plain_password, hashed_password)
