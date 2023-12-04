from asyncio import run
from threading import get_ident

import pytest

from awaits import awaitable
from awaits.errors import IncorrectUseOfTheDecoratorError
from awaits.room_keeper import RoomKeeper


def test_await_awaitable_function_without_brackets_without_arguments():
    value = 777

    @awaitable
    def function():
        return value

    assert run(function()) == value


def test_await_awaitable_function_without_brackets_without_arguments_raise_exception():
    @awaitable
    def function():
        raise ValueError

    with pytest.raises(ValueError):
        run(function())


def test_check_thread_id():
    @awaitable
    def function():
        return get_ident()

    assert run(function()) != get_ident()


def test_await_awaitable_function_without_brackets_with_arguments():
    first_value = 777
    second_value = 999
    third_value = 5
    forth_value = 17

    @awaitable
    def function(a, b, c=third_value):
        return a + b + c

    assert run(function(first_value, second_value)) == first_value + second_value + third_value
    assert run(function(first_value, second_value, c=forth_value)) == first_value + second_value + forth_value


def test_await_awaitable_function_with_empty_brackets_without_arguments():
    value = 777

    @awaitable()
    def function():
        return value

    assert run(function()) == value


def test_await_awaitable_function_with_empty_brackets_with_arguments():
    first_value = 777
    second_value = 999
    third_value = 5
    forth_value = 17

    @awaitable()
    def function(a, b, c=third_value):
        return a + b + c

    assert run(function(first_value, second_value)) == first_value + second_value + third_value
    assert run(function(first_value, second_value, c=forth_value)) == first_value + second_value + forth_value


def test_await_awaitable_function_with_brackets_and_pool_name_without_arguments():
    value = 777

    @awaitable(pool='kek')
    def function():
        return value

    assert run(function()) == value


def test_await_awaitable_function_with_brackets_and_wrong_pool_object_without_arguments():
    value = 777

    with pytest.raises(IncorrectUseOfTheDecoratorError):
        @awaitable(pool=5)
        def function():
            return value


def test_await_awaitable_function_with_brackets_and_pool_object_without_arguments():
    value = 777
    pool = RoomKeeper().room['test_await_awaitable_function_with_brackets_and_pool_object_without_arguments']

    @awaitable(pool=pool)
    def function():
        return value

    assert run(function()) == value


def test_await_awaitable_function_with_brackets_and_pool_object_without_arguments():
    value = 777
    pool = RoomKeeper().room['test_await_awaitable_function_with_brackets_and_pool_object_without_arguments']

    @awaitable(pool=pool)
    def function():
        return value

    assert run(function()) == value
