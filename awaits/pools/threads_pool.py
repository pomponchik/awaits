from queue import Queue
from threading import Thread

from awaits.units.abstract_unit import AbstractUnit
from awaits.units.thread_unit import ThreadUnit
from awaits.pools.abstract_pool import AbstractPool


class ThreadsPool(AbstractPool):
    def get_queue(self) -> Queue:
        return Queue()

    def create_worker(self, index: int) -> AbstractUnit:
        worker = Thread(target=ThreadUnit(self.queue, self, index).run)
        worker.daemon = True
        worker.start()
        return worker
