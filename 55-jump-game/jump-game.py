class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if curr - i <= nums[i]:
                curr = i       
        return curr==0

            

