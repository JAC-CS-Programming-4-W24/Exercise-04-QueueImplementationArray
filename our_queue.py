
from our_array import Array


class IntQueue:

    def __init__(self, capacity: int):
        self._elements: Array[int] = Array(capacity)
        # self._front: int = -1
        self._rear: int = -1

    def enqueue(self, element: int):
        pass  # TODO

    def dequeue(self) -> int:
        pass  # TODO

    def front(self) -> int:
        pass  # TODO

    def is_empty(self) -> bool:
        pass  # TODO

    def is_full(self) -> bool:
        pass  # TODO

    def __str__(self):
        pass  # TODO

    def __repr__(self):
        pass  # TODO
