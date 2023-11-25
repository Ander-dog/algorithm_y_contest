# Функция возвращает двоичную запись заданного числа

def doublize(n):
    result = []
    while n > 1:
        result.append(str(n % 2))
        n = n // 2
    result.append(str(n))
    return ''.join(result[::-1])


if __name__ == '__main__':
    n = int(input())
    print(doublize(n))
