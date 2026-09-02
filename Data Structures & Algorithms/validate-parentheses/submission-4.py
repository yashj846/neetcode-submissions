class Solution:
    def isValid(self, s: str) -> bool:
        para_dict = {'(':')', '[':']', '{':'}'}
        closing_stack = []

        for i in s:
            if i in para_dict:
                closing_stack.append(para_dict[i])
                print(closing_stack)
            elif  len(closing_stack) != 0 and i == closing_stack[-1]:
                closing_stack.pop()
            else:
                return False

        if len(closing_stack) == 0:
            return True
        else: return False


