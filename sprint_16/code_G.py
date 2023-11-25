# В первой строке записано одно число n — количество команд
# В следующих n строках идут команды. Команды могут быть следующих видов:
# push(x) — добавить число x в стек, за O(1);
# pop() — удалить число с вершины стека, за O(1);
# get_max() — напечатать максимальное число в стеке, за O(1);

class Stack:
    def __init__(self):
        self.items = []
        self.max_value = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, item):
        if self.isEmpty():
            self.max_value.append(item)
        elif self.max_value[-1] < item:
            self.max_value.append(item)
        else:
            self.max_value.append(self.max_value[-1])
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print('error')
            return None
        self.max_value.pop()
        return self.items.pop()

    def get_max_value(self):
        if self.isEmpty():
            return None
        return self.max_value[-1]

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
