# Функция выводит медиану после слияния двух списков

def merge(arr_n, arr_s, n, m, k):
    result = [0] * k

    a, b, r = 0, 0, 0
    while a < n and b < m and r <= k // 2:
        if arr_n[a] <= arr_s[b]:
            result[r] = arr_n[a]
            a += 1
        else:
            result[r] = arr_s[b]
            b += 1
        r += 1

    while a < n and r <= k // 2:
        result[r] = arr_n[a]
        a += 1
        r += 1

    while b < m and r <= k // 2:
        result[r] = arr_s[b]
        b += 1
        r += 1

    return result[:r]


def mediane(n, m, arr_n, arr_s):
    k = n + m
    arr = merge(arr_n, arr_s, n, m, k)
    if k % 2 == 0:
        return (arr[-1] + arr[-2]) / 2
    else:
        return arr[-1]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr_n = list(map(int, input().split()))
    arr_s = list(map(int, input().split()))
    print(mediane(n, m, arr_n, arr_s))
