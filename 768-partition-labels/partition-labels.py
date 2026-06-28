class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        start = 0
        end = s.rfind(s[0])

        for i,ch in enumerate(s):
            if i == end:
                res.append(end-start+1)
                start = end+1
                if start< len(s):
                    end = s.rfind(s[start])
            if s.rfind(ch)> end:
                end = s.rfind(ch)

        return res







        return res

                

        