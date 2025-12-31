class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i,cur,total):
            if total == target:
                result.append(cur)
                return
            if total > target or i >= len(candidates):
                return
            dfs(i, cur + [candidates[i]], total+candidates[i])
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return result