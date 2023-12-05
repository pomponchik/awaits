from abc import ABC, abstractmethod


class AbstractUnit(ABC):
    @abstractmethod
    def run(self):
        ... # pragma: no cover
