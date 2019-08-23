from functools import wraps


def make_special(function):

    @wraps(function)
    def decorator():
        val = function()
        return 'Awesome {} special.'.format(val)
    return decorator


@make_special
def something_awesome():
    """Original Function"""
    return "Python, its"


print(something_awesome())
