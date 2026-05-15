class Solution:
    def addBinary(self, a: str, b: str) ->str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            Total = carry
            if i >= 0:
                Total += int(a[i])
                i -= 1
            if j >= 0:
                Total += int(b[j])
                j -= 1
            result.append(str(Total%2))
            carry = Total//2
        return "".join(result[::-1])

        