# Time complexity: O(log(n))
# Space complexity: O(1)
def search_range(nums: list, target: int) -> list:
    def search(left_bias: bool) -> int:
        i = -1
        li, ri = 0, len(nums)-1
        while li <= ri:
            mi = (li+ri)//2
            if target == nums[mi]:
                i = mi
                if left_bias:
                    ri = mi-1
                else:
                    li = mi+1
            elif target < nums[mi]:
                ri = mi-1
            else:
                li = mi+1

        return i

    return [search(True), search(False)]
