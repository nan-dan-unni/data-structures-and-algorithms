class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
    

class LinkedListStack:
    MAX_SIZE = 3
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)

        if self.size >= self.MAX_SIZE:
            print("Stack overflow")
            return
        
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack underflow")
            return None
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_full(self):
        return self.size >= self.MAX_SIZE

    def is_empty(self):
        return self.top is None
    
    def __str__(self):
        current = self.top
        data = []
        while current is not None:
            data.append(str(current.data))
            current = current.next
        
        return ", ".join(data)


if __name__ == "__main__":
    stack = LinkedListStack()
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("is full", stack.is_full())
    print(stack.pop())
    print(stack)
    print(stack.peek())
    stack.pop()
    stack.pop()
    print("is empty", stack.is_empty())