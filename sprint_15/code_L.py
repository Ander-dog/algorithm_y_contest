# Функция, которая находит лишнюю букву, сравнивая две строки

def find_odd(s, t):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                t.pop(j)
                break
    return t[0]


if __name__ == '__main__':
    s = str(input())
    t = str(input())
    print(find_odd(s, t))
