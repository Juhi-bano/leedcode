class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        set_input = set()
        stack = []
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        for i, char in enumerate(s):
            if char in set_input:
                continue
            while stack and char < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                set_input.remove(removed)
            stack.append(char)
            set_input.add(char)
        return "".join(stack)
        