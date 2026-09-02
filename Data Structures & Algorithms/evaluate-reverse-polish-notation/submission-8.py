class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i not in signs:
                stack.append(int(i))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if i == '+':
                    stack.append(val1 + val2)
                elif i == '-':
                    stack.append(val2 - val1)
                elif i == '*':
                    stack.append(val1 * val2)
                elif i == '/':
                    stack.append(int(val2 / val1))
        return int(stack[0])


        