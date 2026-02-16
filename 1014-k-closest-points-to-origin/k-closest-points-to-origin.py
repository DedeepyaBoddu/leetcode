class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i,j in points:
            minheap.append([i**2+j**2,i,j])
        heapq.heapify(minheap)

        res = []
        while len(res)<k:
            dist, i, j = heapq.heappop(minheap)
            res.append([i,j])
        return res
        