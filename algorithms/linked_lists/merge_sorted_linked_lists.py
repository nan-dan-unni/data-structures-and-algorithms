import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data_structures.linked_list import SortedLinkedList, SinglyLinkedList

def merge_sorted_linked_lists(ll1: SortedLinkedList, ll2: SortedLinkedList) -> SinglyLinkedList:
    ll3 = SinglyLinkedList()
    current1 = ll1.head
    current2 = ll2.head
    while current1 is not None or current2 is not None:
        if current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                ll3.add(current1.data)
                current1 = current1.next
            else:
                ll3.add(current2.data)
                current2 = current2.next
        elif current1 is not None:
            ll3.add(current1.data)
            current1 = current1.next
        elif current2 is not None:
            ll3.add(current2.data)
            current2 = current2.next
    return ll3
        

if __name__ == "__main__":
    ll1 = SortedLinkedList()
    ll2 = SortedLinkedList()
    # ll1.insert(8)
    # ll1.insert(6)
    # ll1.insert(4)
    ll1.insert(2)
    ll2.insert(1)
    # ll2.insert(3)
    # ll2.insert(5)
    # ll2.insert(7)
    print(ll1)
    print(ll2)
    ll3 = merge_sorted_linked_lists(ll1, ll2)
    print(ll3)