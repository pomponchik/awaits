from queue import Queue
from awaits import shoot


def test_simple_shoot():
    queue = Queue()
    lst = []

    @shoot
    def function():
        for number in range(100):
            lst.append(number)
        queue.put(None)

    function()
    queue.get()

    assert len(lst) == 100
