class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def insert_after(self, data, after):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True
        else:
            current = self.head
            while current is not None:
                if current.data == after:
                    new_node.prev = current
                    if current.next is not None:
                        new_node.next = current.next
                        current.next.prev = new_node
                    current.next = new_node
                    return True
                current = current.next
        return False

    def remove_one(self, data):
        if self.head is None:
            print("List is empty")
            return False
        elif self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return True
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                    return True
                current = current.next
        return False

    def remove_all(self, data):
        deleted_count = 0
        if self.head is None:
            print("List is empty")
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            deleted_count += 1
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    next_node = current.next
                    current.prev.next = next_node
                    if current.next is not None:
                        current.next.prev = current.prev
                    deleted_count += 1
                    current = next_node
                else:
                    current = current.next
        return deleted_count
    
    def __str__(self):
        data = []
        current = self.head
        while current is not None:
            data.append(str(current.data))
            current = current.next
        return "None <-> " + " <-> ".join(data) + " <-> None"

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert(1)
    ll.insert(4)
    ll.insert(4)
    ll.insert(4)
    ll.insert(3)
    ll.insert(4)
    print(ll)
    ll.remove_one(4)
    print(ll)
    ll.remove_all(4)
    print(ll)
    ll.insert_after(2, 1)
    ll.insert(4)
    ll.insert(5)
    print(ll)

