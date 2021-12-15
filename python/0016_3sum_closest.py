# Time complexity: O(n^2)
# Space complexity: O(n)
def three_sum_closest(nums: list, target: int) -> int:
    ans = nums[0]+nums[1]+nums[2]

    sorted_nums = sorted(nums)
    for li in range(len(nums)-2):
        mi, ri = li+1, len(nums)-1
        while mi < ri:
            curr = sorted_nums[li]+sorted_nums[mi]+sorted_nums[ri]
            if curr == target: return curr
            ans = min(ans, curr, key=lambda n: abs(target-n))
            if curr < target:
                mi += 1
            else:
                ri -= 1

    return ans
