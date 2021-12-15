# Time complexity: O(n)
# Space complexity: O(1)
def is_palindrome(x: int) -> bool:
    x_str = str(x)

    li, ri = 0, len(x_str)-1
    while li < ri and x_str[li] == x_str[ri]:
        li += 1
        ri -= 1

    return li >= ri
