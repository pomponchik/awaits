from awaits.config import config
from awaits.threads_pools_room import ThreadsPoolsRoom


class RoomKeeper:
    def __init__(self) -> None:
        if not hasattr(self, 'room'):
            pool_size = config.pool_size
            self.room = ThreadsPoolsRoom(pool_size)

    def __new__(cls) -> 'RoomKeeper':
        if not hasattr(cls, 'instance'):
            cls.instance = super(RoomKeeper, cls).__new__(cls)
        return cls.instance
