# Time complexity: O(n)
# Space complexity: O(1)
def jump(nums: list) -> int:
    jumps = 0
    
    li, ri = 0, 0
    while ri < len(nums)-1:
        farthest = li
        for i in range(li, ri+1):
            farthest = max(farthest, i+nums[i])
        li, ri = ri, farthest
        jumps += 1

    return jumps
