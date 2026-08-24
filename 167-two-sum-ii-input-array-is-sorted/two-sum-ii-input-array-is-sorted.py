class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        curr_sum = numbers[l]+numbers[r]
        while curr_sum != target:
            if target > curr_sum:
                l +=1
            if target < curr_sum:
                r -=1
            curr_sum = numbers[l] + numbers[r]
        return [l+1,r+1]
            
                
            
