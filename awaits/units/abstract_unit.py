from abc import ABC, abstractmethod

from awaits.protocols.queue import QueueProtocol


class AbstractUnit(ABC):
    def __init__(self, queue: QueueProtocol, pool: 'AbstractPool', index: int) -> None:  # type: ignore[name-defined] # noqa: F821
        self.index = index
        self.queue = queue
        self.pool = pool
        self.activate()

    @abstractmethod
    def activate(self) -> None:
        ... # pragma: no cover

    @abstractmethod
    def run(self) -> None:
        ... # pragma: no cover
