class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        string_add = s + s
        if goal in string_add:
            return True
        else:
            return False