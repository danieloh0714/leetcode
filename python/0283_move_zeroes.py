# Time complexity: O(n)
# Space complexity: O(1)
def move_zeroes(nums: list) -> None:
    li = 0
    for ri in range(len(nums)):
        if nums[ri] != 0:
            nums[li], nums[ri] = nums[ri], nums[li]
            li += 1
