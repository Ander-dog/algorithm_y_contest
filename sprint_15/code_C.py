# Функция выводит соседние элементы от заданного элемента в матрице
# в порядке возрастания

def neighbours(n, m, matrix, i, j):
    elements = []
    if i != 0:
        elements.append(matrix[i-1][j])
    if i != n-1:
        elements.append(matrix[i+1][j])
    if j != 0:
        elements.append(matrix[i][j-1])
    if j != m-1:
        elements.append(matrix[i][j+1])
    if len(elements) != 0:
        elements.sort()
    return elements


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        arr = list(map(int, input().split()))
        matrix.append(arr)
    i = int(input())
    j = int(input())
    elements = neighbours(n, m, matrix, i, j)
    print(*elements)
