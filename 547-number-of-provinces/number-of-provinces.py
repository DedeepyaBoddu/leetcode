class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(node):
            while parent[node]!=node:
                node = parent[node]
            return node
        def union(i,j):
            p1,p2 = find(i), find(j)
            
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2]=p1
                rank[p1] += rank[p2]
            else:
                parent[p1]=p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= union(i,j)
        return res
                    
        