class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            length = 0
            if (num-1)  not in numset:
                i = num
                while i in numset:
                    length +=1
                    i +=1
            longest = max (longest,length)
        return longest 
            
                


        