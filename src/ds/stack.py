class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

        else:
            return None

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    # my_stack = list()
    # my_stack.append(3)
    # my_stack.append(4)
    # my_stack.append(6)
    # print(my_stack)
    #
    # my_stack.pop()
    # my_stack.pop()
    #
    # print(my_stack)

    my_stack = Stack()
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(2)
    my_stack.push(6)

    print(my_stack)
    my_stack.pop()
    my_stack.pop()
    print(my_stack)
    print(my_stack.peek())
