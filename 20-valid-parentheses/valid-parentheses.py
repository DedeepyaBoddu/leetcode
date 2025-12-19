class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {"]":"[", "}":"{",")":"("}

        for char in s:
            if char in b_map:
                if stack and stack[-1]==b_map[char]:
                    stack.pop()
                else:
                     return False
            else:
                stack.append(char)
        return True if not stack else False

        