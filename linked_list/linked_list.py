from typing import Optional
from linked_list.list_node import ListNode


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, head:ListNode, val:int) -> Optional[ListNode]:
        node:ListNode = ListNode(val)
        node.next = head
        return node

    def delete_node(self, node:ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next

    def length(self, head:ListNode) -> int:
        if not head:
            return 0
        count: int = 1
        while head.next != None:
            count += 1
            head = head.next

        return count

    def search_key(self, head:ListNode, key: int) -> bool:
        temp: ListNode = head
        while temp != None:
            if temp.val == key:
                return True
            temp = temp.next
        return False
