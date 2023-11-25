# Функция выводит количество локальных пиков заданного массива

def chaotic_weather(n, arr):
    chaos = 0
    increase = True
    for i in range(n-1):
        print(chaos, increase)
        if arr[i] > arr[i+1] and increase:
            chaos += 1
        if arr[i] < arr[i+1]:
            increase = True
        else:
            increase = False
    if increase:
        chaos += 1
    return chaos


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(chaotic_weather(n, arr))
