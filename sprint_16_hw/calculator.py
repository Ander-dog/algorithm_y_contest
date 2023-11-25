# 82582965

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
    '*': lambda x, y: x * y,
    }


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()


def calculate(symbols):
    calc_stack = Stack()
    for opr in symbols:
        if opr in OPERATORS:
            b = calc_stack.pop()
            a = calc_stack.pop()
            calc_stack.push(OPERATORS[opr](a, b))
        else:
            calc_stack.push(int(opr))
    return calc_stack.pop()


if __name__ == '__main__':
    symbols = input().split()
    print(calculate(symbols))
