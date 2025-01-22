class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character in ['(', '[','{']:
                stack.append(character)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if character == ')':
                    if last != '(':
                        return False
                elif character == ']':
                    if last != '[':
                        return False
                else:
                    if last != '{':
                        return False
        if not stack:
            return True
        return False