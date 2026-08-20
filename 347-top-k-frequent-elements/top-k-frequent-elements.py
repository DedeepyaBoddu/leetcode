class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        freq = [[] for i in range(len(nums)+1)]
        for key,value in counter.items():
            freq[value].append(key)
        res = []
        count = 0
        for bucket in freq[::-1]:
            for num in bucket:
                res.append(num)
                count+=1
                if count==k:
                    return res

