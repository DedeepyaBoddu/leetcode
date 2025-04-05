class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        cd = 0
        min_g = float("inf")
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            cd += (g - c)
            if cd < min_g:
                min_g = cd
                start = i

        return (start + 1) % len(gas)

