
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sortedInterval = sorted(intervals, key = lambda x: x[0])
        # sorting the first index mean that if 
        result = []
        result.append(sortedInterval.pop(0))

        while sortedInterval:
            currInterval = sortedInterval.pop(0)
            if result[-1][1] >= currInterval[0]: 
                result[-1][1] = max(result[-1][1], currInterval[1])
            else:
                result.append([currInterval[0], currInterval[1]])
        return result