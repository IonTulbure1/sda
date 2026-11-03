
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                ultimul = stack.pop()

                if c == ')' and ultimul != '(':
                    return False
                if c == ']' and ultimul != '[':
                    return False
                if c == '}' and ultimul != '{':
                    return False

        return len(stack) == 0

