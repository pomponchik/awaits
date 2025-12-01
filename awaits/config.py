from typing import Union

from skelet import Storage, Field, for_tool


class Config(Storage, sources=for_tool('my_tool_name')):
    pool_size: int = Field(10, validation=lambda x: x > 0)
    delay: Union[int, float] = Field(0.001, validation=lambda x: x >= 0)

config = Config()
