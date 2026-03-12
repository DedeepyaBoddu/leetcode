class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for i in range(1,len(nums)):
            diff = nums[i]-nums[i-1]
            if diff > 0:
                if direction < 0: return False
                direction = 1
            if diff < 0:
                if direction > 0: return False
                direction = -1
        return True
        
            
        

                





        