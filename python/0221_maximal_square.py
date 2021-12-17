# Time complexity: O(mn)
# Space complexity: O(mn)
def maximal_square(matrix: list) -> int:
    ans = 0
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    def access_dp(r: int, c: int) -> int:
        if r >= len(matrix) or c >= len(matrix[0]): return 0
        return dp[r][c]

    for r in reversed(range(len(matrix))):
        for c in reversed(range(len(matrix[0]))):
            if matrix[r][c] == '0': continue

            right = access_dp(r, c+1)
            diag = access_dp(r+1, c+1)
            down = access_dp(r+1, c)
            dp[r][c] = min(right, diag, down)+1

            ans = max(ans, dp[r][c])

    return ans*ans
