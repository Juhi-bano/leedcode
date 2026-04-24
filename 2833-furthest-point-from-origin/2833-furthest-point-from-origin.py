class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = 0
        R = 0
        blank = 0
        for ch in moves:
            if ch == 'L':
                L += 1
            elif ch == 'R':
                R += 1
            else:
                blank += 1 
        return abs(R-L)+blank
