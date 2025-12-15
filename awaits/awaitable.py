from asyncio import sleep
from functools import wraps
from typing import Awaitable, Callable, Optional, Union

from awaits.config import config
from awaits.pools.abstract_pool import AbstractPool
from awaits.types import FunctionParameters, FunctionResult
from awaits.utils.end_of_wrappers import end_of_wrappers
from awaits.utils.get_pool_for_decorator import get_pool_for_decorator


def awaitable(*args: Callable[FunctionParameters, FunctionResult], pool: Optional[Union[str, AbstractPool]] = None, delay: Optional[Union[int, float]] = None) -> Union[Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Awaitable[FunctionResult]]], Callable[FunctionParameters, Awaitable[FunctionResult]]]:
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(function: Callable[FunctionParameters, FunctionResult]) -> Callable[FunctionParameters, Awaitable[FunctionResult]]:
        @wraps(function)
        async def wrapper(*args: FunctionParameters.args, **kwargs: FunctionParameters.kwargs) -> FunctionResult:
            sleep_time = config.delay if delay is None else delay
            task = pool.do(function, *args, **kwargs)
            while not task.done:  # noqa: ASYNC110
                await sleep(sleep_time)
            if task.error:
                raise task.exception  # type: ignore[misc]
            return task.result  # type: ignore[return-value]
        return wrapper

    return end_of_wrappers(args, wrapper_of_wrapper)
