class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string = str(n)
        ans = 0
        for i,digit in enumerate(string):
            if i%2 ==0:
                ans += int(digit)
            else:
                ans -= int(digit)
        return ans


        

            

        