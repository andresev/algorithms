def maxProfit(prices: list[int]) -> int:
    buy_price = min(prices)
    buy_price_index = prices.index(buy_price)

    for index, price in enumerate(prices):
        if index > buy_price_index:
            print(price)
            if price > buy_price and price > prices[index - 1]:
                sell_price = price
                profit = sell_price - buy_price
            elif profit <= 0:
                profit = 0
        else:
            profit = 0
    # return profit
    print(f"Hello, it's {profit}")
