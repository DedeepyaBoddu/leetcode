class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = defaultdict(int)
        dictt = defaultdict(int)
        if len(s)==len(t):
            for i in range(len(s)):
                dicts[s[i]]+=1
                dictt[t[i]]+=1
            return dicts==dictt
        return False
    
