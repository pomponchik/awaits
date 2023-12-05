from functools import wraps
from asyncio import sleep

from awaits.common_data import CommonData
from awaits.utils.get_pool_for_decorator import get_pool_for_decorator
from awaits.utils.end_of_wrappers import end_of_wrappers


def awaitable(*args, pool=None, delay=None):
    pool = get_pool_for_decorator(pool)

    def wrapper_of_wrapper(function):
        @wraps(function)
        async def wrapper(*args, **kwargs):
            sleep_time = CommonData().delay if delay is None else delay
            task = pool.do(function, *args, **kwargs)
            while not task.done:
                await sleep(sleep_time)
            if task.error:
                raise task.exception
            return task.result
        return wrapper

    return end_of_wrappers(args, wrapper_of_wrapper)
