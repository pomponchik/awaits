# noqa: A005
from typing import TypeVar

# TODO: Delete this try-except if python version is >= 3.10.
try:
    from typing import ParamSpec  # type: ignore[attr-defined, unused-ignore]
except ImportError:  # pragma: no cover
    from typing_extensions import ParamSpec  # type: ignore[assignment, unused-ignore]

FunctionParameters = ParamSpec('FunctionParameters')
FunctionResult = TypeVar('FunctionResult')
