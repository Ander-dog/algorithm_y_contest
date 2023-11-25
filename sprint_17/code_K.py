# Реализация сортировки слиянием с помощью двух функций: merge и merge_sort

def merge(arr, lf, mid, rt):
    if (rt - lf) == 1:
        return arr[lf]

    result = [0] * (rt - lf)

    a, b, r = lf, mid, 0
    while a < mid and b < rt:
        if arr[a] <= arr[b]:
            result[r] = arr[a]
            a += 1
        else:
            result[r] = arr[b]
            b += 1
        r += 1

    while a < mid:
        result[r] = arr[a]
        a += 1
        r += 1

    while b < rt:
        result[r] = arr[b]
        b += 1
        r += 1

    return result


def merge_sort(arr, lf, rt):
    if (rt - lf) in (0, 1):
        return None
    mid = (lf + rt) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rt)
    arr[lf:rt] = merge(arr, lf, mid, rt)
    return None


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
