# Time complexity: O(n)
# Space complexity: O(1)
def max_product(nums: list) -> int:
    max_prod = nums[0]

    curr_max = nums[0]
    curr_min = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        curr_max, curr_min = max(n, curr_max*n, curr_min*n), min(n, curr_max*n, curr_min*n)
        max_prod = max(max_prod, curr_max)

    return max_prod
