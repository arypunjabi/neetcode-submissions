class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                stack.append(stack.pop()+stack.pop())
            elif n == "-":
                stack.append((-1 * stack.pop()) + stack.pop())
            elif n == "*":
                stack.append(stack.pop()*stack.pop())
            elif n == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(n))
        return stack.pop()
