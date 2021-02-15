class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return ('(' + str(self.data) + ')')


class CircularLinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next = self.root
        else:
            new_node = Node(data, self.root.next)
            self.root.next = new_node

        self.size += 1

    def find(self, data):
        curr = self.root

        while curr is not None:
            if curr.data == data:
                return data
            elif curr.next == self.root:
                return False

            curr = curr.next

    def remove(self, data):

        curr = self.root
        prev = None

        while True:

            if curr.data == data:

                if prev is not None:
                    prev.next = curr.next

                else:
                    while curr.next != self.root:
                        curr = curr.next

                    curr.next = self.root.next
                    self.root = self.root.next

                self.size -= 1
                return True

            elif curr.next == self.root:
                return False

            prev = curr
            curr = curr.next

    def print_list(self):

        if self.root is None:
            return

        curr = self.root
        print(curr, end='->')

        while curr.next != self.root:
            curr = curr.next
            print(curr, end='->')

        print()


if __name__ == '__main__':

    cll = CircularLinkedList()
    for i in [5, 7, 9, 8, 3]:
        cll.add(i)

    print('size=', cll.size)
    print(cll.find(3))
    print(cll.find(12))

    my_node = cll.root
    print(my_node, end='->')

    for i in range(8):
        my_node = my_node.next
        print(my_node, end='->')

    print()
