# Time complexity: O(n)
# Space complexity: O(1)
def max_area(height: list) -> int:
    area = 0

    li, ri = 0, len(height)-1
    while li < ri:
        left, right = height[li], height[ri]
        area = max(area, (ri-li)*min(left, right))
        if left < right:
            li += 1
        else:
            ri -= 1

    return area
