# 82441933

def cool_join(arr, n):
    for i in range(n):
        arr[i] = str(arr[i])
    return ' '.join(arr)


def dist(arr, n):
    dist_arr = [0] * n
    closest_zero = n
    for i in range(n):
        if arr[i] == 0:
            closest_zero = 0
        else:
            closest_zero += 1
            dist_arr[i] = closest_zero
    closest_zero = n
    for i in reversed(range(n)):
        closest_zero += 1
        if dist_arr[i] > closest_zero:
            dist_arr[i] = closest_zero
        else:
            closest_zero = dist_arr[i]
    return dist_arr


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(cool_join(dist(arr, n), n))
