class CommonData:
    pool_size = 10
    delay = 0.01

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.__class__, key, value)

    def __new__(cls, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CommonData, cls).__new__(cls)
        return cls.instance
