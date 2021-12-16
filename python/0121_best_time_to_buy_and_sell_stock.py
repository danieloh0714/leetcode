# Time complexity: O(n)
# Space complexity: O(1)
def max_profit(prices: list) -> int:
    ans = 0

    min_so_far = prices[0]
    for price in prices:
        min_so_far = min(min_so_far, price)
        ans = max(ans, price-min_so_far)

    return ans
