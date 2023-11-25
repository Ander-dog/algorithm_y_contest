# Функция находит последние k цифр i-го числа Фибоначчи

def fibonacci(n, k):
    mod = 10**k
    arr = [1] * (n+1)
    for i in range(2, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % mod
    return arr[n]


if __name__ == '__main__':
    n_k = list(map(int, input().split()))
    print(fibonacci(*n_k))
