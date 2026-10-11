class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l,r = 0,1
        maxProfit = 0
        while r < len(prices):
            cur =  prices[r] - prices[l]
            if cur > maxProfit:
                maxProfit = cur

            if prices[r] < prices[l]:
                l = r

            r+=1

        return maxProfit