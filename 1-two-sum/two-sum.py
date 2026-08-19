class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = defaultdict(int)

        for i,num in enumerate(nums):
            if target-num in past:
                return [i, past[target-num]]
            past[num]=i

        