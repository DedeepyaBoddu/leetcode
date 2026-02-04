class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {')': '(', ']':'[', '}':'{'}

        for ch in s:
            if ch in mapping:
                if stack:
                    if mapping[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(ch)
                
        return True if not stack else False
            