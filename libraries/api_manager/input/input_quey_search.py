""" Define a class that has search API attributes"""
from pydantic import validator, BaseModel
from fastapi import Query
from libraries.utils.exception import request_exception

class InputQuerySearch(BaseModel):
    """ Class that has search API attributes"""
    page: int = Query(
        "1",
        title="query page",
        description="Number page",
    )
    limit: int = Query(
        "10",
        title="query limit",
        description="Regiters per page",
    )
    search: str = ""
    sort: str = Query(
        "created_at",
        title="query sort",
        description="Sort the search using 'created_at'"
    )
    order: str = Query(
        "asc",
        title="query order",
        description="Order the search using 'asc' or 'desc'"
    )

    @validator('page')
    def min_max_page(cls, value):
        """ Validate min max page """
        if value < 1 or value > 200:
            raise request_exception(
                422, 'limit', 'Página fuera del limite',
                loc_in='query'
            )
        return value

    @validator('limit')
    def min_max_limit(cls, value):
        """ Validate min max limit """
        if value < 0 or value > 500:
            raise request_exception(
                422, 'limit', 'La cantidad de registros permitidos por página es de 0 a 500',
                loc_in='query'
            )
        return value

    @validator('sort')
    def sort_allowed_values(cls, value):
        """ Validate sort allowed values """
        if value not in ['created_at']:
            raise request_exception(
                422, 'sort', 'Solo le permiten los valores "created_at"',
                loc_in='query'
            )
        return value

    @validator('order')
    def order_allowed_values(cls, value):
        """ Validate order allowed values """
        if value not in ['asc', 'desc']:
            raise request_exception(
                422, 'order', 'Solo le permiten los valores "asc" y "desc"',
                loc_in='query'
            )
        return value
