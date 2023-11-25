# Функция проверяет, является ли число степенью 4

def power_of_four(n):
    while n > 1:
        if n % 4 != 0:
            return False
        n = n / 4
    return True


if __name__ == '__main__':
    n = int(input())
    print(power_of_four(n))
