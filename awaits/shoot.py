from functools import wraps
from typing import Awaitable, Callable, Optional, Union

from awaits.pools.abstract_pool import AbstractPool
from awaits.task import Task
from awaits.types import FunctionParameters, FunctionResult
from awaits.utils.end_of_wrappers import end_of_wrappers
from awaits.utils.get_pool_for_decorator import get_pool_for_decorator


def shoot(*args: Callable[FunctionParameters, FunctionResult], pool: Optional[Union[str, AbstractPool]] = None) -> Union[Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Awaitable[FunctionResult]]], Callable[FunctionParameters, Awaitable[FunctionResult]], Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Task]]]:  # type: ignore[valid-type, unused-ignore]
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(function: Callable[FunctionParameters, FunctionResult]) -> Callable[FunctionParameters, Task]:  # type: ignore[valid-type, unused-ignore]
        @wraps(function)
        def wrapper(*args: FunctionParameters.args, **kwargs: FunctionParameters.kwargs) -> Task:
            return pool.do(function, *args, **kwargs)
        return wrapper

    return end_of_wrappers(args, wrapper_of_wrapper)
