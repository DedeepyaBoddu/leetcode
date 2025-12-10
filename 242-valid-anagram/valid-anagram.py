class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in s:
            dict1[i] +=1
        for j in t:
            dict2[j] +=1
        return dict1==dict2