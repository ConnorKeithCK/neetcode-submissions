class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for par in list(s):
            if par in valid.values():
                stack.append(par)
            if par in valid.keys():
                if stack and stack[-1] == valid[par]:
                    stack.pop()
                else:
                    return False

        print(stack)
        return len(stack) == 0
