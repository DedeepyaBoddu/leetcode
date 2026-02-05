class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)),reverse= True)
        stack = []
        for p,s in cars:
            (target - p)/s
            if stack and (target - stack[-1][0])/stack[-1][1] >= (target - p)/s:
                continue
            else:
                stack.append([p,s])
        return len(stack)