from threading import active_count

import pytest
from full_match import match

from awaits.pools.threads_pool import ThreadsPool
from awaits.units.thread_unit import ThreadUnit


def test_create_pull_with_zero_workers():
    with pytest.raises(ValueError, match=match("The size of the pool must be greater than zero.")):
        ThreadsPool(0)


def test_len_of_pool():
    assert len(ThreadsPool(5)) == 5


def test_repr_of_pool():
    assert repr(ThreadsPool(5)) == 'ThreadsPool(5)'


def test_str_of_pool():
    pool = ThreadsPool(5)

    assert str(pool) == f'<ThreadsPool pool object of 5 workers #{id(pool)}>'


def test_getitem_with_wrong_index():
    pool = ThreadsPool(5)

    with pytest.raises(IndexError):
        pool[-1]

    with pytest.raises(IndexError):
        pool[5]

    with pytest.raises(IndexError):
        pool[6]

    with pytest.raises(IndexError):
        pool[150]

    with pytest.raises(ValueError, match=match("Key must be an integer number.")):
        pool['kek']


def test_getitem_with_good_index():
    pool = ThreadsPool(5)

    assert isinstance(pool[0], ThreadUnit)


def test_threads_was_really_created():
    number_of_threads_before = active_count()
    number_of_creating_threads = 5

    pool = ThreadsPool(number_of_creating_threads)  # noqa: F841

    assert active_count() == number_of_threads_before + number_of_creating_threads
