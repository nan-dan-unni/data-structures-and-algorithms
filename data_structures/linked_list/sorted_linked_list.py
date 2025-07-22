class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            return
        
        if self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data >= new_node.data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node
    
    def __remove(self, data, multiple=True):
        deleted_count = 0
        if self.head is None:
            print("List is empty")
            return 0
        
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                deleted_count += 1
                if not multiple: return
            else: prev = current
            current = current.next
        
        return deleted_count
    
    def remove_one(self, data):
        return self.__remove(data, multiple=False)
    
    def remove_all(self, data):
        return self.__remove(data, multiple=True)
    
    def __str__(self):
        data = []
        current = self.head
        while current is not None:
            data.append(str(current.data))
            current = current.next
        return " -> ".join(data) + " -> None"


if __name__ == "__main__":
    ll = SortedLinkedList()
    ll.insert(5)
    ll.insert(2)
    ll.insert(6)
    print(ll)
    ll.insert(1)
    print(ll)
    ll.insert(7)
    print(ll)
    ll.insert(4)
    ll.insert(5)
    print(ll)
    ll.remove_one(2)
    ll.remove_all(5)
    ll.remove_all(1)
    print(ll)

