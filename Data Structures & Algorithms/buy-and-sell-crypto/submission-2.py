class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers

        #l and r 
        l, r = 0, 1
        #maxP
        maxP = 0
        #while r < len(prices)
        while r < len(prices):
            #if l < r
            if prices[l] < prices[r]:
                #profit = r - l
                profit = prices[r] - prices[l]
                #maxP = max(maxP, profit)
                maxP = max(maxP, profit)
            #else
            else:
                #l = r
                l = r
            #r+=1
            r+=1
        #return maxP
        return maxP

                