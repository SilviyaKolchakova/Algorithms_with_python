# [1, 2, 3, 4, 5]
#  0  1  2  3  4
# targert = 1

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid = nums[mid_idx]

        if mid == target:
            return mid_idx

        if mid < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
