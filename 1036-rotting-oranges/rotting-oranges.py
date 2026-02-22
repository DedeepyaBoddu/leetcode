class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        
        time = 0
        while q and fresh>0:
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if (0<=x < len(grid)) and (0<= y < len(grid[0])) and grid[x][y] == 1:
                        fresh -=1
                        grid[x][y] = 2
                        q.append((x,y))
            time +=1
        
        return time if fresh == 0 else -1
