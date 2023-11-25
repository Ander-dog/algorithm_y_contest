# Функция выводит самое большое число, которое можно составить из данных чисел.

def more(object_1, object_2):
    str_1 = object_1 + object_2
    str_2 = object_2 + object_1
    return str_1 > str_2


def big_number(arr, n):
    for i in range(1, n):
        item_to_insert = arr[i]
        j = i
        while j > 0 and more(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return ''.join(arr)


if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    print(big_number(arr, n))
