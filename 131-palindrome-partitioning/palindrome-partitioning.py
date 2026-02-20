class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sublist = []
        def ispalindrome(s):
            l,r = 0, len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(sublist.copy())           
            for j in range(i,len(s)):
                if ispalindrome(s[i:j+1]):
                    sublist.append(s[i:j+1])
                    dfs(j+1)
                    sublist.pop()

        dfs(0)
        return res
            






        
        

        