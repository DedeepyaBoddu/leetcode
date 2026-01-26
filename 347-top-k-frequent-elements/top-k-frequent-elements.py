class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num] +=1

        freq = [[] for i in range(len(nums)+1)]
        for num,c in dict1.items():
            freq[c].append(num)
        
        res = []
        for i in freq[::-1]:
            for ele in i:
                res.append(ele)
                if len(res)==k:
                    return res
                



