import pytest
from full_match import match

from awaits import config


def test_set_incompatible_typed_variable():
    with pytest.raises(TypeError, match=match("The value 'kek' (str) of the \"pool_size\" field does not match the type int.")):
        config.pool_size = 'kek'

    with pytest.raises(TypeError, match=match('The value \'kek\' (str) of the "delay" field does not match the type Union.')):
        config.delay = 'kek'
