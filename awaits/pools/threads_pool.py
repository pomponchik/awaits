from queue import Queue
from threading import Thread
from awaits.units.thread_unit import ThreadUnit
from awaits.pools.abstract_pool import AbstractPool


class ThreadsPool(AbstractPool):
    def queue_size(self):
        """
        ПРИМЕРНЫЙ размер очереди, см. документацию:
        https://docs.python.org/3/library/queue.html#queue.Queue.qsize
        """
        size = self.queue.qsize()
        return size

    def get_queue_class(self):
        return Queue

    def get_where_to_execute(self):
        return Thread

    def get_worker_class(self):
        return ThreadUnit

    def put_to_queue(self, task):
        self.queue.put_nowait(task)

    def activate_workers(self, workers=None):
        if not workers:
            workers = self.workers
        for worker in workers:
            worker.daemon = True
            worker.start()

    def create_worker(self, index):
        where = self.get_where_to_execute()
        worker_class = self.get_worker_class()
        worker = where(target=worker_class(self.queue, self, index).run)
        return worker
