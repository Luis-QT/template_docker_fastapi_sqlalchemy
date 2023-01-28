""" Paginator """

def paginate(query, params):
    """ Paginate query """
    count = query.count()
    result = query.limit(params.limit).offset(params.limit * (params.page - 1)).all()

    return count, result
