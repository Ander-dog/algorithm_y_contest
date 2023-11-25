# Поиск двух строк с одинаковым полиноминальным хэшем

# Перебор чуть не сломал мой компьютер

def checker(hash_int, a):
    while hash_int > 0:
        if not 96 < hash_int % a < 123:
            return False
        hash_int = hash_int // a
    return True


def decoded(hash_int, a):
    string = ''
    while hash_int > 0:
        string = chr(hash_int % a) + string
        hash_int = hash_int // a
    return string


def polynominal_hash_finder(hash, m, depth, full_number):
    if depth == 1:
        for i in range(25):
            if full_number % m == hash:
                return decoded(full_number, 1000)
            full_number += 1
    else:
        for i in range(25):
            polynominal_hash_finder(hash, m, depth-1, full_number*1000 + 97)
            full_number += 1


if __name__ == '__main__':
    a = 1000
    m = 123987123
    s = 'adsbaebtnsfb'
    print(polynominal_hash_finder(42258992, m, 7, 97))
