# Time complexity: O(n)
# Space complexity: O(1)
def product_except_self(nums: list) -> list:
    ans = [1 for _ in nums]

    prod_lr, prod_rl = 1, 1
    for li in range(len(nums)):
        ri = len(nums)-1-li
        ans[li] *= prod_lr
        ans[ri] *= prod_rl
        prod_lr *= nums[li]
        prod_rl *= nums[ri]

    return ans
