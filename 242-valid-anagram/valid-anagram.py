class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for ch in s:
            count1[ch] +=1
        for ch in t:
            count2[ch] +=1
        return count1==count2
        


        