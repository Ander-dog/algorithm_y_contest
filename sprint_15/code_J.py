# Функция, которая раскладывает число на множители

def factorise(n):
    if n == 1:
        return [1,]
    numbers = []
    while n > 1:
        found = False
        i = 2
        while i * i <= n:
            if not n % i:
                numbers.append(i)
                found = True
                n = n // i
                break
            i += 1
        if not found:
            numbers.append(n)
            break
    return numbers


if __name__ == '__main__':
    n = int(input())
    numbers = factorise(n)
    print(*numbers)
