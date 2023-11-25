# Функция принимает отрезки, суммирует их и выводит получившиеся

def merge_segments(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    elif len_arr == 2:
        left = arr[:1]
        right = arr[1:]
    else:
        left = merge_segments(arr[:len_arr//2])
        right = merge_segments(arr[len_arr//2:])

    result = [0] * len_arr

    a, b, = 0, 0
    if left[0][0] <= right[0][0]:
        result[0] = left[0]
        a = 1
    else:
        result[0] = right[0]
        b = 1
    r = 0

    while a < len(left) and b < len(right):
        if left[a][0] <= right[b][0]:
            s = left[a]
            a += 1
        else:
            s = right[b]
            b += 1
        if result[r][1] < s[0]:
            r += 1
            result[r] = s
        else:
            result[r][1] = max(result[r][1], s[1])

    while a < len(left):
        if result[r][1] < left[a][0]:
            r += 1
            result[r] = left[a]
        else:
            result[r][1] = max(result[r][1], left[a][1])
        a += 1

    while b < len(right):
        if result[r][1] < right[b][0]:
            r += 1
            result[r] = right[b]
        else:
            result[r][1] = max(result[r][1], right[b][1])
        b += 1

    return result[:r+1]


def flowerbeds(arr, n):
    arr.sort()
    merged_arr = [arr[0]]
    for i in range(1, n):
        if merged_arr[-1][1] < arr[i][0]:
            merged_arr.append(arr[i])
        else:
            merged_arr[-1][1] = max(merged_arr[-1][1], arr[i][1])
    return merged_arr


def quick_sort_segments(arr) -> list:
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    pivot = arr[0]
    left = [None] * len_arr
    right = [None] * len_arr
    a, b = 0, 0
    for i in range(1, len_arr):
        if arr[i] > pivot:
            right[b] = arr[i]
            b += 1
        elif arr[i] < pivot:
            left[a] = arr[i]
            a += 1
        # Выполняется только если pivot[0] == arr[i][0]
        elif pivot[1] < arr[i][1]:
            pivot[1] = arr[i][1]
    left[a] = pivot
    a += 1
    left = quick_sort_segments(left[:a])
    right = quick_sort_segments(right[:b])

    for i in range(len(right)):
        if left[-1][1] < right[i][1]:
            if left[-1][1] >= right[i][0]:
                left[-1][1] = right[i][1]
                left += right[i+1:]
            else:
                left += right[i:]

    return left


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for segment in merge_segments(arr):
        print(*segment)
