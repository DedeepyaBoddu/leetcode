class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = start = 0
        minlen = float('inf')
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                    minlen = min(minlen, end - start+1)
                    curr_sum -= nums[start]
                    start += 1

        return 0 if minlen == float('inf') else minlen
                
                







        