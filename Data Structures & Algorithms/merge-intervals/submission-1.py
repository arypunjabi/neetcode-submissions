class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        queue = deque()
        queue.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= queue[-1][1]:
                temp = queue.pop()
                queue.append([temp[0], max(temp[1], intervals[i][1])])
            else:
                queue.append(intervals[i])

    
        return list(queue)