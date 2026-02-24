class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edge_map = {i:[] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i!=j:
                    edge_map[i].append(j)

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in edge_map[i]:
                dfs(nei)
            

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count


                    
        