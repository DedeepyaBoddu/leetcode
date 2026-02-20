class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_map = {'2':'abc', '3': 'def', '4':'ghi',
                     '5': 'jkl', '6': 'mno', '7': 'pqrs',
                     '8': 'tuv', '9':'wxyz'}
        def dfs(string, digits):
            if digits == "":
                return res.append(string)
            for c in digit_map[digits[0]]:
                dfs(string+c, digits[1:])
                
        dfs("",digits)
        return res

        