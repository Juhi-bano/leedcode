class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #bruate force
        '''stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == "#":
                if stack1:
                    stack1.remove(stack1[-1])

        for j in range(len(t)):
            if t[j] == "#":
                if stack2:
                    stack2.remove(stack2[-1])
        if s[i] != t[j]:
            return False
        return True'''


        def valid_string(string):
            stack = []
            for ch in string:
                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)
        return valid_string(s) == valid_string(t)


        
        