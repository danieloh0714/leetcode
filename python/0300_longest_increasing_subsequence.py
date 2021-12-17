def length_of_LIS(nums: list) -> int:
    ans = 1

    dp = [1 for _ in nums]
    dp[-1] = 1
    for i in reversed(range(len(nums)-1)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])

    return ans
