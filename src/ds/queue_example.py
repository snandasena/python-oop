from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else:
            return None

    def peek(self):
        if self.size > 0:
            temp = self.queue.popleft()
            self.queue.appendleft(temp)
            return temp
        else:
            return None

    def get_size(self):
        return self.size


if __name__ == '__main__':
    #
    # my_queue = deque()
    # my_queue.append(1)
    # my_queue.append(2)
    # my_queue.append(3)
    #
    # print(my_queue)
    # my_queue.popleft()
    # print(my_queue)

    my_queue = Queue()
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    my_queue.enqueue(6)

    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()

    print(my_queue.peek())