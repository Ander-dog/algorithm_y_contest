# Функция принимает на вход скобочную последовательность и возвращает True,
# если последовательность правильная, а иначе False.

BR_PAIR = {
    ')': '(',
    '}': '{',
    ']': '[',
}


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()


def is_correct_bracket_seq(brack):
    br_stack = Stack()
    for br in brack:
        if br in BR_PAIR:
            if br_stack.pop() != BR_PAIR[br]:
                return False
        else:
            br_stack.push(br)
    return br_stack.isEmpty()


if __name__ == '__main__':
    brack = input()
    print(is_correct_bracket_seq(brack))
