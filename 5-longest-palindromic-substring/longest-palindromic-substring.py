class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s

        res = s[0]
        res_len = 1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for j in range(len(s)):
            dp[j][j] = True
            for i in range(j):
                if s[i] == s[j] and ((j-i)<=2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    if (j-i+1) > res_len:
                        res = s[i:j+1]
                        res_len = j-i+1
        return res
                
        