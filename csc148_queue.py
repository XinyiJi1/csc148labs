"""
queue class materials
"""
from typing import Any


class Queue:
    """first item in is first item out"""

    def __init__(self) -> None:
        """creat a new instance of Queue
        >>> q = Queue()
        """
        self._container = []

    def add(self, element: Any) -> None:
        """add the element at the end of the Queue
        >>> q = Queue()
        >>> q.add(1)
        """
        self._container.append(element)

    def remove(self) -> Any:
        """remove and return the object at the beginning of the queue
        >>> q = Queue()
        >>> q.add(1)
        >>> q.add(20)
        >>> q.add(4)
        >>> q.remove()
        1
        >>> q.remove()
        20
        """
        return self._container.pop(0)

    def is_empty(self) -> bool:
        """return True if this queue is empty, False otherwise
        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.add('a')
        >>> q.is_empty()
        False
        """
        return self._container == []


if __name__ == '__main__':
    import doctest
    doctest.testmod()

