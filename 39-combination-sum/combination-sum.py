class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >=len(candidates):
                return
            dfs(i, subset + [candidates[i]], total+candidates[i] )
            dfs(i+1, subset , total)
        dfs(0,[],0)
        return res
            