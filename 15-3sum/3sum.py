class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, left in enumerate(nums):
            if i>0 and left == nums[i-1]:
                continue
            
            m = i+1
            r = len(nums)-1
            while m<r:
                sum = left + nums[m]+ nums[r]

                if sum > 0:
                    r -=1
                elif sum<0:
                    m +=1
                else:
                    triplets.append([left, nums[m], nums[r]])
                    m +=1
                    while nums[m] == nums[m-1] and m<r :
                        m +=1
        return triplets




        