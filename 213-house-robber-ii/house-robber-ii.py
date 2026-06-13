class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def house_robber1(nums):
            one = two = 0

            for i in range(0,len(nums)):
                temp = max(two, nums[i] + one)
                one = two
                two = temp
            return two
        return max(nums[0],house_robber1(nums[0:-1]),house_robber1(nums[1:]))

        