class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-n for n in nums]
        heapq.heapify(maxheap)

        while len(maxheap)>len(nums)-k:
            x = heapq.heappop(maxheap)
        return -x

        