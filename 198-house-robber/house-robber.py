class Solution:
    def rob(self, nums: List[int]) -> int:
        one = two = 0

        for i in range(len(nums)):
            nums[i] = max(nums[i]+two, one)
            two = one
            one = nums[i]
        return nums[-1]
        