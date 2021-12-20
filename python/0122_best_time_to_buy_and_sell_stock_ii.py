# Time complexity: O(n)
# Space complexity: O(1)
def max_profit(prices: list) -> int:
    ans = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            ans += prices[i]-prices[i-1]

    return ans
