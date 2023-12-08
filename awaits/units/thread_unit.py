from awaits.units.abstract_unit import AbstractUnit


class ThreadUnit(AbstractUnit):
    """
    Экземпляр класса соответствует одному потоку. Здесь выполняются таски.
    """
    def run(self) -> None:
        """
        Принимаем из очереди таски и выполняем их.
        """
        while True:
            try:
                task = self.queue.get()
                task()
            finally:
                self.queue.task_done()
