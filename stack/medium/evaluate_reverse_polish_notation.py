from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                x_1 = stack.pop()
                x_0 = stack.pop()
                stack.append(x_0 - x_1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                x_div = stack.pop()
                x_mul = stack.pop()
                stack.append(int(x_mul / x_div))
        return stack.pop()


assert Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
assert Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
assert Solution().evalRPN(tokens=["4", "3", "-"]) == 1
