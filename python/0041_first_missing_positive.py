# Time complexity: O(n)
# Space complexity: O(1)
def first_missing_positive(nums: list) -> int:
    for i, n in enumerate(nums):
        if n < 0: nums[i] = 0

    for i in range(len(nums)):
        abs_val = abs(nums[i])
        if 1 <= abs_val <= len(nums):
            j = abs_val-1
            if nums[j] > 0:
                nums[j] *= -1
            elif nums[j] == 0:
                nums[j] = -(len(nums)+1)

    for i, n in enumerate(nums):
        if n >= 0: return i+1

    return len(nums)+1
