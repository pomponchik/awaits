import pytest

from awaits.pools.threads_pool import ThreadsPool


def test_create_pull_with_zero_workers():
    with pytest.raises(ValueError):
        ThreadsPool(0)


def test_len_of_pool():
    assert len(ThreadsPool(5)) == 5


def test_repr_of_pool():
    assert repr(ThreadsPool(5)) == 'ThreadsPool(5)'


def test_str_of_pool():
    pool = ThreadsPool(5)

    assert str(pool) == f'<ThreadsPool pool object of 5 workers #{id(pool)}>'
