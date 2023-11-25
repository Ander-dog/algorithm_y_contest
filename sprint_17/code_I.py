# Функция выводит первые k самых встречающихся чисел

def key_value(elem):
    return arr.count(elem)


def university(arr, k):
    arr_keys = list(set(arr))
    arr_keys.sort(key=key_value, reverse=True)
    return arr_keys[:k]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(*university(arr, k))
