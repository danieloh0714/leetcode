# Time complexity: O(n)
# Space complexity: O(1)
def num_decodings(s: str) -> int:
    one, two = 1, 1

    for i in reversed(range(len(s))):
        one_next = 0
        if 1 <= int(s[i]) <= 9:
            one_next += one
        if 10 <= int(s[i:i+2]) <= 26:
            one_next += two
        one, two = one_next, one

    return one
