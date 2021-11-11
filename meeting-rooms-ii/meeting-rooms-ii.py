#     Approach 1: MinHeap
#     Time complexity: O(n log n), Space Complexity: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        occupied = list()

        intervals.sort()

        heappush(occupied, [intervals[0][1], intervals[0][0]])
        rooms = 1

        for i in range(1, len(intervals)):
            if occupied[0][0] > intervals[i][0]:
                rooms += 1
            else:
                heappop(occupied)

            heappush(occupied, [intervals[i][1], intervals[i][0]])

        return rooms

#     Approach 2: Chronological Ordering
#     Time complexity: O(n log n), Space Complexity: O(n)
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         rooms = 0
        
#         starts = [interval[0] for interval in intervals]
#         ends = [interval[1] for interval in intervals]
        
#         starts.sort()
#         ends.sort()
        
#         s, e = 0, 0
        
#         while s < len(starts):
#             if starts[s] < ends[e]:
#                 rooms += 1
#             else:
#                 e += 1
                
#             s += 1
                
#         return rooms
