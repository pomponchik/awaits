from awaits.common_data import CommonData


class config(object):
    """
    Установка глобальных параметров.
    """
    allowed_settings = {
        'pool_size': (int, ),
        'delay': (int, float, ),
    }

    @staticmethod
    def set(**kwargs):
        new_kwargs = {}
        for key, value in kwargs.items():
            if key not in config.allowed_settings.keys():
                raise ValueError(f'"{key}" variable is not allowed for the awaits settings.')
            allowed_types = config.allowed_settings.get(key)
            is_allowed = False
            for one in allowed_types:
                if isinstance(value, one):
                    is_allowed = True
            if not is_allowed:
                allowed_types = ', '.join(allowed_types)
                raise TypeError(f'Variable "{key}" has not one of types: {allowed_types}.')
            new_kwargs[key] = value
        CommonData(**new_kwargs)
