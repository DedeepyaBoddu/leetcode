class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        hash_set = set()
        longest = 0
        while r < len(s):
            if s[r] in hash_set:
                while s[l] != s[r]:
                    hash_set.remove(s[l])
                    l +=1
                l +=1
            else:
                hash_set.add(s[r])
                longest = max(longest,len(hash_set))
            r +=1
        return longest
        
            