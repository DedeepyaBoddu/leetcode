class Solution:
    def numDecodings(self, s: str) -> int:
        one = two = 1

        for i in range(len(s)-1, -1, -1):
            res = 0
            if s[i] != "0":
                res = one
                if (i+1< len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"))):
                    res += two
            temp = one
            one = res
            two = temp

        return one
            

        