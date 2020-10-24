from queue import Queue
from threading import Thread
from awaits.thread_unit import ThreadUnit
from awaits.task import Task


class ThreadsPool:
    def __init__(self, pool_size):
        self.active = False
        self.pool_size = pool_size
        self.queue = Queue()
        self.workers = [Thread(target=ThreadUnit(self.queue, self, index).run) for index in range(self.pool_size)]
        for worker in self.workers:
            worker.daemon = True
            worker.start()
        self.active = True

    def do(self, function, *args, **kwargs):
        task = Task(function, *args, **kwargs)
        self.queue.put_nowait(task)
        return task

    def queue_size(self):
        """
        ПРИМЕРНЫЙ размер очереди, см. документацию:
        https://docs.python.org/3/library/queue.html#queue.Queue.qsize
        """
        size = self.queue.qsize()
        return size

    def __len__(self):
        return self.pool_size

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise ValueError('Key must be an integer number.')
        if index > len(self):
            raise IndexError(f'Lenth of the pool is equal {len(self)}.')
        return self.workers[index]

    def __repr__(self):
        return f'ThreadsPool({len(self)})'

    def __str__(self):
        active = 'active' if self.active else 'not active'
        return f'<pool of {len(self)} threads, {active}>'
