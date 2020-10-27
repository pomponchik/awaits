from awaits.pools.threads_pool import ThreadsPool


class ThreadsPoolsRoom:
    def __init__(self, pool_size):
        self.pool_size = pool_size
        self.pools = {}

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError(f'Key of the pools room must be a string, not {key.__class__.__name__}.')
        if key not in self.pools:
            self.pools[key] = ThreadsPool(self.pool_size)
        return self.pools[key]

    def __len__(self):
        return len(self.pools)
