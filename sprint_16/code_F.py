# В первой строке записано одно число n — количество команд
# В следующих n строках идут команды. Команды могут быть следующих видов:
# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print('error')
            return None
        return self.items.pop()

    def get_max_value(self):
        if self.isEmpty():
            return None
        return max(self.items)

    def get_max(self):
        print(self.get_max_value())


stack = Stack()
n = int(input())
for i in range(n):
    command_arr = input().split()
    command = getattr(stack, command_arr.pop(0))
    if len(command_arr) > 0:
        command(int(*command_arr))
    else:
        command()
