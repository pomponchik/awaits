from queue import Queue
from threading import Thread

from awaits.units.abstract_unit import AbstractUnit
from awaits.units.thread_unit import ThreadUnit
from awaits.pools.abstract_pool import AbstractPool


class ThreadsPool(AbstractPool):
    def get_queue(self) -> Queue:
        return Queue()

    def get_where_to_execute(self):
        return Thread

    def get_worker_class(self):
        return ThreadUnit

    def activate_workers(self, workers=None):
        if not workers:
            workers = self.workers
        for worker in workers:
            worker.daemon = True
            worker.start()

    def create_worker(self, index: int) -> AbstractUnit:
        where = self.get_where_to_execute()
        worker_class = self.get_worker_class()
        worker = where(target=worker_class(self.queue, self, index).run)
        return worker
