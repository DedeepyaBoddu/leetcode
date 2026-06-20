class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for j in range(len(s)):
            dp[j][j] = True
            count+=1
            for i in range(j):
                if s[i]==s[j] and ((j-i)<=2 or dp[i+1][j-1]==True):
                    dp[i][j]= True
                    count+=1
        
        return count
        