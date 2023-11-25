# Функция суммирует два числа в двоичной форме и возвращает двоичное число

def doublize_sum(n, m):
    sum = [0,] + [int(x) for x in str(n + m)]
    for i in reversed(range(len(sum))):
        if sum[i] > 1:
            sum[i] -= 2
            sum[i-1] += 1
    if 1 not in sum:
        return '0'
    return ''.join(list(map(str, sum))).lstrip('0')


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(doublize_sum(n, m))
