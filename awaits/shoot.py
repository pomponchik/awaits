from functools import wraps
from awaits.utils.get_pool_for_decorator import get_pool_for_decorator
from awaits.utils.end_of_wrappers import end_of_wrappers


def shoot(*args, pool=None):
    pool = get_pool_for_decorator(pool)
    def wrapper_of_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            task = pool.do(func, *args, **kwargs)
            return task
        return wrapper
    return end_of_wrappers(args, wrapper_of_wrapper)
