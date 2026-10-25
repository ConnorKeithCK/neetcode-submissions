class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i, op in enumerate(operations):
            if op == "+":
                stack.append(stack[-2] + stack[-1])
                continue
            if op == "C":
                stack.pop()
                continue
            if op == "D":
                stack.append(stack[-1] * 2)
                continue

            stack.append(int(op))
        
        return sum(stack)