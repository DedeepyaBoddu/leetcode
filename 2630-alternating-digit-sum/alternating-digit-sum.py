class Solution:
    def alternateDigitSum(self, n: int) -> int:
        stack = []
        while n != 0:
            stack.append(n%10)
            n = n//10

        factor = 1
        ans =0
        print(stack)
        while stack:
            k = stack.pop()
            ans += k*factor
            factor = factor*(-1)
        
        return ans


            

        