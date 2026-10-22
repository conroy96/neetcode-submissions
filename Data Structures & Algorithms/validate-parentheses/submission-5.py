class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            "[":"]",
            "(":")",
            "{":"}"
        }
        stack = []
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if not stack and s[i] not in braces:
                return False
            elif s[i] in braces:
                stack.append(s[i])
            elif s[i] != braces[stack[-1]]:
                return False
            else:
                stack.pop()
        return len(stack) == 0


        