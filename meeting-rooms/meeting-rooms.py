class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        n = len(intervals)
        
        if n == 1:
            return True
        
        intervals.sort(key = lambda x : x[1])
        print(intervals)
        
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
            
        return True
            