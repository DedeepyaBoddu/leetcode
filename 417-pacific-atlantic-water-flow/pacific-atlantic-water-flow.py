class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()

        def pacific(i,j, prev_height):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i,j) in pac or heights[i][j] < prev_height:
                return
            if i == 0 or j == 0:
                pac.add((i,j))
            elif heights[i][j] >= prev_height:
                pac.add((i,j))
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                pacific(x,y,heights[i][j])

        def atlantic(i,j, prev_height):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i,j) in atl or heights[i][j] < prev_height:
                return
            if i == len(heights)-1 or j == len(heights[0])-1:
                atl.add((i,j))
            elif heights[i][j] >= prev_height:
                atl.add((i,j))
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                atlantic(x,y,heights[i][j])

        for i in range(len(heights[0])):
            pacific(0,i,0)
            atlantic(len(heights)-1,i,0)

        for j in range(len(heights)):
            pacific(j,0,0)
            atlantic(j,len(heights[0])-1,0)


        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])
        
        return result
            




        