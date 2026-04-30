class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in range(len(operations)): # for op in operations:
            if operations[op] == "C": #if op == "C"
                if result:
                    result.pop()
            elif operations[op] == "D": # elif op == "D":
                result.append(2*result[-1])
            elif operations[op] == "+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(operations[op])) # result.append(int(op))
        return sum(result)
        