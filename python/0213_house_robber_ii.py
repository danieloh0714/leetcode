# Time complexity: O(n)
# Space complexity: O(1)
def rob(nums: list) -> int:
    if len(nums) == 1: return nums[0]

    one, two = 0, 0
    for i in range(len(nums)-1):
        one, two = two, max(one+nums[i], two)

    three, four = 0, 0
    for i in range(1, len(nums)):
        three, four = four, max(three+nums[i], four)

    return max(two, four)
