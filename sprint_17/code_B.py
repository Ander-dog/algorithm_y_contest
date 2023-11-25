# Функция выводит все возможные комбинации букв через пробел, если известны
# какие кнопки на телефоне нажимали

BUTTONS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def button_phone_text_recursion(n, seq, expr, arr):
    if seq == 0:
        arr.append(expr)
    else:
        for letter in BUTTONS[seq // (10 ** n)]:
            button_phone_text_recursion(
                n - 1,
                seq % (10 ** n),
                expr + letter,
                arr
            )


def button_phone_text(seq):
    arr = []
    n = len(str(seq)) - 1
    button_phone_text_recursion(n, seq, '', arr)
    return ' '.join(arr)


if __name__ == '__main__':
    seq = int(input())
    print(button_phone_text(seq))
