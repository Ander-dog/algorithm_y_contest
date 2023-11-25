# Функция выводит наибольшее количество домов, которое может купить Тимофей.

def house_purchase(n, k, arr):
    if k == 0:
        return 0
    arr.sort()
    count = 0
    sum = 0
    while sum <= k and count < n:
        sum += arr[count]
        count += 1
    if sum > k:
        count -= 1
    return count


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(house_purchase(n, k, arr))
