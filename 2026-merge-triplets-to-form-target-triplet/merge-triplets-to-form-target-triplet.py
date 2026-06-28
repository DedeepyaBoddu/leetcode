class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res0 = res1 = res2 = False

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                if not res0 and x == target[0]:
                    res0 = True
                if not res1 and y == target[1]:
                    res1 = True
                if not res2 and z == target[2]:
                    res2 = True
        return res0 and res1 and res2
                    

        
        