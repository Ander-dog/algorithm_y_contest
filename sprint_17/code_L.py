# Бинарный поиск чисел s и 2s, выполненный через рекурсию

def binary_search(arr, s, left, right):
    mid = (left + right) // 2
    if left >= right:
        return -1
    if arr[mid] >= s and (arr[mid - 1] < s or mid == left):
        return mid + 1
    elif arr[mid] >= s and arr[mid - 1] >= s:
        return binary_search(arr, s, left, mid)
    else:
        return binary_search(arr, s, mid+1, right)


def two_bycicles(n, arr, s):
    day_1 = binary_search(arr, s, 0, n)
    if day_1 >= 0:
        day_2 = binary_search(arr, 2*s, day_1, n)
    else:
        day_2 = -1
    return day_1, day_2


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    print(*two_bycicles(n, arr, s))
