class Solution:
    def canJump(self, nums: List[int]) -> bool:

        idx_to_reach=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if idx_to_reach - i <= nums[i]:
                idx_to_reach=i
        return idx_to_reach == 0

