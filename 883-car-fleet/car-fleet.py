class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)),reverse= True)
        stack = []
        for p,s in cars:
            (target - p)/s
            if not stack or (target - stack[-1][0])/stack[-1][1] < (target - p)/s:
                stack.append([p,s])
                
        return len(stack)