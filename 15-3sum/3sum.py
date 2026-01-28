class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    triplets.append([nums[i],nums[j],nums[k]])
                    j +=1
                    while nums[j] == nums[j-1] and j<k:
                        j +=1
                if total < 0:
                    j +=1
                else:
                    k -=1
        return triplets
