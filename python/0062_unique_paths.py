# Time complexity: O(mn)
# Space complexity: O(n)
def unique_paths(m: int, n: int) -> int:
    dp = [1 for _ in range(n)]

    for _ in range(1, m):
        for c in range(1, n):
            dp[c] = dp[c-1]+dp[c]

    return dp[n-1]
