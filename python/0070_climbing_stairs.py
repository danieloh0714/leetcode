# Time complexity: O(n)
# Space complexity: O(1)
def climb_stairs(n: int) -> int:
    one, two = 1, 0
    for _ in range(n):
        one, two = one+two, one

    return one
