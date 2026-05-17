class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        Total = 0
        for ch in s:
            idx1 = s.index(ch)
            idx2 = t.index(ch)
            Total += abs(idx1 - idx2)
        return Total
    
        