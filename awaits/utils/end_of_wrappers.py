from typing import Any, Callable, Tuple, Union

from awaits.errors import IncorrectUseOfTheDecoratorError
from awaits.types import P


def end_of_wrappers(args: Tuple[Callable[P, Any], ...], wrapper: Callable[[Callable[P, Any]], Callable[P, Any]]) -> Union[Callable[[Callable[P, Any]], Callable[P, Any]], Callable[P, Any]]:
    """
    Определяем, как вызван декоратор - как фабрика декораторов (т. е. без позиционных аргументов) или как непосредственный декоратор.
    """
    if not len(args):
        return wrapper
    if len(args) == 1 and callable(args[0]):
        return wrapper(args[0])
    raise IncorrectUseOfTheDecoratorError('You used the awaitable decorator incorrectly. Read the documentation.')
