class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for i in range(len(s)):
            pos = t.find(s[i]) 
            if pos == -1:
                return False
            elif i == len(s)-1:
                return True
            else:
                t = t[pos+1:]

            
            