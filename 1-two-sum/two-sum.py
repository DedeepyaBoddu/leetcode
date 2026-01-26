class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dict1:
                return [i,dict1[diff]]
            dict1[num]=i
        
        