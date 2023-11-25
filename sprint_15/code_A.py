# Функция выводит значение квадратичной функции в заданной точке

def solution(a, x, b, c):
    return a*x*x + b*x + c


if __name__ == '__main__':
    axbc = list(map(int, input().split()))
    print(solution(*axbc))
