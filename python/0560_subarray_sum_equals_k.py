# Time complexity: O(n)
# Space complexity: O(n)
def subarray_sum(nums: list, k: int) -> int:
    ans = 0

    cache = {0: 1}
    running_sum = 0
    for n in nums:
        running_sum += n
        diff = running_sum-k
        ans += cache.get(diff, 0)
        cache[running_sum] = cache.get(running_sum, 0)+1

    return ans
