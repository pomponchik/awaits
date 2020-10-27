from awaits.errors import IncorrectUseOfTheDecoratorError
from awaits.pools.abstract_pool import AbstractPool
from awaits.room_keeper import RoomKeeper


def get_pool_for_decorator(pool):
    if pool is None:
        return RoomKeeper().room['base']
    elif isinstance(pool, str):
        return RoomKeeper().room[pool]
    elif isinstance(pool, AbstractPool):
        return pool
    raise IncorrectUseOfTheDecoratorError('You can specify the pool by name, or pass an instance of the class inherited from AbstractPool.')
