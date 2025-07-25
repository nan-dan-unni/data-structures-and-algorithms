import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data_structures.linked_list import  SinglyLinkedList, Node

def remove_nth_node_from_end(ll: SinglyLinkedList, n: int) -> SinglyLinkedList:
    dummy = Node(0)
    dummy.next = ll.head
    current = dummy
    pilot = dummy
    for _ in range(n+1):
        if pilot is not None:
            pilot = pilot.next
        else:
            print("Couldn't find the position")
            return ll
    while pilot is not None:
        pilot = pilot.next
        current = current.next
    if current is not None:
        if current.next is not None:
            current.next = current.next.next
    ll.head = dummy.next
    return ll

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    print(ll)
    ll = remove_nth_node_from_end(ll, n=1)
    print(ll)