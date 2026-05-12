class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newstart = newInterval[0]
        newend = newInterval[1]
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if end < newstart:
                result.append([start, end])
            elif start > newend:
                result.append([newstart, newend])
                return result + intervals[i:]
            else:
                newstart = min(start, newstart)
                newend = max(end, newend)
                
        result.append([newstart, newend])
        return result