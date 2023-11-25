# Сортировка пузырьком

def bubble(arr, n):
    sorting = True
    was_sorted = True
    while sorting:
        sorting = False
        printable = ''
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                holder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = holder
                sorting = True
                was_sorted = False
            printable += f'{arr[i]} '
        if sorting:
            print(printable + str(arr[n-1]))
    if was_sorted:
        print(printable + str(arr[n-1]))
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    bubble(arr, n)
