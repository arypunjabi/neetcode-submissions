from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append("A")
        for i in s:
            match i:
                case "}":
                    if not(stack.pop() == "{"):
                        return False
                case ")":
                    if not(stack.pop() == "("):
                        return False
                case "]":
                    if not(stack.pop() == "["):
                        return False
                case _:
                    stack.append(i)
        if(stack.pop() == "A"):
            return True
        return False

