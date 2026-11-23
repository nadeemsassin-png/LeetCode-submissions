class Solution:
    def maxProfit(self, prices):
        minPrice = prices[0]
        best = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > best:
                best = price - minPrice
        return best
