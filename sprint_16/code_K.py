# Функция рекурсивно находит число Фибоначчи с индексом i

def fibonacci(i):
    if i == 0 or i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
