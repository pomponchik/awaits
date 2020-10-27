from awaits.errors import IncorrectUseOfTheDecoratorError


def end_of_wrappers(args, wrapper):
    """
    Определяем, как вызван декоратор - как фабрика декораторов (т. е. без позиционных аргументов) или как непосредственный декоратор.
    """
    if not len(args):
        return wrapper
    elif len(args) == 1 and callable(args[0]):
        return wrapper(args[0])
    raise IncorrectUseOfTheDecoratorError('You used the awaitable decorator incorrectly. Read the documentation.')
