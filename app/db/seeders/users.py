"""" File to generate dancers data """
from sqlalchemy.orm import Session
from app.db.models import User
from libraries.utils.crypto import hash_password
from libraries.utils.avatar import generate_avatar_url

def generate_users(db: Session):
    """ Creating users fake """
    user = User(
        name='admin',
        username='admin',
        email='admin@admin.com',
        password=hash_password('123456'),
        avatar_url=generate_avatar_url('admin')
    )
    db.add(user)
    db.commit()
