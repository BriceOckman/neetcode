class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sale in prices:
            maxP = max(maxP, sale - minBuy)
            minBuy = min(minBuy, sale)
        
        return maxP