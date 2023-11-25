# Функция возвращает количество детей, которые останутся довольными

def cookies(n, arr_cond, m, arr):
    arr_cond.sort()
    arr.sort()
    count = 0
    for i in range(1, n+1):
        if arr[-count-1] >= arr_cond[-i]:
            count += 1
            if count == m:
                break
    return count


if __name__ == '__main__':
    n = int(input())
    arr_cond = list(map(int, input().split()))
    m = int(input())
    arr = list(map(int, input().split()))
    print(cookies(n, arr_cond, m, arr))
