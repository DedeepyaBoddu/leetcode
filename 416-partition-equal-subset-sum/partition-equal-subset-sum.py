class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = {0}

        for num in nums:
            temp = dp.copy()
            for i in dp:
                temp.add(i+num)
                temp.add(i)
            dp = temp


        return True if target in dp else False


        return dp[target]



        