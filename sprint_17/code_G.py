# Функция сортирует "вещи по цветам" сортировкой подсчётом
# На самом деле сортирует массив из 0, 1, 2

def count_sort(arr):
    count_list = [0] * 3
    for i in arr:
        count_list[i] += 1
    result = []
    for k in range(3):
        result += [k] * count_list[k]
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = count_sort(arr)
    print(*sorted_arr)
