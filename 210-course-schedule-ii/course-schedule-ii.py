class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in rec_stack:
                return False
            if crs in finished:
                return True
            rec_stack.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            rec_stack.remove(crs)
            finished.add(crs)
            output.append(crs)
            return True
        output = []
        finished = set()
        rec_stack = set()
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output


        