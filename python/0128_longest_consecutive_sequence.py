# Time complexity: O(n)
# Space complexity: O(n)
def longest_consecutive(nums: list) -> int:
    ans = 0

    nums_set = set(nums)
    for n in nums:
        if n-1 in nums_set: continue

        curr = n
        while curr in nums_set:
            curr += 1
        ans = max(ans, curr-n)

    return ans
