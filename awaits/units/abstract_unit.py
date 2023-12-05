from abc import ABC, abstractmethod

from awaits.protocols.queue import QueueProtocol


class AbstractUnit(ABC):
    def __init__(self, queue: QueueProtocol, pool: 'AbstractPool', index: int) -> None:
        self.index = index
        self.queue = queue
        self.pool = pool

    @abstractmethod
    def run(self) -> None:
        ... # pragma: no cover
