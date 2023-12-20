# Функция должна напечатать все возможные скобочные последовательности
# заданной длины в алфавитном (лексикографическом) порядке.

def skobka(n):
    if n == 1:
        return ['()']
    elif n == 0:
        return []
    elif n > 1:
        br_arr = []
        for i in range(n):
            for br_seq_1 in skobka(i):
                for br_seq_2 in skobka(n-i):
                    br_arr.append(br_seq_1 + br_seq_2)
        for br_seq in skobka(n-1):
            br_arr.append('(' + br_seq + ')')
        br_arr = list(set(br_arr))
        br_arr.sort()
        return br_arr


def all_skobka(n):
    if n == 1:
        return ['()', '[]', '{}']
    elif n == 0:
        return []
    elif n > 1:
        br_arr = []
        for i in range(n):
            for br_seq_1 in all_skobka(i):
                for br_seq_2 in all_skobka(n-i):
                    br_arr.append(br_seq_1 + br_seq_2)
        for br_seq in all_skobka(n-1):
            br_arr.append('(' + br_seq + ')')
            br_arr.append('[' + br_seq + ']')
            br_arr.append('{' + br_seq + '}')
        br_arr = list(set(br_arr))
        br_arr.sort()
        return br_arr


def bracket(i, n, br_seq):
    if n == 0:
        print(br_seq)
    elif i == n:
        bracket(i - 1, n - 1, br_seq + ')')
    else:
        bracket(i + 1, n - 1, br_seq + '(')
        if i > 0:
            bracket(i - 1, n - 1, br_seq + ')')


def all_bracket(i, n, br_seq, stack):
    if n == 0:
        print(br_seq)
    elif i == n:
        closing_br = stack.pop()
        all_bracket(i - 1, n - 1, br_seq + closing_br, stack)
    else:
        all_bracket(i + 1, n - 1, br_seq + '(', stack + ')')
        all_bracket(i + 1, n - 1, br_seq + '[', stack + ']')
        all_bracket(i + 1, n - 1, br_seq + '{', stack + '}')
        if i > 0:
            closing_br = stack.pop()
            all_bracket(i - 1, n - 1, br_seq + closing_br, stack)


if __name__ == '__main__':
    n = int(input())
    # bracket(0, 2*n, '')
    # for br in all_skobka(n): print(br)
    # all_bracket(0, 2*n, '', '')
