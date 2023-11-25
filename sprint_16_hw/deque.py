# 82657061

class QueueLimitException(Exception):
    'Raised when you reacheched to a queue limit'
    pass


class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.front = 1
        self.back = 0
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def is_full(self):
        return self.q_size == self.max_n

    def push_back(self, x):
        if self.is_full():
            raise QueueLimitException
        self.queue[self.back] = x
        self.back = (self.back - 1 + self.max_n) % self.max_n
        self.q_size += 1

    def push_front(self, x):
        if self.is_full():
            raise QueueLimitException
        self.queue[self.front] = x
        self.front = (self.front + 1) % self.max_n
        self.q_size += 1

    def pop_back(self):
        if self.is_empty():
            raise QueueLimitException
        self.back = (self.back + 1) % self.max_n
        x = self.queue[self.back]
        self.queue[self.back] = None
        self.q_size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise QueueLimitException
        self.front = (self.front - 1 + self.max_n) % self.max_n
        x = self.queue[self.front]
        self.queue[self.front] = None
        self.q_size -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    q = Deque(max_size)
    for i in range(n):
        command_arr = input().split()
        command = getattr(q, command_arr.pop(0))
        try:
            if len(command_arr) > 0:
                command(int(*command_arr))
            else:
                print(command())
        except QueueLimitException:
            print('error')
