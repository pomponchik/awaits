from queue import Queue

from awaits.units.abstract_unit import AbstractUnit
from awaits.units.thread_unit import ThreadUnit
from awaits.pools.abstract_pool import AbstractPool
from awaits.task import Task


class ThreadsPool(AbstractPool):
    def get_queue(self) -> Queue[Task]:
        return Queue()

    def create_worker(self, index: int) -> AbstractUnit:
        return ThreadUnit(self.queue, self, index)
