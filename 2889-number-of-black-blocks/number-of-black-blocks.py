class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_count = defaultdict(int)
        for x, y in coordinates:
            for i,j in [(0,0),(-1,0),(0,-1),(-1,-1)]:
                if 0<= x+i < m-1 and 0<= y+j < n-1:
                    block_count[(x+i,y+j)] +=1
        
        arr = [0]*5
        for value in block_count.values():
            arr[value]+=1
        
        arr[0] = (m-1)*(n-1) - sum(arr[1:])
        return arr
