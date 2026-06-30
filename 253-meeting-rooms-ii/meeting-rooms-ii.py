class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        heap = [intervals[0][1]]
        max_rooms = 1
        for start,end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
            max_rooms = max(max_rooms,len(heap))
        return max_rooms
            