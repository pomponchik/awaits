from abc import ABC, abstractmethod
from typing import List

try:
    from functools import cached_property
except ImportError:
    from functools import lru_cache
    
    def cached_property(method):
        return property(lru_cache(method))

from awaits.task import Task


class AbstractPool(ABC):
    def __init__(self, pool_size: int) -> None:
        self.active = False
        self.pool_size = pool_size
        self.workers = self.create_workers()
        self.activate_workers()
        self.active = True

    def __len__(self) -> int:
        return self.pool_size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({len(self)})'

    def __str__(self) -> str:
        active = 'active' if self.active else 'not active'
        return f'<{self.__class__.__name__} pool object of {len(self)} workers #{id(self)}, {active}>'

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise ValueError('Key must be an integer number.')
        if index >= len(self) or index < 0:
            raise IndexError(f'The size of the pool is equal {len(self)}.')
        return self.workers[index]

    @cached_property
    def queue(self):
        self.get_queue()

    def get_queue(self):
        ... # pragma: no cover

    def do(self, function, *args, **kwargs):
        task = Task(function, *args, **kwargs)
        self.put_to_queue(task)
        return task

    def create_workers(self, number_of_workers=None, base_number=0) -> List:
        number_of_workers = self.pool_size if number_of_workers is None else number_of_workers
        workers = []
        for number in range(base_number, number_of_workers):
            worker = self.create_worker(number)
            workers.append(worker)
        return workers

    @abstractmethod
    def create_worker(self, index: int):
        ... # pragma: no cover

    @abstractmethod
    def activate_workers(self, workers=None):
        ... # pragma: no cover

    @abstractmethod
    def queue_size(self) -> int:
        ... # pragma: no cover

    @abstractmethod
    def put_to_queue(self, task: Task) -> None:
        ... # pragma: no cover

    @abstractmethod
    def get_where_to_execute(self):
        ... # pragma: no cover
