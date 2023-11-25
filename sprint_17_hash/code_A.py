# Функция выводит полиноминальный хэш

def polynominal_hash(a, m, s):
    if s == '':
        return 0
    hash, s = ord(s[0]), s[1:]
    for char in s:
        hash = ((hash * a) + ord(char)) % m
    return hash


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    print(polynominal_hash(a, m, s))
