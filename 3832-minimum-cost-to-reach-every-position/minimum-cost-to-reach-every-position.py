class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        result = []
        min = cost[0]
        for i in range(len(cost)):
            if min > cost[i]:
                min = cost[i]
            result.append(min)
            i += 1
        return result

        