# 83281620

def broken_search(nums, target, left=0, right=-1):
    if right == -1:
        right = len(nums)
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        if nums[right-1] < nums[mid]:
            return broken_search(nums, target, mid + 1, right)
        elif nums[right-1] < target:
            return broken_search(nums, target, left, mid)
        else:
            return broken_search(nums, target, mid + 1, right)
    else:
        if nums[left] > nums[mid]:
            return broken_search(nums, target, left, mid)
        elif nums[left] > target:
            return broken_search(nums, target, mid + 1, right)
        else:
            return broken_search(nums, target, left, mid)


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
