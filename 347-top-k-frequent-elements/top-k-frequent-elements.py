class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] +=1

        freq = [[] for i in range(0, len(nums)+1)]
        for i,c in count.items():
            freq[c].append(i)

        res = []
        for c in range(len(freq)-1,0,-1):
            for i in freq[c]:
                res.append(i)
                if len(res) == k:
                    return res

