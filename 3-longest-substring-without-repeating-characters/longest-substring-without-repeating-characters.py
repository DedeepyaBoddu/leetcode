class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charset = set()
        maxlen = 0
        for end in range(0,len(s)):
                while s[end] in charset:
                    charset.remove(s[start])
                    start += 1
                charset.add(s[end])
                maxlen = max(maxlen,end - start +1)  
        return maxlen

            
            
            
