# Time complexity: O(ac)
# Space complexity: O(a)
def coin_change(coins: list, amount: int) -> int:
    dp = [amount+1 for _ in range(amount+1)]
    dp[0] = 0

    for a in range(1, amount+1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a-coin]+1)

    return -1 if dp[amount] == amount+1 else dp[amount]
