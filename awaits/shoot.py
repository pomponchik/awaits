from functools import wraps
from typing import Union, Optional

from awaits.utils.get_pool_for_decorator import get_pool_for_decorator
from awaits.utils.end_of_wrappers import end_of_wrappers
from awaits.pools.abstract_pool import AbstractPool


def shoot(*args, pool: Optional[Union[str, AbstractPool]] = None):
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            task = pool.do(func, *args, **kwargs)
            return task
        return wrapper
    
    return end_of_wrappers(args, wrapper_of_wrapper)
