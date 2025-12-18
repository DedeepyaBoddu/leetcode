class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = longest = r =0
        count = [0]*26

        for r in range(len(s)):
            count[ord(s[r])-ord("A")]+=1
            if len(s[l:r+1])-max(count)>k:
                count[ord(s[l])-ord("A")]-=1
                l+=1

            longest = max(longest,r-l+1)
      
        return longest

            

        