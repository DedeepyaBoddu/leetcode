class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        
        curr_sum = numbers[i] + numbers[j]
        while curr_sum != target:
            if curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            curr_sum = numbers[i] + numbers[j]
        return [i+1,j+1]





        