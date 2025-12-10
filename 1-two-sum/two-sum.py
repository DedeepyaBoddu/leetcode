class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()
        for i in range(0,len(nums)):
            val = target-nums[i]
            if val in dict1:
                return [i,dict1[val]]
            dict1[nums[i]] = i

        