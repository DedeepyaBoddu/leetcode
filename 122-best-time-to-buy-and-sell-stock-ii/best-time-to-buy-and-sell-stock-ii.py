class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        #capture all the inclines
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return max(profit,0)
        