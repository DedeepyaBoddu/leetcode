class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        cost.append(0)

        def dfs(i):
            if (i == n-1 or i == n):
                return cost[i]
            if i not in memo:
                memo[i] = cost[i]+min(dfs(i+1),dfs(i+2))
            return memo[i]
        
        return min(dfs(0),dfs(1))
        