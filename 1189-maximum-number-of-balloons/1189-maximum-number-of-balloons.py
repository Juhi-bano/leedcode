class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a_count = 0
        b_count = 0
        l_count = 0
        o_count = 0
        n_count = 0
        for ch in text:
            if ch == "a" in text:
                a_count += 1
            if ch == "b" in text:
                b_count += 1
            if ch == "l" in text:
                l_count += 1
            if ch == "o" in text:
                o_count += 1
            if ch == "n" in text:
                n_count += 1
        return min(a_count,b_count,l_count//2,o_count//2,n_count)

