# Программа эмулирует работу очереди на кольцевом буфере

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def push(self, x):
        if self.q_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.q_size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.q_size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.q_size


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    q = MyQueueSized(max_size)
    for i in range(n):
        command_arr = input().split()
        command = getattr(q, command_arr.pop(0))
        if len(command_arr) > 0:
            command(int(*command_arr))
        else:
            print(command())
