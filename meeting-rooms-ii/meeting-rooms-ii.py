class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        
        starts.sort()
        ends.sort()
        
        s, e = 0, 0
        
        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
            else:
                e += 1
                
            s += 1
                
        return rooms