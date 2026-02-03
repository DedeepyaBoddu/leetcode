class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        s1_dict = defaultdict(int)
        for ch in s1:
            s1_dict[ch] +=1
        win_dict = defaultdict(int)

        l=0
        for r in range(len(s2)):
            win_dict[s2[r]] +=1

            if r-l+1 > len(s1):
                win_dict[s2[l]] -=1
                if win_dict[s2[l]]==0:
                    del win_dict[s2[l]]
                l +=1
            
            if win_dict == s1_dict:
                return True
        return False

            
            
            
            
        
        