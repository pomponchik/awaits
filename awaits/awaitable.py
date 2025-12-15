from asyncio import sleep
from functools import wraps
from typing import Any, Awaitable, Callable, Optional, Union

from awaits.config import config
from awaits.pools.abstract_pool import AbstractPool
from awaits.utils.end_of_wrappers import end_of_wrappers
from awaits.utils.get_pool_for_decorator import get_pool_for_decorator


def awaitable(*args: Callable[[Any], Any], pool: Optional[Union[str, AbstractPool]] = None, delay: Optional[Union[int, float]] = None) -> Union[Callable[[Callable[..., Any]], Callable[..., Awaitable[Any]]], Callable[..., Awaitable[Any]]]:
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(function: Callable[..., Any]) -> Callable[..., Awaitable[Any]]:
        @wraps(function)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            sleep_time = config.delay if delay is None else delay
            task = pool.do(function, *args, **kwargs)
            while not task.done:  # noqa: ASYNC110
                await sleep(sleep_time)
            if task.error:
                raise task.exception  # type: ignore[misc]
            return task.result
        return wrapper

    return end_of_wrappers(args, wrapper_of_wrapper)
