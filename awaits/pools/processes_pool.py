from multiprocessing import Process, Queue, current_process
import time
from awaits.units.process_unit import ProcessUnit
from awaits.pools.abstract_pool import AbstractPool


def test():
    print('hello')

class ProcessesPool(AbstractPool):
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
        return Process

    def get_worker_class(self):
        return ProcessUnit

    def put_to_queue(self, task):
        function = task.function
        function_name = function.__name__
        function_module = function.__module__
        subtask = {'function_name': function_name, 'function_module': function_module, 'args': task.args, 'kwargs': task.kwargs}
        self.queue.put(subtask)

    def activate_workers(self, workers=None):
        if workers is None:
            workers = self.workers
        if current_process().name != 'MainProcess':
            return
        for worker in workers:
            #time.sleep(3)
            worker.daemon = True
            worker.start()
        #raise ValueError


    def create_worker(self, index):
        worker = Process(target=test, args=())
        #print(worker)
        return worker
