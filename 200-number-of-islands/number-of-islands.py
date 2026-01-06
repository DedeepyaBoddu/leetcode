class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        def dfs(i,j):
            
            if i >=0 and j >=0 and i <len(grid) and j < len(grid[0]) and grid[i][j]=="1" and (i,j) not in visited:
                visited.add((i,j))
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    islands+=1
                    dfs(i,j)
        return islands
        
            
            
            


                
        