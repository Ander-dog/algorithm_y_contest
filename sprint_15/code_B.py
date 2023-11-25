# Функция проверяет, являются ли все три одной чётности

def check(a, b, c):
    if a*b*c % 2 != 0:
        return 'WIN'
    if a % 2 + b % 2 + c % 2 == 0:
        return 'WIN'
    return 'FAIL'


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(check(*arr))
