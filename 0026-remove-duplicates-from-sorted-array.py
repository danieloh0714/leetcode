# Time complexity: O(n)
# Space complexity: O(1)
def remove_duplicates(nums: list) -> int:
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    return i
