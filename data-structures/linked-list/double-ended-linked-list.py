class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleEndedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def insert_after(self, data, after):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True
        else:
            current = self.head
            while current is not None:
                if current.data == after:
                    next_node = current.next
                    current.next = new_node
                    new_node.prev = current
                    new_node.next = next_node
                    if next_node:
                        next_node.prev = new_node
                    return True
                else:
                    current = current.next
        return False
    
    def __remove(self, data, delete_multiple=False):
        deleted_count = 0

        if self.head is None:
            return deleted_count
        
        current = self.head
        while current is not None:
            next_node = current.next
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if not delete_multiple: break
                else: deleted_count += 1

                if next_node is None:
                    self.tail = current.prev
            current = next_node
        

        return deleted_count
    
    def remove_one(self, data):
        deleted_count = self.__remove(data=data, delete_multiple=False)
        return deleted_count > 0
    
    def remove_all(self, data):
        return self.__remove(data=data, delete_multiple=True)
    
    def __str__(self):
        data = []
        current = self.head
        while current is not None:
            data.append(str(current.data))
            current = current.next
        return "None <-> " + " <-> ".join(data) + " <-> None"



if __name__ == "__main__":
    ll = DoubleEndedLinkedList()
    ll.insert(1)
    ll.insert(4)
    ll.insert(4)
    ll.insert(4)
    ll.insert(3)
    ll.insert(4)
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
