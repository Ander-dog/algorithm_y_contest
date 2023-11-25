# Функция на вход принимает голову односвязного списка и элемент,
# который нужно найти. Функция возвращает индекс первого вхождения
# искомого элемента в список(индексация начинается с нуля).
# Если элемент не найден, нужно вернуть -1.

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, elem):
    idx = 0
    while node.value != elem:
        if node.next_item is None:
            return -1
        node = node.next_item
        idx += 1
    return idx


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__' and LOCAL:
    test()
