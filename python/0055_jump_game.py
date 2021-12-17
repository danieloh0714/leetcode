# Time complexity: O(n)
# Space complexity: O(1)
def can_jump(nums: list) -> bool:
    farthest = nums[0]
    i = 0
    while i <= farthest:
        farthest = max(farthest, i+nums[i])
        if farthest >= len(nums)-1: return True
        i += 1

    return False
