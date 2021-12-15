# Time complexity: O(log(n))
# Space complexity: O(1)
def search_insert(nums: list, target: int) -> int:
    li, ri = 0, len(nums)-1
    while li <= ri:
        mi = (li+ri)//2
        if target == nums[mi]:
            return mi
        if target < nums[mi]:
            ri = mi-1
        else:
            li = mi+1

    return li
