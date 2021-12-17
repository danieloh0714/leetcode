# Time complexity: O(mn)
# Space complexity: O(n)
def maximal_square(matrix: list) -> int:
    ans = 0

    dp = [0 for _ in range(len(matrix[0])+1)]
    prev_right = 0

    for r in reversed(range(len(matrix))):
        for c in reversed(range(len(matrix[0]))):
            temp = dp[c]

            if matrix[r][c] == '0':
                dp[c] = 0
            else:
                right = dp[c+1]
                diag = prev_right
                down = dp[c]
                dp[c] = min(right, diag, down)+1

            ans = max(ans, dp[c])
            prev_right = temp

    return ans*ans
