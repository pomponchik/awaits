from typing import Callable, Any

class Task:
    def __init__(self, function: Callable[[Any], Any], *args: Any, **kwargs: Any) -> None:
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.done = False
        self.error = False
        self.result = None
        self.exception = None

    def __call__(self) -> None:
        try:
            self.result = self.function(*(self.args), **(self.kwargs))
        except Exception as e:
            self.error = True
            self.exception = e
        self.done = True

    def __repr__(self) -> str:
        def string_wrapper(some_value):
            return f'"{some_value}"' if isinstance(some_value, str) else repr(some_value)

        function_name = self.function.__name__
        args = ', '.join([string_wrapper(x) for x in self.args])
        kwargs = ', '.join([f'{key}={string_wrapper(value)}' for key, value in self.kwargs.items()])
        content = []
        if function_name:
            content.append(function_name)
        if args:
            content.append(args)
        if kwargs:
            content.append(kwargs)
        content = ', '.join(content)
        result = f'Task({content})'
        return result
