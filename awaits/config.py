from typing import Dict, Tuple, Type, Union

from awaits.common_data import CommonData


class config:
    """
    Установка глобальных параметров.
    """
    allowed_settings: Dict[str, Tuple[Union[Type[int], Type[float]], ...]] = {
        'pool_size': (int, ),
        'delay': (int, float, ),
    }

    @staticmethod
    def set(**kwargs: Union[int, float]) -> None:
        new_kwargs = {}

        for key, value in kwargs.items():
            if key not in config.allowed_settings:
                raise KeyError(f'"{key}" variable is not allowed for the awaits settings.')
            allowed_types = config.allowed_settings[key]

            is_allowed = False
            for one in allowed_types:
                if isinstance(value, one):
                    is_allowed = True

            if not is_allowed:
                if len(allowed_types) == 1:
                    raise TypeError(f'Variable "{value}" has not the type {allowed_types[0].__name__}.')
                else:
                    allowed_types_in_line = ', '.join([allowed_type.__name__ for allowed_type in allowed_types])
                    raise TypeError(f'Variable "{value}" has not one of types: {allowed_types_in_line}.')

            new_kwargs[key] = value

        CommonData(**new_kwargs)
