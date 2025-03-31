class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bp = prices[0]
        profit =0

        for p in prices[1:]:
            if bp>p:
                bp=p
            profit = max(profit, p-bp)
        return profit

        # max_profit=[]
        # for i in range(0,len(prices)-1):
        #     max_p = max([prices[j]-prices[i] for j in range(i+1,len(prices))])
        #     max_p = max(max_p,0)
        #     max_profit.append(max_p)
        # return max(max_profit, default=0)