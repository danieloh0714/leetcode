# Time complexity: O(n)
# Space complexity: O(1)
def remove_element(nums: list, val: int) -> int:
    li, ri = 0, len(nums)-1
    while li <= ri:
        if nums[li] == val:
            nums[li], nums[ri] = nums[ri], nums[li]
            ri -= 1
        else:
            li += 1

    return li
