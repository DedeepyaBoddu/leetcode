class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        while haystack[:len(needle)] != needle:
            index += 1
            haystack = haystack[1:]
            if len(haystack) < len(needle):
                return -1
        return index

            
