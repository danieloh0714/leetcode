# Time complexity: O(n)
# Space complexity: O(1)
def max_subarray(nums: list) -> int:
    ans = nums[0]
    curr = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], curr+nums[i])
        ans = max(ans, curr)

    return ans
