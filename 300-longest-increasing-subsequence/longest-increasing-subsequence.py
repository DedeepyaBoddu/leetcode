class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] represents length of longest increasing subsequence for nums[i:]
        # reccurence dependency - for all nums greater than nums[i] in nums[i+1:], max longest +1
        dp = [1]*(len(nums)+1)
        dp[-1] = 0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)



        