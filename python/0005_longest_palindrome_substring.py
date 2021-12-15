# Time complexity: O(n^2)
# Space complexity: O(1)
def longest_palindrome(s: str) -> str:
    idxs = [0, 0]

    def palindrome_length(li, ri):
        while li >= 0 and ri < len(s) and s[li] == s[ri]:
            li -= 1
            ri += 1
        return [li+1, ri-1]

    for i in range(len(s)-1):
        one = palindrome_length(i, i)
        two = palindrome_length(i, i+1)
        idxs = max(idxs, one, two, key=lambda pair: pair[1]-pair[0])

    return s[idxs[0]:idxs[1]+1]
