"""stack_client"""
from stack import Stack
from typing import Any


def list_stack(l: list, s: Stack) -> None:
    """do the following things mentioed in the lab"""
    for element in l:
        s.add(element)
    while not s.is_empty():
        b = s.remove()
        if not isinstance(b, list):
            print(b)
        else:
            for element in b:
                s.add(element)


if __name__ == '__main__':
    s = Stack()
    a = ''
    while a != 'end':
        a = input('Type a string')
        s.add(a)
    while not s.is_empty():
        print(s.remove())


