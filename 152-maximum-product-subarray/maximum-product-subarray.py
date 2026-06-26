class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = 1
        res = max(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                max_prod = min_prod = 1
            tmp = max_prod
            max_prod = max(nums[i]*tmp, nums[i]*min_prod, nums[i])
            min_prod = min(nums[i]*tmp, nums[i]*min_prod, nums[i])
            res = max(res,max_prod)

        return res

