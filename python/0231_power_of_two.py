# Time complexity: O(n)
# Space complexity: O(1)
def is_power_of_two(n: int) -> bool:
    i = 1
    while i < n:
        i *= 2

    return i == n
