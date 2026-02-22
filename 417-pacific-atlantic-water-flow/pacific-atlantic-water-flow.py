class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()

        def flow(i,j, visited,prev_height):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i,j) in visited or heights[i][j] < prev_height:
                return
            elif heights[i][j] >= prev_height:
                visited.add((i,j))
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                flow(x,y,visited,heights[i][j])

        for i in range(len(heights[0])):
            flow(0,i,pac,0)
            flow(len(heights)-1,i,atl,0)

        for j in range(len(heights)):
            flow(j,0,pac,0)
            flow(j,len(heights[0])-1,atl,0)


        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])
        
        return result
            




        