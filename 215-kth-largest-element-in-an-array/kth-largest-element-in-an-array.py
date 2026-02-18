class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickselect(l,r):
            pivot = nums[random.randint(l,r)]

            left = l
            i = l
            right = r

            while i<=right:
                if nums[i]< pivot:
                    nums[left], nums[i] = nums[i],nums[left]
                    left +=1
                    i+=1
                elif nums[i] > pivot:
                    nums[right],nums[i] = nums[i], nums[right]
                    right -=1
                else:
                    i +=1
            
            if k < left:
                return quickselect(l, left-1)
            elif k > right:
                return quickselect(right+1,r)
            else:
                return nums[k]
        return quickselect(0,len(nums)-1)

    

                
