from threading import Thread

from awaits.units.abstract_unit import AbstractUnit


class ThreadUnit(AbstractUnit):
    """
    Экземпляр класса соответствует одному потоку. Здесь выполняются таски.
    """
    def activate(self) -> None:
        self.thread = Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

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
