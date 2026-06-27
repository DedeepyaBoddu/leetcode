class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = level = 0
        while r < len(nums)-1:
            level +=1
            temp = r
            for i in range(l,r+1):
                r = max(r, i+nums[i])
            l = temp +1
        return level





        