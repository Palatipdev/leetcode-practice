class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       # solution 1:
        # Use Union Find
        
        self.parent = list(range(len(edges) +1))
        self.size = [1] * (len(edges) + 1)
        for i in range(0,len(edges)):
            if self.find(edges[i][0]) == self.find(edges[i][1]):
                marked = i
                continue
            else:
                self.union(edges[i][0], edges[i][1])
        if marked != -1:
            return edges[marked]
        else:
            return []

    def find(self, node: int) -> int:
        if (node != self.parent[node]):
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)
        if self.size[a_root] >= self.size[b_root]:
            self.size[a_root] += self.size[b_root]
            self.parent[b_root] = a_root
        else:
            self.size[b_root] += self.size[a_root]
            self.parent[a_root] = b_root
            
        

            