from functools import wraps
from typing import Awaitable, Callable, Union, Optional, Any

from awaits.utils.get_pool_for_decorator import get_pool_for_decorator
from awaits.utils.end_of_wrappers import end_of_wrappers
from awaits.pools.abstract_pool import AbstractPool
from awaits.task import Task


def shoot(*args: Callable[[Any], Any], pool: Optional[Union[str, AbstractPool]] = None) -> Union[Callable[[Callable[[Any], Any]], Callable[[Any], Awaitable[Any]]], Callable[[Any], Awaitable[Any]]]:
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(function: Callable[[Any], Any]) -> Callable[[Any], Task]:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Task:
            task = pool.do(function, *args, **kwargs)
            return task
        return wrapper

    return end_of_wrappers(args, wrapper_of_wrapper)
