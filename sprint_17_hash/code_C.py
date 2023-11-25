# Скользящий хэш

def hash_prepare(a, m, s):
    preped_hash = []
    if s == '':
        return preped_hash
    hash, s = ord(s[0]), s[1:]
    preped_hash.append(hash % m)
    for char in s:
        hash = ((hash * a) + ord(char)) % m
        preped_hash.append(hash)
    return preped_hash


def hash_prepare_alt(a, m, s):
    block_len = len(s) // 3
    if block_len > 10:
        block_len = 10
    progress = 0
    preped_hash = []
    while progress + block_len <= len(s):
        hash = ord(s[progress])
        for i in range(progress, progress+block_len):
            hash = ((hash * a) + ord(s[i])) % m
        preped_hash.append(hash)
    return preped_hash, block_len


def sub_seq_hash(preped_hash, start, end, a, m, s):
    length = end - start
    coef = a ** length
    if length < 0:
        return 0
    hash = preped_hash[length]
    for i in range(start-1):
        hash = ((hash - ord(s[i]) * coef) * a + ord(s[length + i + 1])) % m
    return hash


def sub_seq_hash_alt(diapasones, a, m, s):
    preped_hash, block_len = hash_prepare_alt(a, m, s)
    result = []
    for d in diapason:
        start, end = d[0], d[1]
        length = end - start
        coef = a ** block_len
        if length < 0:
            result.append(0)
        blocks = length // block_len
        start_block = start // block_len
        remainer = length % block_len
        hash = preped_hash[start_block]
        for i in range(blocks):
            hash = (hash * coef + preped_hash[start_block+i]) % m
        k = (start_block+blocks)*10
        for i in range(remainer):
            hash = (hash * a + s[k+i]) % m
        coef = a ** length
        for i in range(start-1):
            hash = ((hash - ord(s[i]) * coef) * a + ord(s[length + i + 1])) % m
        result.append(hash)


if __name__ == '__main__':
    k = '23.45'
    int(k)
    a = int(input())
    m = int(input())
    s = input()
    preped_hash = hash_prepare(a, m, s)
    n = int(input())
    for i in range(n):
        diapason = list(map(int, input().split()))
        start, end = diapason[0], diapason[1]
        print(sub_seq_hash(preped_hash, start, end, a, m, s))
