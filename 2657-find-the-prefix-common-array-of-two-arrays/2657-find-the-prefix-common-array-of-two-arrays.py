class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        setA = set()
        setB = set()
        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            count = 0
            for num in setA:
                if num in setB:
                    count += 1
            result.append(count)
        return result
        