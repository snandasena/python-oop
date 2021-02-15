class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return ('(' + str(self.data) + ')')


class LinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        curr = self.root

        while curr is not None:
            if curr.data == data:
                return data
            else:
                curr = curr.next

        return None

    def remove(self, data):
        curr = self.root
        prev = None

        while curr is not None:

            if curr.data == data:
                if prev is not None:
                    prev.next = curr.next
                else:
                    self.root = curr.next

                self.size -= 1
                return True

            else:
                prev = curr
                curr = curr.next

        return False

    def print_list(self):
        curr = self.root

        while curr is not None:
            print(curr, end='->')
            curr = curr.next

        print('None')



if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(8)
    linked_list.add(12)

    linked_list.print_list()

    linked_list.remove(8)

    linked_list.print_list()

    print(linked_list.find(5))
    print(linked_list.root)
