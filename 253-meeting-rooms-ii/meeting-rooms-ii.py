class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count = max_count = 0
        s = e = 0
        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            max_count = max(max_count,count)
        return max_count
