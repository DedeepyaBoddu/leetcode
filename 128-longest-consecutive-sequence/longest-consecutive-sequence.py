class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 1

        for num in numset:
            length = 1
            if (num-1) in numset:
                continue
            if (num+1) in numset:
                i = num+1
                while i in numset:
                    length +=1
                    i +=1
            longest = max (longest,length)
        return longest if len(nums)!=0 else 0
            
                


        