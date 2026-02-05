class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            if token in set(['+','-','*','/']):
                y = int(stack.pop())
                x = int(stack.pop())
                if token == '+':
                    stack.append(x+y)
                elif token == '-':
                    stack.append(x-y)
                elif token == '*':
                    stack.append(x*y)
                elif token == '/':
                    stack.append(x/y)
            else:
                stack.append(token)
        return int(stack.pop())
                


        


        