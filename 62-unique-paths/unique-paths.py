class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        def dfs(i,j):
            if i == 0 or j == 0:
                dp[i][j] =1
                return 1
            if dp[i][j]!=0:
                return dp[i][j]
            res = dfs(i,j-1)+dfs(i-1,j)
            dp[i][j] = res
            return res
        return dfs(m-1,n-1)

                
