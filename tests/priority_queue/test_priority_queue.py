from ting_file_management.priority_queue import PriorityQueue
# import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()

    file = [
        {"qtd_linhas": 2},
        {"qtd_linhas": 3},
        {"qtd_linhas": 8},
    ]

    for f in file:
        pq.enqueue(f)

    assert len(pq) == len(file)
    assert pq.search(0) == file[0]
    assert pq.search(1) == file[1]
    assert pq.search(2) == file[2]
    pq.dequeue()
    assert pq.search(0) == file[2]

    # with pytest.assertRaises(IndexError):
    #     pq.search(4)

    # assert pq.search(1) == file[2]

    # if pq.high_priority or pq.regular_priority:
    #     assert len(pq) == len(file)
    # else:
    #     assert False, "A fila está vazia!"
