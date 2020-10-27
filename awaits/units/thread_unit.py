from awaits.units.abstract_unit import AbstractUnit


class ThreadUnit(AbstractUnit):
    """
    Экземпляр класса соответствует одному потоку. Здесь выполняются таски.
    """
    def __init__(self, queue, pool, index):
        self.index = index
        self.queue = queue
        self.pool = pool

    def run(self):
        """
        Принимаем из очереди таски и выполняем их.
        """
        while True:
            try:
                task = self.queue.get()
                task.do()
                self.queue.task_done()
            except Exception as e:
                pass
