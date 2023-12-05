import pytest

from awaits.pools.threads_pool import ThreadsPool


def test_create_pull_with_zero_workers():
    with pytest.raises(ValueError):
        ThreadsPool(0)
