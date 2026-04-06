from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class ListNode(Generic[T]):
    def __init__(self, val=None, next=None) -> None:
        self.val:Optional[T] = val
        self.next: Optional[ListNode] = next
