""" Init seeders """
from app.db.seeders.users import generate_users

def run_seeds(db):
    """ Run seed """
    generate_users(db)
