import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data_structures.linked_list import Node, SinglyLinkedList

def linked_list_cycle(head: Node) -> bool:
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add(1)
    ll.add(2)

    print("Does the linked list have a cycle? ", linked_list_cycle(ll.head))

