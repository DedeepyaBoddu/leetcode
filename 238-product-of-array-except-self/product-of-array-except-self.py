class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        n=len(nums)

        for i in range(1,n):
                prefix[i]= nums[i-1]*prefix[i-1]
                suffix[n-i-1] = nums[n-i]*suffix[n-i]
        
        for i in range(len(nums)):
            answer[i]=prefix[i]*suffix[i]
        return answer
                
