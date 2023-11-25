# Функция возфращает k-ую минимальную разницу между индексами в массиве

def minimal_dif(n, arr, k):
    arr.sort()
    arr_dif = [None] * k
    len_arr_dif = 0
    for i in range(n):
        for j in range(i + 1, n):
            dif = arr[j]-arr[i]
            if len_arr_dif < k:
                arr_dif[len_arr_dif] = dif
                len_arr_dif += 1
                if len_arr_dif == k:
                    arr_dif.sort()
            else:
                if dif < arr_dif[-1]:
                    p = 1
                    while p <= k:
                        if arr_dif[-p] <= dif:
                            break
                        p += 1
                    arr_dif[k-p+2:] = arr_dif[k-p+1:-1]
                    arr_dif[k-p+1] = dif
                else:
                    break
    return arr_dif[-1]


def uneffective_dif(n, arr: list, k):
    arr.sort()
    arr_dif = []
    arr_dif_count = []
    j = 0
    while sum(arr_dif_count) < k:
        count = 0
        for i in range(n):
            count += arr[i+1:].count(arr[i] + j)
        if count > 0:
            arr_dif.append(j)
            arr_dif_count.append(count)
        j += 1
    return arr_dif[-1]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(uneffective_dif(n, arr, k))
