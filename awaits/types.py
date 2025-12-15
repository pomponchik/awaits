# noqa: A005
from typing import TypeVar

try:
    from typing import ParamSpec
except ImportError:
    from typing_extensions import ParamSpec  # type: ignore[assignment]

P = ParamSpec('P')
R = TypeVar('R')
