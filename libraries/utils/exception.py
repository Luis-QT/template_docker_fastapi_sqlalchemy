""" Exception utilities """
from fastapi import HTTPException

def dao_exception(status_code, field: str, msg: str):
    """ Return exception generate in DAO """
    return HTTPException(
        status_code=status_code,
        detail=[{
            "loc": ["body", field],
            "msg": msg,
            "type": "dao"
        }]
    )

def request_exception(status_code, field: str, msg: str, loc_in="body"):
    """ Return exception generate in Request """
    return HTTPException(
        status_code=status_code,
        detail=[{
            "loc": [loc_in, field],
            "msg": msg,
            "type": "request"
        }]
    )
