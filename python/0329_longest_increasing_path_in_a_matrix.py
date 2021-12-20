# Time complexity: O(mn)
# Space complexity: O(mn)
def longest_increasing_path(matrix: list) -> int:
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    def dfs(r: int, c: int, prev: int) -> int:
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]): return 0
        val = matrix[r][c]
        if val <= prev: return 0
        if dp[r][c] != 0: return dp[r][c]
        up = dfs(r-1, c, val)
        right = dfs(r, c+1, val)
        down = dfs(r+1, c, val)
        left = dfs(r, c-1, val)
        dp[r][c] = max(up, right, down, left)+1
        return dp[r][c]

    longest = 1
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if dp[r][c] == 0:
                dp[r][c] = dfs(r, c, -1)
                longest = max(longest, dp[r][c])

    return longest
