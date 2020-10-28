from awaits.task import Task


class AbstractPool:
    def __init__(self, pool_size):
        self.active = False
        self.pool_size = pool_size
        self.queue = self.get_queue()
        self.workers = self.create_workers()
        self.activate_workers()
        self.active = True

    def get_queue(self):
        if not hasattr(self, 'queue'):
            queue_class = self.get_queue_class()
            self.queue = queue_class()
        return self.queue

    def do(self, function, *args, **kwargs):
        task = Task(function, *args, **kwargs)
        self.put_to_queue(task)
        return task

    def create_workers(self, number_of_workers=None, base_number=0):
        number_of_workers = self.pool_size if number_of_workers is None else number_of_workers
        workers = []
        for number in range(base_number, number_of_workers):
            worker = self.create_worker(number)
            workers.append(worker)
        return workers

    def create_worker(self, index):
        raise NotImplementedError('The create workers operation is not defined.')

    def activate_workers(self, workers=None):
        raise NotImplementedError('The activate workers operation is not defined.')

    def queue_size(self):
        raise NotImplementedError('The queue_size operation is not defined.')

    def get_queue_class(self):
        raise NotImplementedError('The queue class is not defined.')

    def put_to_queue(self, task):
        raise NotImplementedError('The put operation is not defined.')

    def get_where_to_execute(self):
        raise NotImplementedError('The class to execute workers is not defined.')

    def __len__(self):
        return self.pool_size

    def __repr__(self):
        return f'{self.__class__.__name__}({len(self)})'

    def __str__(self):
        active = 'active' if self.active else 'not active'
        return f'<{self.__class__.__name__} pool object of {len(self)} workers #{id(self)}, {active}>'

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise ValueError('Key must be an integer number.')
        if index > len(self):
            raise IndexError(f'Lenth of the pool is equal {len(self)}.')
        return self.workers[index]
