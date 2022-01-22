class UnionFind:
    def __init__(self, connections):
        self.parents = dict()
        self.ranks = dict()
        
        for s, e in connections:
            self.parents[s] = s
            self.parents[e] = e
            self.ranks[s] = s
            self.ranks[e] = e
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        
        return self.parents[u]
    
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = self.parents[pu]
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = self.parents[pv]
        else:
            self.parents[pv] = self.parents[pu]
            self.ranks[pu] += 1
            
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return edges
        
        uf = UnionFind(edges)
        
        for s, e in edges:
            if uf.isConnected(s, e):
                return [s, e]
            uf.union(s, e)
            
        return []