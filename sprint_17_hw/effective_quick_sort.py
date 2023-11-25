# 83389361

from random import choice


class CompetionScore:
    def __init__(self, login, score, penalty):
        self.login = login
        self.score = score
        self.penalty = penalty

    def __str__(self):
        return self.login

    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        elif self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.login < other.login


def in_place_quick_sort(arr, start, end):
    if end - start < 2:
        return None
    pivot = choice(arr[start:end])
    left = start
    right = end - 1
    while left <= right:
        while arr[left] < pivot and left < right:
            left += 1
        while pivot < arr[right] and left < right:
            right -= 1
        if left == right and pivot < arr[left]:
            break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    in_place_quick_sort(arr, start, left)
    in_place_quick_sort(arr, left, end)
    return None


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        new_arr = input().split()
        arr.append(
            CompetionScore(new_arr[0], int(new_arr[1]), int(new_arr[2]))
        )
    in_place_quick_sort(arr, 0, n)
    for name in arr:
        print(name)
