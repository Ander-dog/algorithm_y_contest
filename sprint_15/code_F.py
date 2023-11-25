# Функция проверяет, является ли предложение палиндропом без учёта пунктуации

import string


def palindrom(sentence):
    sentence = sentence.translate(
        str.maketrans('', '', ' ' + string.punctuation)
    ).casefold()
    for i in range(len(sentence)//2):
        if sentence[i] != sentence[-i-1]:
            return False
    return True


if __name__ == '__main__':
    sentence = input()
    print(palindrom(sentence))
