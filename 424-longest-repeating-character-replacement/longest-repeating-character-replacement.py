class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longest = count = 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] +=1
            max_freq = max(freq.values())
            while (r-l+1) - max_freq > k:
                freq[s[l]] -=1
                l +=1
            longest = max(longest, r-l+1)
        return longest

            
        