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
        temp: Optional[ListNode] = self.head

        while temp.next != None:
            if temp.next.val == node.val:
                break
            temp = temp.next

        temp.next = temp.next.next
