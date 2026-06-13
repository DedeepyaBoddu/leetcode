class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = cost[n-2]
        two = cost[n-1]

        for i in range(n-3,-1,-1):
            cost[i] = cost[i] + min(one, two)
            two = one
            one = cost[i]
        return min(one,two)

        