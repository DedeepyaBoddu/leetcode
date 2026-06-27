class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[n-1] = True

        for i in range(len(nums)-2, -1, -1):
            for jump in range(1, min(nums[i],n-1-i)+1):
                if dp[i + jump]:
                    dp[i] = True
                    break
            
        return dp[0]

            

