class UnionFind:
    def __init__(self, indexes):
        self.parents = dict()
        self.ranks = dict()
    
        for i in range (len(indexes)):
            self.parents[i] = i
            self.ranks[i] = 1
            
    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])            
        
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pv] = pu
            self.ranks[pu] += 1
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        uf = UnionFind(isConnected)
        
        n = len(isConnected)
            
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        count = 0
        for k, p in uf.parents.items():
            if k == p:
                count += 1
            
        return count
        
        