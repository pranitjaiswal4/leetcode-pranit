class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        from heapq import heappush, heappop
        
        result = []
        
        dist = lambda x, y: (x**2 + y**2)**(1/2)
        
        for px, py in points:
            heappush(result, [dist(px, py), px, py] )
        
        ans = []
        for i in range(k):
            dist, x, y =  heappop(result)
            ans.append([x, y])
        
        return ans
        