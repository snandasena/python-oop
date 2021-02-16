class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return ('(' + str(self.data) + ')')


class DoublyLinkedLint:

    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def add(self, data):

        if self.size == 0:
            self.root = Node(data)
            self.last = self.root

        else:
            new_node = Node(data, self.root)
            self.root.prev = new_node
            self.root = new_node

        self.size += 1

    def find(self, data):
        curr = self.root

        while curr is not None:
            if curr.data == data:
                return data
            elif curr.next == None:
                return False
            else:
                curr = curr.next

    def remove(self, data):
        curr = self.root

        while curr is not None:
            if curr.data == data:
                if curr.prev is not None:
                    if curr.next is not None:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                    else:
                        curr.next.prev = None
                        self.last = curr.prev
                else:
                    self.root = curr.next
                    curr.next.prev = self.root

                self.size += 1
                return True
            else:
                curr = curr.next

        return False

    def print_list(self):

        if self.root is None:
            return

        curr = self.root
        print(curr, end='->')

        while curr.next is not None:
            curr = curr.next
            print(curr, end='->')

        print()


if __name__ == '__main__':
    dll = DoublyLinkedLint()

    for i in [5, 9, 3, 8, 9]:
        dll.add(i)

    print('size=', dll.size)
    dll.print_list()

    dll.remove(8)
    dll.print_list()
