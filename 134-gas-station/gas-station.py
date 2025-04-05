class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index=-1

        if sum(gas) < sum(cost):
            return start_index
        
        diff = [g - c for g, c in zip(gas, cost)]

        c = 0
        min_g = float("inf")
        start = 0
        for i, d in enumerate(diff):
            c += d
            if c < min_g:
                min_g = c
                start = i

 

        return (start + 1) % len(gas)
            
