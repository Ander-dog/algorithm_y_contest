# Частичная сортировка (придумана в условии задачи) разбивает массив
# на подмассивы, фильтрует их и складывает. Функция выводит максимальное
# количество отрезков, на которое можно разбить массив

def particial_sort(n, arr):
    max_el = arr[0]
    divide_arr = []
    divide_arr.append(0)
    for i in range(1, n):
        if arr[i] > max_el:
            max_el = arr[i]
            divide_arr.append(i)
    divide_arr.append(n)
    checker = min(arr[divide_arr[-2]:])
    for i in reversed(range(len(divide_arr)-2)):
        if max(arr[divide_arr[i]:divide_arr[i+1]]) > checker:
            divide_arr.pop(i+1)
        checker = min(arr[divide_arr[i]:divide_arr[i+1]])
    return len(divide_arr) - 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(particial_sort(n, arr))
