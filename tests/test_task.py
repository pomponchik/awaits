from awaits.task import Task


def test_run_simple_function():
    value = 777

    def function():
        return value

    task = Task(function)

    assert task.done == False
    assert task.result is None
    assert task.error == False
    assert task.exception is None

    task.do()

    assert task.done == True
    assert task.result == value
    assert task.error == False
    assert task.exception is None


def test_run_function_with_arguments():
    first_value = 777
    second_value = 999
    third_value = 5

    def function(a, b, c=third_value):
        return a + b + c

    task = Task(function, first_value, second_value, c=third_value)

    assert task.done == False
    assert task.result is None
    assert task.error == False
    assert task.exception is None

    task.do()

    assert task.done == True
    assert task.result == first_value + second_value + third_value
    assert task.error == False
    assert task.exception is None


def test_run_function_that_raise_exception():
    first_value = 777
    second_value = 999
    third_value = 5

    def function(a, b, c=third_value):
        raise ValueError

    task = Task(function, first_value, second_value, c=third_value)

    assert task.done == False
    assert task.result is None
    assert task.error == False
    assert task.exception is None

    task.do()

    assert task.done == True
    assert task.result == None
    assert task.error == True
    assert isinstance(task.exception, ValueError)
