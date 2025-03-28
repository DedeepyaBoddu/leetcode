class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        max_freq= max(dict.values())
        freq_key = [key for key, value in dict.items() if value == max_freq][0]
        return freq_key
        