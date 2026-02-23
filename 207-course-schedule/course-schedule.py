class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            premap[i].append(j)

        def dfs(crs):
            #recusion stack tracking
            if crs in visited:
                return False
            #memoization
            if premap[crs] == []:
                return True
            visited.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            premap[crs] = []
            return True

        visited = set()
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        