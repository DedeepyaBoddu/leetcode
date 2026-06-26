class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i] is a state that represents if s[i:] can be segmented
        dp = {len(s): True}

        for i in range(len(s)-1,-1,-1):
            res = False
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    res = dp[i + len(word)]
                if res:
                    break
            dp[i] = res
        return dp[0]
        