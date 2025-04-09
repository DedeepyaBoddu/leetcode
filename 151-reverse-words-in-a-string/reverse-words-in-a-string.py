class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        out = ' '.join(words[::-1])
        return out
        