from task_manager.task_manager import add_stuff


def test_add_stuff():
    stuff = add_stuff(1,2)

    assert stuff == 3