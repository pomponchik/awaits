from threading import Lock
from typing import Dict

from awaits.pools.threads_pool import ThreadsPool


class ThreadsPoolsRoom:
    def __init__(self, pool_size: int) -> None:
        self.pool_size: int = pool_size
        self.pools: Dict[str, ThreadsPool] = {}
        self.lock: Lock = Lock()

    def __getitem__(self, key: str) -> ThreadsPool:
        if not isinstance(key, str):
            raise KeyError(f'Key of the pools room must be a string, not {key.__class__.__name__}.')
        with self.lock:
            if key not in self.pools:
                self.pools[key] = ThreadsPool(self.pool_size)
            return self.pools[key]

    def __len__(self) -> int:
        return len(self.pools)
