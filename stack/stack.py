from typing import Optional


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self) -> Optional[int]:
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self) -> int:
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
