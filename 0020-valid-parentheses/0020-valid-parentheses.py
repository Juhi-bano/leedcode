class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for v in s:
            if len(stack) != 0 and v == ")" and stack[-1] == "(":
                stack.pop()
            elif len(stack) != 0 and v == "]" and stack[-1] == "[":
                stack.pop()
            elif len(stack) != 0 and v == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(v)
        if len(stack) != 0:
            return False
        return True


        