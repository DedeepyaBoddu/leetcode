class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            
            for idx in range(0,3):
                if idx not in good:
                    if target[idx] == triplets[i][idx]:
                        good.add(idx)
        return len(good) == 3
                    

        
        