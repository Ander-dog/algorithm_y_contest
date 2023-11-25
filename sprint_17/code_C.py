# Функция выводит True, если s является подпоследовательностью t,
# иначе —– False.

def subsequence(s, t):
    i = 0
    j = 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 1
        i += 1
    return len(s) == j


if __name__ == '__main__':
    s = input()
    t = input()
    print(subsequence(s, t))
