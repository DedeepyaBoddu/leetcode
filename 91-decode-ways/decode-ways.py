class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {0:1}

        for i in range(1,len(s)+1):
            res = 0
            if s[i-1] != "0":
                res += dp[i-1]
            if (i-2>= 0 and (s[i-2]=="1" or (s[i-2]=="2" and s[i-1] in "0123456"))):
                    res += dp[i-2]
            dp[i] = res
        return dp[len(s)]
            

        