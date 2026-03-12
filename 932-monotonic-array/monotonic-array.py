class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1,len(nums)):
            inc = inc and nums[i]>=nums[i-1]
            if not inc:
                break
        for i in range(1,len(nums)):
            dec = dec and nums[i]<=nums[i-1]
            if not dec:
                break
        return inc or dec
            
        

                





        