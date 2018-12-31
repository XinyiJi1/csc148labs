"""queue_client"""
from csc148_queue import Queue
from typing import Any


def list_queue(l: list, q: Queue) -> None:
    """do the following things mentioed in the lab"""
    for element in l:
        q.add(element)
    while not q.is_empty():
        b = q.remove()
        if not isinstance(b, list):
            print(b)
        else:
            for element in b:
                q.add(element)


if __name__ == '__main__':
    q = Queue()
    a = ''
    while a != 148:
        a = input('Type a string')
        a = int(a)
        if a != 148:
            q.add(a)
    sum = 0
    while not q.is_empty():
        sum += q.remove()
    print(sum)
