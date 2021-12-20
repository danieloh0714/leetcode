# Time complexity: O(log(n))
# Space complexity: O(1)
def search(nums: list, target: int) -> bool:
    li, ri = 0, len(nums)-1
    while li <= ri:
        mi = (li+ri)//2
        if nums[mi] == target: return True

        while li < mi and nums[li] == nums[mi]:
            li += 1

        if nums[mi] >= nums[li]:
            if nums[li] <= target < nums[mi]:
                ri = mi-1
            else:
                li = mi+1
        else:
            if nums[mi] < target <= nums[ri]:
                li = mi+1
            else:
                ri = mi-1

    return False
