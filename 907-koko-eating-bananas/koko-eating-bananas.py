class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def finish(k):
            total_time = 0
            for pile in piles:
                t = pile//k if pile%k ==0 else (pile//k)+1
                total_time +=t
            return True if total_time <=h else False
            

        l, r = 1, max(piles)
        
        while l<=r:
            m = (l+r)//2
            if finish(m):
                r = m-1
            else:
                l = m+1
        return l


            

        