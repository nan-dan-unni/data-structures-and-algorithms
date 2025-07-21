class Stack:
    __MAX = 100
    def __init__(self):
        self.__data = []
        self.__top = 0 # usually used in c/c++
    
    def push(self, new_item):
        if self.__top < self.__MAX:
            self.__data.append(new_item)
            self.__top += 1
        else:
            raise ValueError("Stack overflow")
    
    def pop(self):
        if self.__top > 0:
            value = self.__data[self.__top - 1]
            del self.__data[self.__top - 1]
            self.__top -= 1
            return value
        raise ValueError("Stack underflow")
    
    def peek(self):
        if self.__top > 0:
            return self.__data[-1]
        raise ValueError("Stack underflow")
    
    def is_full(self):
        return self.__top >= self.__MAX
    
    def is_empty(self):
        return self.__top == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push("a")
    stack.push("b")
    print("peek = ", stack.peek())
    print("pop = ", stack.pop())
    print("peek = ", stack.peek())

