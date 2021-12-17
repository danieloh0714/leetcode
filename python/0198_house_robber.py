# Time complexity: O(n)
# Space complexity: O(1)
def rob(nums: list) -> int:
    one, two = 0, 0
    
    for n in nums:
        one, two = two, max(one+n, two)

    return two
