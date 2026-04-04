from typing import Generic, Optional, TypeVar


T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item: T):
        self.items.append(item)

    def dequeue(self) -> Optional[T]:
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self) -> Optional[T]:
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.size() == 0
