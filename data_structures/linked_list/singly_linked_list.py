class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, *args):
        self.head = None
        for item in args:
            self.add(item)
    
    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        return newNode
    
    def removeOne(self, data):
        current = self.head

        if current is None:
            print("Empty List")
            return False
        elif current.data == data:
            self.head = current.next
            return True
        else:
            while current is not None:
                if not current.next == None:
                    if current.next.data == data:
                        current.next = current.next.next
                        return True
                current = current.next
        
        return False
        
    def removeAll(self, data):
        current = self.head
        deleted_count = 0

        if current is None:
            print("Empty List")
            return False
        elif current.data == data:
            self.head = current.next
            deleted_count += 1

        while current is not None:
            if current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    deleted_count += 1
            current = current.next
        
        return deleted_count
        
    
    def __str__(self):
        current = self.head
        data = []
        while current is not None:
            data.append(str(current.data))
            current = current.next
        return " -> ".join(data) + " -> None"
    
    def __len__(self):
        current = self.head
        size = 0

        while current is not None:
            size += 1
            current = current.next
        return size


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add(2)
    print(ll)
    ll.add(4)
    ll.add(4)
    ll.removeOne(4)
    print(ll)
    ll.add(5)
    ll.add(6)
    ll.removeOne(5)
    print(ll)
    ll.add(3)
    ll.add(6)
    ll.add(4)
    print(ll)
    ll.removeAll(6)
    ll.add(5)
    ll.add(6)
    print(ll)
    print(len(ll))
