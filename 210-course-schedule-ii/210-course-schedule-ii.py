class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import deque
        q = deque()
        inorder = dict()
        outorder = dict()
        result = list()
        
        def bfs():
            while q:
                node = q.popleft()
                result.append(node)
                
                for child in outorder[node]:
                    inorder[child] -= 1
                    
                    if inorder[child] == 0:
                        q.append(child)
                    
        for i in range(numCourses):
            inorder[i] = 0
            outorder[i] = []
        
        for course, prereq in prerequisites:
            inorder[course] += 1              
            outorder[prereq].append(course)
        
        for course in inorder:
            if inorder[course] == 0:
                q.append(course)
        
        bfs()
        
        if len(result) != numCourses:
            return []
        
        return result
        