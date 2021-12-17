# Time complexity: O(mn)
# Space complexity: O(mn)
def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

    for i2 in reversed(range(len(text2))):
        for i1 in reversed(range(len(text1))):
            if text2[i2] == text1[i1]:
                dp[i2][i1] = dp[i2+1][i1+1]+1
            else:
                dp[i2][i1] = max(dp[i2+1][i1], dp[i2][i1+1])

    return dp[0][0]
