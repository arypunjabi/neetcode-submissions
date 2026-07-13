class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        currProfit = 0
        maxProfit = 0

        while R < len(prices):
            currProfit = prices[R] - prices[L]
            if(currProfit < 0):
                L = R
            maxProfit = max(maxProfit, currProfit)
            R = R + 1
        return maxProfit
