from awaits.units.abstract_unit import AbstractUnit


class ProcessUnit(AbstractUnit):
    """
    Экземпляр класса соответствует одному потоку. Здесь выполняются таски.
    """
    def __init__(self, queue, index):
        self.index = index
        self.queue = queue
        #self.pool = pool

    def run(self):
        """
        Принимаем из очереди таски и выполняем их.
        """
        while True:
            try:
                subtask = self.queue.get_nowait()
                #module = __import__(subtask['module'])
                #func = getattr(module, subtask['function'] + '2')
                print(subtask)
                #func(*(subtask['args']), **(subtask['kwargs']))
            except Exception as e:
                pass
