# Time complexity: O(n)
# Space complexity: O(1)
def max_profit(prices: list) -> int:
    buy, sell = float('-inf'), 0
    prev_buy, prev_sell = 0, 0

    for price in prices:
        prev_buy = buy
        buy = max(buy, prev_sell-price)

        prev_sell = sell
        sell = max(sell, prev_buy+price)

    return sell
