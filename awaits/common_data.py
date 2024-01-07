from typing import Union


class CommonData:
    pool_size: int = 10
    delay: Union[int, float] = 0.01

    def __init__(self, **kwargs: Union[int, float]) -> None:
        for key, value in kwargs.items():
            setattr(self.__class__, key, value)

    def __new__(cls, **kwargs: Union[int, float]) -> 'CommonData':
        if not hasattr(cls, 'instance'):
            cls.instance = super(CommonData, cls).__new__(cls)
        return cls.instance
