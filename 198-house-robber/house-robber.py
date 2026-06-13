class Solution:
    def rob(self, nums: List[int]) -> int:
        one = two = 0
        for i in range(0,len(nums)):
            nums[i] = max(two, nums[i]+one)
            one = two
            two = nums[i]
        return nums[-1]

        