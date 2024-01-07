import pytest

from awaits import config


def test_set_incompatible_typed_variable():
    with pytest.raises(TypeError, match='Variable "kek" has not the type int.'):
        config.set(pool_size='kek')

    with pytest.raises(TypeError, match='Variable "kek" has not one of types: int, float.'):
        config.set(delay='kek')


def test_unknown_key_name():
    with pytest.raises(KeyError, match='"kek" variable is not allowed for the awaits settings.'):
        config.set(kek='kek')
