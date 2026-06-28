class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(len(triplets)):
            a = b = c = False
            for j in range(0,3):
                if triplets[i][j] > target[j]:
                    triplets[i] = [0,0,0]
        res0 = target[0] == max([t[0] for t in triplets])
        res1 = target[1] == max([t[1] for t in triplets])
        res2 = target[2] == max([t[2] for t in triplets])
        return res0 and res1 and res2
        
        