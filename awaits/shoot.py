from functools import wraps
from asyncio import sleep
from awaits.room_keeper import RoomKeeper
from awaits.common_data import CommonData
from awaits.errors import IncorrectUseOfTheDecoratorError


def shoot(*args, pool=None):
    def wrapper_of_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pool_name = 'base' if pool is None else pool
            task = RoomKeeper().room[pool_name].do(func, *args, **kwargs)
            return task
        return wrapper
    # Определяем, как вызван декоратор - как фабрика декораторов (т. е. без позиционных аргументов) или как непосредственный декоратор.
    if not len(args):
        return wrapper_of_wrapper
    elif len(args) == 1 and callable(args[0]):
        return wrapper_of_wrapper(args[0])
    raise IncorrectUseOfTheDecoratorError('You used the awaitable decorator incorrectly. Read the documentation.')
