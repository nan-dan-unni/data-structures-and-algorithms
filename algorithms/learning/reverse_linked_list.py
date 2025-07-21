import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data_structures.linked_list import SinglyLinkedList

def reverse_linked_list(ll: SinglyLinkedList) -> SinglyLinkedList:
    current = ll.head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        if next is None:
            ll.head = current
        current = next
    return ll


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    print(ll)
    ll = reverse_linked_list(ll)
    print(ll)
