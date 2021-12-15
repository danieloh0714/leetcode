# Time complexity: O(n)
# Space complexity: O(1)
def trap(height: list) -> int:
    water = 0

    l_max, r_max = 0, 0
    li, ri = 0, len(height)-1
    while li <= ri:
        if l_max < r_max:
            l_max = max(l_max, height[li])
            water += l_max-height[li]
            li += 1
        else:
            r_max = max(r_max, height[ri])
            water += r_max-height[ri]
            ri -= 1

    return water
