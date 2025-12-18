class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = longest = 0
        r = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l +=1
            chars.add(s[r])
            longest = max(longest,len(chars))
        return longest



        