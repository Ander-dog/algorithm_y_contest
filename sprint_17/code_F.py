# Функция выводит наибольший возможный периметр треугольника
# из заданных отрезков

def triangle(n, arr):
    arr.sort()
    i = n-1
    while i > 1:
        if arr[i] < arr[i-1] + arr[i-2]:
            return arr[i] + arr[i-1] + arr[i-2]
        i -= 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(triangle(n, arr))
