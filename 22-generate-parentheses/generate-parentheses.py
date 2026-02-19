class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(string, open, close):
            if open == close == n:
                return res.append(string)
            elif open == close:
                dfs(string+"(", open+1, close)
            elif open > close:
                if open<n:
                    dfs(string+"(",open+1,close)
                    dfs(string+")",open, close+1)
                if open ==n:
                    dfs(string+")",open, close+1)

            
        dfs("(",1,0)
        return res








        