class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def ispalindrome(s):
            l,r = 0, len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True

        def dfs(rem_str,sublist):
            #substr = s[:i+1]
            if not rem_str:
                res.append(sublist.copy())
            
            for i in range(len(rem_str)):
                if ispalindrome(rem_str[:i+1]):
                    dfs(rem_str[i+1:],sublist+ [rem_str[:i+1]])

        dfs(s, [])
        return res
            






        
        

        