from abc import ABC, abstractmethod
from typing import List, Callable, Any, Optional

try:
    from functools import cached_property  # type: ignore[attr-defined]
except ImportError:
    from cached_property import cached_property  # type: ignore[import-not-found, no-redef, unused-ignore]

from awaits.task import Task
from awaits.protocols.queue import QueueProtocol
from awaits.units.abstract_unit import AbstractUnit


class AbstractPool(ABC):
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError('The size of the pool must be greater than zero.')

        self.size = size
        self.workers = self.create_workers()

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({len(self)})'

    def __str__(self) -> str:
        return f'<{self.__class__.__name__} pool object of {len(self)} workers #{id(self)}>'

    def __getitem__(self, index: int) -> AbstractUnit:
        if not isinstance(index, int):
            raise ValueError('Key must be an integer number.')
        if index >= len(self) or index < 0:
            raise IndexError(f'The size of the pool is equal {len(self)}.')
        return self.workers[index]

    @cached_property
    def queue(self) -> QueueProtocol:
        return self.get_queue()

    def do(self, function: Callable[[Any], Any], *args: Any, **kwargs: Any) -> Task:
        task = Task(function, *args, **kwargs)
        self.queue.put_nowait(task)
        return task

    def create_workers(self, number_of_workers: Optional[int] = None, base_number: int = 0) -> List[AbstractUnit]:
        pool_size = self.size if number_of_workers is None else number_of_workers
        workers = []

        for number in range(base_number, pool_size):
            worker = self.create_worker(number)
            workers.append(worker)
        return workers

    @abstractmethod
    def get_queue(self) -> QueueProtocol:
        ... # pragma: no cover

    @abstractmethod
    def create_worker(self, index: int) -> AbstractUnit:
        ... # pragma: no cover
