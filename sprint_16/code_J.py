# Программа реализует очередь через связанный список

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def put(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.q_size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.head.value
        self.head = self.head.next
        self.q_size -= 1
        return x

    def size(self):
        return self.q_size


if __name__ == '__main__':
    n = int(input())
    q = Queue()
    for i in range(n):
        command_arr = input().split()
        command = getattr(q, command_arr.pop(0))
        if len(command_arr) > 0:
            command(*command_arr)
        else:
            print(command())
