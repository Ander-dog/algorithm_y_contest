# Функция печатает транспонированную матрицу

def transpon_print(matrix, n, m):
    for i in range(m):
        stroka = f'{matrix[0][i]}'
        for j in range(1, n):
            stroka += f' {matrix[j][i]}'
        print(stroka)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        new_arr = list(map(int, input().split()))
        matrix.append(new_arr)
    transpon_print(matrix, n, m)
