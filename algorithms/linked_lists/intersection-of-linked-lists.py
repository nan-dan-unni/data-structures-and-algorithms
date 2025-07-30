import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data_structures.linked_list import Node, SinglyLinkedList

def intersection_of_linked_lists(head1: Node, head2: Node) -> int:
    current1 = head1
    current2 = head2
    len1 = 0
    len2 = 0
    while current1 is not None:
        len1 += 1
        current1 = current1.next
    while current2 is not None:
        len2 += 1
        current2 = current2.next
    
    current1 = head1
    current2 = head2
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            current2 = current2.next
    while current1 and current2:
        if current1 is current2:
            return current1.data
        current2 = current2.next
        current1 = current1.next
    return None


if __name__ == "__main__":
    ll1 = SinglyLinkedList(1,2,3)
    ll2 = SinglyLinkedList(-1,-2)
    beforenode = ll2.add(-3)
    intnode = ll1.add(4)
    ll1.add(5)
    ll1.add(6)
    beforenode.next = intnode
    print(ll1)
    print(ll2)
    print(intersection_of_linked_lists(ll1.head, ll2.head))
