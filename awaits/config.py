from typing import Union

from skelet import Field, Storage, for_tool


class Config(Storage, sources=for_tool('my_tool_name')):
    pool_size: int = Field(10, validation=lambda x: x > 0)  # type: ignore[assignment]
    delay: Union[int, float] = Field(0.001, validation=lambda x: x >= 0)  # type: ignore[assignment]

config = Config()
