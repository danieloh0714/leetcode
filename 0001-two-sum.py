# Time complexity: O(n)
# Space complexity: O(n)
def two_sum(nums: list, target: int) -> list:
    seen = dict()
    for i, n in enumerate(nums):
        diff = target-n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []
