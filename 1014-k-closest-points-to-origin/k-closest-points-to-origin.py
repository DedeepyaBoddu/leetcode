class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i,j in points:
            dist.append([-i**2-j**2,i,j])
        maxheap = dist[0:k]
        heapq.heapify(maxheap)

        for x in dist[k:]:
            heapq.heappushpop(maxheap,x)

        return [[x,y] for [_,x,y] in maxheap]
        