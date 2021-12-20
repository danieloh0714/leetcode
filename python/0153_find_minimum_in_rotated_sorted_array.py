# Time complexity: O(log(n))
# Space complexity: O(1)
def find_min(nums: list) -> int:
    li, ri = 0, len(nums)-1
    while li < ri:
        mi = (li+ri)//2
        if nums[mi] < nums[ri]:
            ri = mi
        else:
            li = mi+1

    return nums[li]
