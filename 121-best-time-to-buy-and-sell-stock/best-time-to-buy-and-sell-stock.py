class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b,s = 0,1
        while s < len(prices):
            profit = 0
            if prices[b] <= prices[s]:
                max_profit = max(max_profit, (prices[s] - prices[b]))
                s +=1
            else:
                b = s
                s +=1
        return max_profit

            