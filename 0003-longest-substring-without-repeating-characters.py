# Time complexity: O(n)
# Space complexity: O(n)
def length_of_longest_substring(s: str) -> int:
    ans = 0

    latest_idx = dict()
    li = 0
    for ri, char in enumerate(s):
        if char in latest_idx and latest_idx[char] >= li:
            ans = max(ans, ri-li)
            li = latest_idx[char]+1
        latest_idx[char] = ri

    return max(ans, len(s)-li)
