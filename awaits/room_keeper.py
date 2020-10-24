from awaits.common_data import CommonData
from awaits.threads_pools_room import ThreadsPoolsRoom


class RoomKeeper:
    def __init__(self):
        if not hasattr(self, 'room'):
            pool_size = CommonData().pool_size
            self.room = ThreadsPoolsRoom(pool_size)

    def __new__(cls, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RoomKeeper, cls).__new__(cls)
        return cls.instance
