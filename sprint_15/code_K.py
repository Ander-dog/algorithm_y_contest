# Функция, которая складывает число в списочной форме и в обычной
# и возвращает число в списочной

def list_form(b, arr, k):
    arr_n = []
    while k > 0:
        arr_n.append(k % 10)
        if b > 0:
            arr_n[-1] += arr.pop()
            b -= 1
        k = k // 10 + arr_n[-1] // 10
        arr_n[-1] %= 10
    arr_n += arr[::-1]
    return arr_n[::-1]


if __name__ == '__main__':
    b = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    sum_list = list_form(b, arr, k)
    print(*sum_list)
