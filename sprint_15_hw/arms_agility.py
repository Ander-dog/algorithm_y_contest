# 82255807

def agility(line, k):
    score = 0
    for number in range(1, 10):
        amount = line.count(str(number))
        if 2*k >= amount and amount > 0:
            score += 1
    return score


if __name__ == '__main__':
    k = int(input())
    line = ''
    for i in range(4):
        new_line = str(input())
        new_line = new_line.replace('.', '')
        line += new_line

    print(agility(line, k))
