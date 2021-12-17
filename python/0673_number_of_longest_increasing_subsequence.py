# Time complexity: O(n^2)
# Space complexity: O(n)
def find_number_of_LIS(nums: list) -> int:
    dp = [[1, 1] for _ in nums]

    ans = 1
    lis = 1
    for i in reversed(range(len(nums)-1)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                length, count = dp[j]
                if length+1 > dp[i][0]:
                    dp[i] = [length+1, count]
                elif length+1 == dp[i][0]:
                    dp[i][1] += count

        if dp[i][0] > lis:
            lis = dp[i][0]
            ans = dp[i][1]
        elif dp[i][0] == lis:
            ans += dp[i][1]

    return ans
