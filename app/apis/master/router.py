""" Master APIs router """
from fastapi import APIRouter
from app.connections import database

router = APIRouter(
    prefix="/api/master"
)

@router.get("/database/refresh_db")
def refresh_db():
    """ Reset models and seeders """
    database.refresh_db()
    return "DB refreshed"
