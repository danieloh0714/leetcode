from collections import deque


# Time complexity: O(n)
# Space complexity: O(k)
def max_sliding_window(nums: list, k: int) -> list:
    ans = []

    d = deque()
    li = 0
    for ri, right in enumerate(nums):
        while d and nums[d[-1]] <= right:
            d.pop()
        d.append(ri)

        if ri+1 < k: continue

        if d[0] < li:
            d.popleft()
        ans.append(nums[d[0]])

        li += 1

    return ans
