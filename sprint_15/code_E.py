def complicated(arr):
    word = arr[0]
    for i in range(len(arr)-1):
        if len(word) < len(arr[i+1]):
            word = arr[i+1]
    return word


if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    word = complicated(arr)
    print(word)
    print(len(word))
