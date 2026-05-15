class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[1] and intervals[i][1] >= newInterval[0]:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
            else:
                result.append(intervals[i])
        result.append(newInterval)
        return sorted(result)
        