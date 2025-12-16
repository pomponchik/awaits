# noqa: A005
from typing import TypeVar

try:
    from typing import ParamSpec  # type: ignore[attr-defined]
except ImportError:
    from typing_extensions import ParamSpec  # type: ignore[assignment]

FunctionParameters = ParamSpec('FunctionParameters')
FunctionResult = TypeVar('FunctionResult')
