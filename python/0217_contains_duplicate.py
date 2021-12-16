# Time complexity: O(n)
# Space complexity: O(n)
def contains_duplicate(nums: list) -> bool:
    seen = set()
    for n in nums:
        if n in seen: return True
        seen.add(n)

    return False
