class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        l = longest = 0

        for r in range(len(s)):
            hash_map[s[r]] +=1
            while len(s[l:r+1]) - max(hash_map.values(), default=0) > k:
                hash_map[s[l]] -=1
                l +=1
            
            longest = max(longest,len(s[l:r+1]))

        return longest


                
            


