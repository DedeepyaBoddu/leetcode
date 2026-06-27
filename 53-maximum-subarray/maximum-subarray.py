class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        curr_sum = 0
        ## Greedy - no negative prefix, reset everytime prefix sum goes negative
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            
            max_sum = max(max_sum, curr_sum)
        return max_sum

            

        