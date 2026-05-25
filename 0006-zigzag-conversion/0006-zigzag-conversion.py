class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [""]*numRows
        curr_row = 0
        direction = 1
        for ch in s:
            result[curr_row] += ch
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = - 1
            curr_row += direction
        return "".join(result)

        