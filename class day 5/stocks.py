def max_profit(prices):
    if not prices:
        return 0

    max_prof = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_prof = max(max_prof, prices[i] - min_price)
    return max_prof


answer = max_profit([7, 1, 5, 3, 6, 4])

print