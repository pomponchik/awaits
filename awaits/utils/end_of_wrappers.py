from typing import Any, Callable, Tuple, Union, Awaitable

from awaits.task import Task
from awaits.errors import IncorrectUseOfTheDecoratorError
from awaits.types import FunctionParameters, FunctionResult





def end_of_wrappers(args: Tuple[Callable[FunctionParameters, FunctionResult], ...], wrapper: Union[Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Awaitable[FunctionResult]]], Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Task]]]) -> Union[Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Awaitable[FunctionResult]]], Callable[FunctionParameters, Awaitable[FunctionResult]], Callable[[Callable[FunctionParameters, FunctionResult]], Callable[FunctionParameters, Task]]]:
    """
    Определяем, как вызван декоратор - как фабрика декораторов (т. е. без позиционных аргументов) или как непосредственный декоратор.
    """
    if not len(args):
        return wrapper
    if len(args) == 1 and callable(args[0]):
        return wrapper(args[0])  # type: ignore[return-value]
    raise IncorrectUseOfTheDecoratorError('You used the awaitable decorator incorrectly. Read the documentation.')
