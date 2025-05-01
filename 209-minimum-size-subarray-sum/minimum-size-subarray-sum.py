class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = start = 0
        minlen = float('inf')
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                curr_sum -= nums[start]
                minlen = min(minlen, end-start+1)
                start += 1
        return minlen if minlen < len(nums)+1 else 0
                







        